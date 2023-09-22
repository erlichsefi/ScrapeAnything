from ..browser import *
from ..view import *
from ..think import *
from ..act import *
from .controller import Controller
from .data_types import IncommingData,OutGoingData
from queue import Queue



class RemoteFeedController(Controller):

    def __init__(self,url,incoming_data_queue:Queue,outgoing_data_queue:Queue) -> None:
        self.url = url
        self.incoming_data_queue = incoming_data_queue
        self.outgoing_data_queue = outgoing_data_queue

    def fetch_infomration_on_screen(self,output_folder:str,loop_num:int):

        incoming_data:IncommingData = self.incoming_data_queue.get()
        # compute the elements on screen, current + change
        raw_on_screen, viewpointscroll,viewportHeight,scroll_ratio = incoming_data.raw_on_screen,incoming_data.viewpointscroll,incoming_data.viewportHeight,incoming_data.scroll_ratio
        # store the raw elements before processing
        raw_on_screen.to_csv(f"{output_folder}/step_{loop_num+1}_raw.csv")

        
        # get screen size
        screen_size = f"width={incoming_data.width},height={incoming_data.height}"
        file_name_png = None
        file_name_html = None


        # minimize the data sent to the llm + enrich
        on_screen = minimize_and_enrich_page_data(raw_on_screen,viewpointscroll,viewportHeight,file_name_png)
        # store the minimized elements 
        on_screen.to_csv(f"{output_folder}/step_{loop_num+1}_minimized.csv",index=False)

        return on_screen,viewpointscroll,viewportHeight,screen_size,file_name_png,file_name_html,scroll_ratio,self.url
    

    def take_action(self,tool_executor:ToolInterface,tool_input:str,num_loops:int,output_folder:str):

        self.outgoing_data_queue.put(OutGoingData(description=tool_executor.description,
                                                  **tool_input))

        
        

    def close(self):
        pass