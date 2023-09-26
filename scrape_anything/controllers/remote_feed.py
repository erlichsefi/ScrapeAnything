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
        raw_on_screen, viewpointscroll,viewportHeight,scroll_width,scroll_height = incoming_data.raw_on_screen,incoming_data.viewpointscroll,incoming_data.viewportHeight,incoming_data.scroll_width,incoming_data.scroll_height
        width = incoming_data.width
        height = incoming_data.height
        url = incoming_data.url
        file_name_png = None
        file_name_html = None

        return self.process_screen_data(raw_on_screen,scroll_width,scroll_height,width,height,output_folder,viewpointscroll,viewportHeight,url,loop_num,file_name_png=file_name_png,file_name_html=file_name_html)

    

    def take_action(self,tool_executor:ToolInterface,tool_input:str,num_loops:int,output_folder:str):

        self.outgoing_data_queue.put(OutGoingData(description=tool_executor.description,
                                                  **tool_input))

        
        

    def close(self):
        pass