from .tool import ToolInterface

class GoToURL(ToolInterface):
  """ Go to a specific url address """

  name:str = "Go to a specific url web address"
  description:str = "Change the url to a provied URL. Input format: {{\"url\":\"<place_url_here>\"}}"
  click_on_screen:str = True
  example_script:str = "go_to_url.js"

  def use(self, web_driver:object, url: str)-> None:
      web_driver.get(url)


  def process_tool_arg(self,**kwarg):
    url = kwarg['url']
    return {
        "url":f"You should go to {url}"
    }
