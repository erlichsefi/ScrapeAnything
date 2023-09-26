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
      go_to_url(web_driver,url)
