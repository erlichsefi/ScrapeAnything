from scrape_anything import Agent
from scrape_anything import ChatLLM


agnet = Agent(llm=ChatLLM(),max_loops=10)
agnet.run("log in to my account,user name is 'erlichsefi@gmail.com', password is '1234567'","https://www.wishingwell.co.il/")