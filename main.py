from scrape_anything import Agent
from scrape_anything import ChatLLM
from scrape_anything import WebDriverController


controller = WebDriverController("https://www.wishingwell.co.il/") 

agnet = Agent(llm=ChatLLM(),max_loops=10)
agnet.run(controller,"log in to my account,user name is 'erlichsefi@gmail.com', password is '1234567'")