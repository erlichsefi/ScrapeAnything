from selenium.webdriver.common.action_chains import ActionChains
from .tool import ToolInterface

class GoBack(ToolInterface):
    """go back to previous page"""

    name:str = "Go Back"
    description:str = "Go back to the previous page,no input."

    def use(self, web_driver: object) -> None:
        # Simulate clicking the browser's "Next" button
        web_driver.back()

def change_url_twice(web_driver,first_page,second_page):
  web_driver.get(first_page)
  web_driver.get(second_page)

from selenium.webdriver.common.action_chains import ActionChains

class Refresh(ToolInterface):
    """go back to previous page"""

    name:str = "Refresh page"
    description:str = "refresh the current page,no input."

    def use(self, web_driver: object) -> None:
        # Simulate clicking the browser's "Next" button
        web_driver.refresh()
