from .tool import ToolInterface
from .draw import scroll_right,scroll_down

class ScrollDown(ToolInterface):
    """Scroll down the web page by half the screen height"""

    name:str = "Scroll Down"
    description:str = "Scroll down the web page by half the screen height, no input."

    def use(self, web_driver: object) -> None:
        # Get the height of the web page
        page_height = web_driver.execute_script("return document.body.scrollHeight")

        # Get the height of the viewport
        viewport_height = web_driver.execute_script("return window.innerHeight")

        # Calculate the scroll distance (half the screen height)
        scroll_distance = viewport_height // 2

        # Scroll down the web page
        web_driver.execute_script(f"window.scrollBy(0, {scroll_distance});")

    def example(self,web_driver: object) -> None:
        scroll_down(web_driver)

class ScrollUp(ToolInterface):
    """Scroll up the web page by half the screen height"""

    name:str = "Scroll Up"
    description:str = "Scroll up the web page by half the screen height, no input."

    def use(self, web_driver: object) -> None:
        # Get the height of the viewport
        viewport_height = web_driver.execute_script("return window.innerHeight")

        # Calculate the scroll distance (half the screen height)
        scroll_distance = viewport_height // 2

        # Scroll up the web page
        web_driver.execute_script(f"window.scrollBy(0, -{scroll_distance});")

class ScrollRight(ToolInterface):
    """Scroll the web page to the right by half the screen width"""

    name :str= "Scroll Right"
    description:str = "Scroll the web page to the right by half the screen width, no input"

    def use(self, web_driver: object) -> None:
        # Get the width of the viewport
        viewport_width = web_driver.execute_script("return window.innerWidth")

        # Calculate the scroll distance (half the screen width)
        scroll_distance = viewport_width // 2

        # Scroll the web page to the right
        web_driver.execute_script(f"window.scrollBy({scroll_distance}, 0);")

    def example(self,web_driver: object) -> None:
        scroll_right(web_driver)