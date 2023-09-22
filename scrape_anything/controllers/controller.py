from abc import ABC, abstractmethod




class Controller(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def init_feed(self):
        pass

    @abstractmethod
    def fetch_infomration_on_screen(self,output_folder:str,loop_num:int):
        pass


    @abstractmethod
    def take_action(self,tool:str, tool_input:str,num_loops:int,output_folder:str):
        pass

    @abstractmethod
    def close(self):
        pass
