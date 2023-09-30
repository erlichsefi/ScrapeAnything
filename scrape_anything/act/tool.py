from pydantic import BaseModel
from scrape_anything.browser import action_with_js_code
import os


class ToolInterface(BaseModel):
    name: str
    description: str
    click_on_screen:bool = False
    example_script:str = ""

    def is_click_on_screen(self) -> bool:
      return self.click_on_screen

    def process_tool_arg(self,**_):
      return {}

    def example(self,web_driver,*arg,**kwarg):
      assert len(arg) == 0
      action_with_js_code(web_driver,os.path.join(os.path.join(os.getcwd(),"shared", "actions"),self.example_script),self.process_tool_arg(**kwarg))