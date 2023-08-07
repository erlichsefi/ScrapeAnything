from pydantic import BaseModel

class ToolInterface(BaseModel):
    name: str
    description: str
    click_on_screen:bool = False

    def is_click_on_screen(self) -> bool:
      return self.click_on_screen