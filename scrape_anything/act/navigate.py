from .tool import ToolInterface
from .draw import refresh,go_back_a_page

class GoBack(ToolInterface):
    """go back to previous page"""

    name:str = "Go Back"
    description:str = "Go back to the previous page,no input."

    def use(self, web_driver: object) -> None:
        # Simulate clicking the browser's "Next" button
        web_driver.back()

    def example(self, web_driver: object) -> None:
        # Simulate clicking the browser's "Next" button
        go_back_a_page(web_driver)

class Refresh(ToolInterface):
    """go back to previous page"""

    name:str = "Refresh page"
    description:str = "refresh the current page,no input."

    def use(self, web_driver: object) -> None:
        # Simulate clicking the browser's "Next" button
        web_driver.refresh()

    def example(self, web_driver: object) -> None:
        # Simulate clicking the browser's "Next" button
        refresh(web_driver)
