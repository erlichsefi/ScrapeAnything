import datetime
import os
import uuid

from pydantic import BaseModel
from typing import List, Dict
from selenium.common.exceptions import WebDriverException


from .browser import *
from .view import *
from .think import *
from .act import *



class Agent(BaseModel):
    llm: ChatLLM
    tools: List[ToolInterface] = [ClickOnCoordinates(),EnterText(),GoBack(),ScrollRight(),ScrollUp(),ScrollDown(),Refresh(),HitAKey()]
    max_loops: int = 1
    # The stop pattern is used, so the LLM does not hallucinate until the end
    stop_pattern: List[str] = get_stop_patterns()
    final_answer_token:str = get_final_answer_token()

    @property
    def tool_description(self) -> str:
        return "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])

    @property
    def tool_names(self) -> str:
        return ",".join([tool.name for tool in self.tools])

    @property
    def tool_by_names(self) -> Dict[str, ToolInterface]:
        return {tool.name: tool for tool in self.tools}
    
    @staticmethod
    def clean_empty_lines(generated:str):
        return "\n".join(list(filter(lambda x: len(x.strip())>0,generated.split("\n"))))
    
    def take_action(self,web_driver, tool:str, tool_input:str,num_loops:int,output_folder:str):
        if tool == self.final_answer_token:
            return tool_input

        if tool not in self.tool_by_names:
            raise ValueError(f"unknown tool:{tool}")

        initial_page_url = web_driver.current_url
        tool_executor = self.tool_by_names[tool]
        
        if tool_executor.is_click_on_screen():
            draw_on_screen(web_driver,f"{output_folder}/step_{str(num_loops)}",**tool_input)
        try:
            tool_executor.use(web_driver,**tool_input)
        except WebDriverException as e:
            message_without_session_id = str(e).split("\n")[0]
            raise ValueError(f"tool execution failed,{message_without_session_id}")
        
        after_tool_url = web_driver.current_url
        return initial_page_url != after_tool_url
        
    def fetch_infomration_on_screen(self,web_driver,output_folder:str,loop_num:int):
        # compute the elements on screen, current + change
        raw_on_screen, viewpointscroll,viewportHeight,scroll_ratio = get_screen_information(web_driver)

        # get screen size
        screen_size = get_screen_size(web_driver)
        file_name_png = web_driver_to_image(web_driver,f"{output_folder}/step_{loop_num+1}")
        file_name_html = web_driver_to_html(web_driver,f"{output_folder}/step_{loop_num+1}")

        # store the raw elements before processing
        raw_on_screen.to_csv(f"{output_folder}/step_{loop_num+1}_raw.csv")
        # minimize the data sent to the llm + enrich
        on_screen = minimize_and_enrich_page_data(raw_on_screen,viewpointscroll,viewportHeight,file_name_png)
        # store the minimized elements 
        on_screen.to_csv(f"{output_folder}/step_{loop_num+1}_minimized.csv",index=False)

        return on_screen,viewpointscroll,viewportHeight,screen_size,file_name_png,file_name_html,scroll_ratio

    def get_output_folder(self):
        import uuid
        import datetime

        # Generate a UUID and replace dashes with underscores
        uuid_str = str(uuid.uuid4()).replace("-", "_")

        # Get the current date and time
        current_datetime = datetime.datetime.now()

        # Format the date and time as a string
        datetime_str = current_datetime.strftime("%H_%M_%S_%Y_%m_%d")

        # Combine the UUID and datetime
        return f"{datetime_str}x{uuid_str}"

    def run(self, task_to_accomplish: str, url:str):
        output_folder = os.path.join("outputs",self.get_output_folder())
        os.makedirs(output_folder)
        
        on_screen = None
        web_driver = None
        try:
            web_driver = start_browesr()
            web_driver.set_window_size(1024, 768)
            web_driver.get(url)

            previous_responses = []
            previous_responses_status = ""
            num_loops = 0
     
            on_screen,_,_,\
            screen_size,_, _,\
                scroll_ratio = self.fetch_infomration_on_screen(web_driver,output_folder,loop_num=num_loops)
            
            while num_loops < self.max_loops:
                num_loops += 1
                print(f"--- Iteration {num_loops} ---")
                
                curr_prompt = format_prompt(today = datetime.date.today(),
                    site_url=url,
                    tool_description=self.tool_description,
                    tool_names=self.tool_names,
                    task_to_accomplish=task_to_accomplish,
                    previous_responses="\n".join(previous_responses),
                    on_screen_data=on_screen,
                    screen_size=screen_size,scroll_ratio=scroll_ratio,
                )
                
                generated = "parsing generation failed"
                try:
                    generated, tool, tool_input = make_a_decide_on_next_action(self.llm,curr_prompt,num_loops,output_folder,self.final_answer_token,self.stop_pattern)
                    need_to_wait = self.take_action(web_driver, tool, tool_input,num_loops,output_folder)
                    previous_responses_status = "successful."

                    # if the tool worked, wait and sample the site again. 
                    if need_to_wait:
                        wait_for_page_load(web_driver)
                    
                except ValueError as e:
                    previous_responses_status = f"failed, {str(e)}"
                    print(f"WARNINGS: {str(e)}")
                
                finally:
                     on_screen,_,_,\
                     screen_size,_, _,\
                     scroll_ratio = self.fetch_infomration_on_screen(web_driver,output_folder,loop_num=num_loops)

                
                previous_responses.append(f"\n\nPrevious {num_loops} response:\n{self.clean_empty_lines(generated)}\nexecution status:{previous_responses_status}")

        except Exception as e:
            raise e
        finally:
            try:
                if web_driver != None:
                    web_driver.close()
                    web_driver.quit()
            except UnboundLocalError:
                raise ValueError("please start server")
