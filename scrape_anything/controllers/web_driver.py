from ..browser import *
from ..view import *
from ..think import *
from ..act import *
from selenium.common.exceptions import WebDriverException
from .controller import Controller

class WebDriverController(Controller):


    def __init__(self,url) -> None:
        self.web_driver = None
        self.url = url

    def init_feed(self):
        self.web_driver = start_browesr()
        self.web_driver.set_window_size(1024, 768)
        self.web_driver.get(self.url)

    def fetch_infomration_on_screen(self,output_folder:str,loop_num:int):
        # compute the elements on screen, current + change
        raw_on_screen, viewpointscroll,viewportHeight,scroll_ratio = get_screen_information(self.web_driver)

        # get screen size
        screen_size = get_screen_size(self.web_driver)
        file_name_png = web_driver_to_image(self.web_driver,f"{output_folder}/step_{loop_num+1}")
        file_name_html = web_driver_to_html(self.web_driver,f"{output_folder}/step_{loop_num+1}")

        # store the raw elements before processing
        raw_on_screen.to_csv(f"{output_folder}/step_{loop_num+1}_raw.csv")
        # minimize the data sent to the llm + enrich
        on_screen = minimize_and_enrich_page_data(raw_on_screen,viewpointscroll,viewportHeight,file_name_png)
        # store the minimized elements 
        on_screen.to_csv(f"{output_folder}/step_{loop_num+1}_minimized.csv",index=False)

        return on_screen,viewpointscroll,viewportHeight,screen_size,file_name_png,file_name_html,scroll_ratio,self.url
    

    def take_action(self,tool:str, tool_input:str,num_loops:int,output_folder:str):
        if tool == self.final_answer_token:
            return tool_input

        if tool not in self.tool_by_names:
            raise ValueError(f"unknown tool:{tool}")

        initial_page_url = self.web_driver.current_url
        tool_executor = self.tool_by_names[tool]
        
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
               self. web_driver.close()
               self.web_driver.quit()
        except UnboundLocalError:
            raise ValueError("please start server")