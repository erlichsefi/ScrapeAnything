
import re
from typing import Tuple
import json


def make_a_decide_on_next_action(llm, prompt: str,num_loops:int, output_folder:str,final_answer_token:str,stop_pattern:list[str]) -> str:        
    generated = llm.generate(prompt,stop_pattern,output_folder,num_loops)

    tool, tool_input = extract_tool_and_args(generated,final_answer_token)

    return generated, tool, parse_json(tool_input)

def extract_tool_and_args(generated: str, final_answer_token:str) -> Tuple[str, str]:
    if final_answer_token in generated:
        return "Final Answer", generated.split(final_answer_token)[-1].strip()

    if "Action Input" in generated:
        regex = r"Action: [\[]?(.*?)[\]]?[\n]*Action Input:[\s]*(.*)"
        match = re.search(regex, generated, re.DOTALL)
        if not match:
            raise ValueError(f"the output `{generated}` is not matching the expected format.")
        tool = match.group(1).strip()
        tool_input = match.group(2)
    else:
        tool = generated.split("Action:")[-1].strip()
        tool_input = "{}"

    return strip_tool(tool), strip_characther_in_args(tool_input)

def strip_tool(string:str):
    return re.sub(r'[^a-zA-Z ]', '', string).strip(" ").strip('"')

def strip_characther_in_args(string:str):
    string_temp = string.strip(" ").strip('"').strip("None").strip("\n")
    string_temp  = "{"+string_temp.split("{")[-1]
    string_temp = string_temp.split("}")[0] + "}"
    return string_temp

def parse_json(tool_input:str):
    try:
        response = json.loads(tool_input)
    except Exception as e:
        raise ValueError(f"the output `{tool_input}` is not a JSON, error = {e}")
    return response