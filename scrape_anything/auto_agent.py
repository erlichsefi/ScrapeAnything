import datetime
import os
import uuid
from .controllers.web_driver import WebDriver

from pydantic import BaseModel
from typing import List, Dict


from .browser import *
from .view import *
from .think import *
from .act import *
from .controllers import Controller


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

    def run(self,controller, task_to_accomplish: str):
        output_folder = os.path.join("outputs",self.get_output_folder())
        os.makedirs(output_folder)
        
        on_screen = None
        try:
            previous_responses = []
            previous_responses_status = ""
            num_loops = 0
     
            on_screen,_,_,\
            screen_size,_, _,\
                scroll_ratio,url = controller.fetch_infomration_on_screen(output_folder,loop_num=num_loops)
            
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
                    controller.take_action(tool, tool_input,num_loops,output_folder)
                    previous_responses_status = "successful."
                    
                except ValueError as e:
                    previous_responses_status = f"failed, {str(e)}"
                    print(f"WARNINGS: {str(e)}")
                
                finally:
                     on_screen,_,_,\
                     screen_size,_, _,\
                     scroll_ratio,url = controller.fetch_infomration_on_screen(output_folder,loop_num=num_loops)

                previous_responses.append(f"\n\nPrevious {num_loops} response:\n{self.clean_empty_lines(generated)}\nexecution status:{previous_responses_status}")
        except Exception as e:
            raise e
        finally:
            controller.close()
