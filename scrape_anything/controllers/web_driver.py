from ..browser import *
from ..view import *
from ..think import *
from ..act import *
from .controller import Controller
from selenium.common.exceptions import WebDriverException
import pickle

class WebDriverController(Controller):


    def __init__(self,url,cache_to_pickle=False) -> None:
        try:
            self.web_driver = start_browesr(selenium_host="selenium-chrome")
            self.web_driver.set_window_size(1024, 768)
            self.web_driver.get(url)
            self.url = url
            self.cache_to_pickle = cache_to_pickle
        except Exception as e:
            self.close()
            raise e
        

    def fetch_infomration_on_screen(self,output_folder:str,loop_num:int):
        # compute the elements on screen, current + change
        raw_on_screen, viewpointscroll, viewportHeight, scroll_width, scroll_height = get_screen_information(self.web_driver)
        # get screen size
        width,height = get_screen_size(self.web_driver)
        url = get_url(self.web_driver)

        if self.cache_to_pickle:
            self.pickle(
                raw_on_screen=raw_on_screen,
                viewpointscroll=viewpointscroll,
                viewportHeight=viewportHeight,
                scroll_width=scroll_width,
                scroll_height=scroll_height,
                width=width,
                height=height,
                url=url
                )

        file_name_png = web_driver_to_image(self.web_driver,f"{output_folder}/step_{loop_num+1}")
        file_name_html = web_driver_to_html(self.web_driver,f"{output_folder}/step_{loop_num+1}")

        return self.process_screen_data(raw_on_screen,scroll_width,scroll_height,width,height,output_folder,viewpointscroll,viewportHeight,url,loop_num,file_name_png=file_name_png,file_name_html=file_name_html)
    

    def take_action(self,tool_executor:ToolInterface,tool_input:str,num_loops:int,output_folder:str):
        initial_page_url = self.web_driver.current_url

        if tool_executor.is_click_on_screen():
            draw_on_screen(self.web_driver,f"{output_folder}/step_{str(num_loops)}",**tool_input)
        try:
            tool_executor.use(self.web_driver,**tool_input)
        except WebDriverException as e:
            message_without_session_id = str(e).split("\n")[0]
            raise ValueError(f"tool execution failed,{message_without_session_id}")
        
        after_tool_url = self.web_driver.current_url
        
        need_to_wait = initial_page_url != after_tool_url
        # if the tool worked, wait and sample the site again. 
        if need_to_wait:
            wait_for_page_load(self.web_driver)

    def close(self):
        try:
            if self.web_driver != None:
               self.web_driver.close()
               self.web_driver.quit()
        except UnboundLocalError:
            raise ValueError("please start server")