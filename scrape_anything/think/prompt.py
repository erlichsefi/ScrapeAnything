FINAL_ANSWER_TOKEN = "Final Answer:"
OBSERVATION_TOKEN = "Observation:"
THOUGHT_TOKEN = "Thought:"
PROMPT_TEMPLATE = """
Today is {today}, the site i'm looking on is {site_url}.

Here is a representation of what is see on my screen in a table shape:
{on_screen_data}

Current screen size: 
{screen_size}

Scroll Options: 
{scroll_ratio}

You should accomplish the task given to you as best as you can using the following tools:

{tool_description}
--
Use the following format:

Question: the input question you must answer.
Thought: comment on what you want to do next.
Input Field: The coordinates and the values of elements that accept input on screen.
Input Field Thought: comment on what are the Input Field are used for.
Buttons: The coordinates of the buttons on screen. what there are used for?
Buttons Thought: comment on what are the Buttons are used for.
Execution Status: comment on if the your previous executions what is successful.
Action: the action to take, exactly one element of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation repeats N times, use it until you are sure of the answer)
Thought: I now know the final answer
Final Answer: your final answer to the original input question 

Begin!
--
Task To Accomplish: {task_to_accomplish}
Previous executions:
{previous_responses}
"""

def get_stop_patterns():
    return [f'\n{OBSERVATION_TOKEN}', f'\n\t{OBSERVATION_TOKEN}']

def format_prompt(**kwrgs):
    return  PROMPT_TEMPLATE.format(**kwrgs)
