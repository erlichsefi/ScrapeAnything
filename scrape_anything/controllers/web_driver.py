from ..browser import *
from ..view import *
from ..think import *
from ..act import *
from .controller import Controller
from selenium.common.exceptions import WebDriverException

class WebDriverController(Controller):


    def __init__(self,url) -> None:
        try:
            self.web_driver = start_browesr(selenium_host="selenium-chrome")
            self.web_driver.set_window_size(1024, 768)
            self.web_driver.get(url)
            self.url = url
        except Exception as e:
            self.close()
            raise e
            


    def fetch_infomration_on_screen(self,output_folder:str,loop_num:int):
        # compute the elements on screen, current + change
        raw_on_screen, viewpointscroll,viewportHeight,width_scroll,height_scroll = get_screen_information(self.web_driver)

        # get screen size
        width,height = get_screen_size(self.web_driver)
        screen_size = f"width={width},height={height}"
        scroll_ratio = f"On the Width Axis, {width_scroll}. On the Height Axis, {height_scroll}"

        file_name_png = web_driver_to_image(self.web_driver,f"{output_folder}/step_{loop_num+1}")
        file_name_html = web_driver_to_html(self.web_driver,f"{output_folder}/step_{loop_num+1}")

        # store the raw elements before processing
        raw_on_screen.to_csv(f"{output_folder}/step_{loop_num+1}_raw.csv")
        # minimize the data sent to the llm + enrich
        on_screen = minimize_and_enrich_page_data(raw_on_screen,viewpointscroll,viewportHeight,file_name_png)
        # store the minimized elements 
        on_screen.to_csv(f"{output_folder}/step_{loop_num+1}_minimized.csv",index=False)

        return on_screen,viewpointscroll,viewportHeight,screen_size,file_name_png,file_name_html,scroll_ratio,self.url
    

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