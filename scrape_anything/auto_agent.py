import datetime
import os
import threading

from pydantic import BaseModel


from scrape_anything.browser import *
from scrape_anything.view import *
from scrape_anything.think import *
from scrape_anything.act import *
from scrape_anything.controllers import Controller
from scrape_anything.tools import ToolBox


class Agent(BaseModel):
    llm: ChatLLM
    max_loops: int = 1
    tool_box : ToolBox = ToolBox()
    

    
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

    def make_a_decide_on_next_action(self, prompt: str,num_loops:int, output_folder:str,tool_box:ToolBox) -> str:        
        generated = self.llm.generate(prompt,output_folder,num_loops)

        tool, tool_input = extract_tool_and_args(generated,tool_box.final_answer_token)

        return generated, tool, parse_json(tool_input)

    def run_parallel(self,controller: Controller, task_to_accomplish: str):
        thread = threading.Thread(target=self.run,args=(controller, task_to_accomplish))
        thread.start()

        return thread
        
    def run(self, controller: Controller, task_to_accomplish: str):
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
            
            while num_loops < self.max_loops or self.max_loops == -1:
                num_loops += 1
                print(f"--- Iteration {num_loops} ---")
                
                curr_prompt = format_prompt(today = datetime.date.today(),
                    site_url=url,
                    tool_description=self.tool_box.tool_description,
                    tool_names=self.tool_box.tool_names,
                    task_to_accomplish=task_to_accomplish,
                    previous_responses="\n".join(previous_responses),
                    on_screen_data=on_screen,
                    screen_size=screen_size,scroll_ratio=scroll_ratio,
                )
                
                generated = "parsing generation failed"
                try:
                    generated, tool, tool_input = self.make_a_decide_on_next_action(curr_prompt,num_loops,output_folder,self.tool_box)
                    tool_executor = self.tool_box.get_tool(tool, tool_input)
                    controller.take_action(tool_executor, tool_input,num_loops,output_folder)
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
