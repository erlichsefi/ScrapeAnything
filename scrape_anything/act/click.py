from .tool import ToolInterface
from .draw import draw_arrow

class ClickOnCoordinates(ToolInterface):
  """Click on certain coordinate on the screen """

  name :str = "Click on coordinates on the screen"
  description:str = "click on x,y coordinates in order to move to the next screen. Input format: {{\"x\": <place_num_here>,\"y\":<place_num_here>}}"
  click_on_screen:bool = True

  def use(self,web_driver:object, x: float, y:float) -> str:
      js_script = f"return document.elementFromPoint({x}, {y})"
      input_field = web_driver.execute_script(js_script)
      # Enter the text into the input field
      input_field.click()

  def example(self,web_driver: object, x:float ,y:float) -> None:
      draw_arrow(web_driver,x,y,"click here")

class EnterText(ToolInterface):
    """Click on a field and enter text"""

    name:str = "Enter Text"
    description:str = "Click on a field and enter text, Input format: {{\"text\":\"<text_to_enter>\",\"x\": <place_num_here>,\"y\":<place_num_here>}}"
    click_on_screen:bool = True

    def use(self, web_driver: object, x:float ,y:float, text: str) -> None:
        js_script = f"return document.elementFromPoint({x}, {y})"
        input_field = web_driver.execute_script(js_script)

        # Enter the text into the input field
        input_field.click()
        input_field.send_keys(text)


    def example(self,web_driver: object, x:float ,y:float, text: str) -> None:
        draw_arrow(web_driver,x,y, f"enter '{text}' here")