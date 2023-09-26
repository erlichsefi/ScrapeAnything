from scrape_anything import Agent
from scrape_anything import ChatLLM
from scrape_anything import RemoteFeedController,OutGoingData,IncommingData
from queue import Queue


user_task = "log in to my account,user name is 'erlichsefi@gmail.com', password is '1234567'"
current_site = "https://www.wishingwell.co.il/"


fake_data = IncommingData()



feed_from_chrome = Queue(maxsize=1)
feed_from_agent = Queue(maxsize=1)

controller = RemoteFeedController(current_site,
                                url=current_site,
                                incoming_data_queue=feed_from_chrome,
                                outgoing_data_queue=feed_from_agent) 


agnet = Agent(llm=ChatLLM(),max_loops=-1)
agnet.run(controller,task_to_accomplish=user_task)