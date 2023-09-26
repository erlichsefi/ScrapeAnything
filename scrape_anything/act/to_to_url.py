from .tool import ToolInterface
from .draw import go_to_url

class GoToURL(ToolInterface):
  """ Go to a specific url address """

  name:str = "Go to a specific url web address"
  description:str = "Change the url to a provied URL. Input format: {{\"url\":\"<place_url_here>\"}}"
  click_on_screen:str = True

  def use(self, web_driver:object, url: str)-> None:
      web_driver.get(url)

  def example(self,web_driver: object, url:str) -> None:
      go_to_url(web_driver,text=f"go to {url}")

def change_url(web_driver,first_page):
  web_driver.get(first_page)

#example_tool(GoToURL,url="https://www.google.com/",setup_function=lambda wd:change_url(wd,"https://www.n12.co.il/"))