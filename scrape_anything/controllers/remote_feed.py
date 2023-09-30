from ..browser import *
from ..view import *
from ..think import *
from ..act import *
from .controller import Controller
from .data_types import IncommingData,OutGoingData,EnabledActions
from queue import Queue



class RemoteFeedController(Controller):

    def __init__(self,incoming_data_queue:Queue,outgoing_data_queue:Queue) -> None:
        self.incoming_data_queue = incoming_data_queue
        self.outgoing_data_queue = outgoing_data_queue

    def fetch_infomration_on_screen(self,output_folder:str,loop_num:int):

        incoming_data:IncommingData = self.incoming_data_queue.get()
        # compute the elements on screen, current + change
        file_name_png = None
        file_name_html = None

        return self.process_screen_data(incoming_data,output_folder,loop_num,file_name_png=file_name_png,file_name_html=file_name_html)

    

    def take_action(self,tool_executor:ToolInterface,tool_input,num_loops:int,output_folder:str):

        self.outgoing_data_queue.put(OutGoingData(description=tool_executor.description,
                                                  tool_enum=EnabledActions.get_tool_enum(tool_executor),
                                                  example_script=tool_executor.example_script,
                                                  tool_input=tool_executor.process_tool_arg(**tool_input)))

        
    def unpickle(self, output_folder, loop_num):
        data = super().unpickle(output_folder, loop_num)
        self.incoming_data_queue.put(data)
        

    def close(self):
        pass