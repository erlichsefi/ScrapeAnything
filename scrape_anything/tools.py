from typing import List, Dict
from pydantic import BaseModel

from scrape_anything.browser import *
from scrape_anything.view import *
from scrape_anything.think import get_stop_patterns,get_final_answer_token
from scrape_anything.act import *

class ToolBox(BaseModel):
    final_answer_token:str = get_final_answer_token()
    tools: List[ToolInterface] = [ClickOnCoordinates(),EnterText(),GoBack(),ScrollRight(),ScrollUp(),ScrollDown(),Refresh(),HitAKey()]
    stop_pattern: List[str] = get_stop_patterns()
    
    @property
    def tool_description(self) -> str:
        return "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])

    @property
    def tool_names(self) -> str:
        return ",".join([tool.name for tool in self.tools])

    @property
    def tool_by_names(self) -> Dict[str, ToolInterface]:
        return {tool.name: tool for tool in self.tools}


    def get_tool(self,tool:str, tool_input:str) -> ToolInterface:
        if tool == self.final_answer_token:
            return tool_input

        if tool not in self.tool_by_names:
            raise ValueError(f"unknown tool:{tool}")

        return self.tool_by_names[tool]