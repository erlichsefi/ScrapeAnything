from scrape_anything import Agent
from scrape_anything import ChatLLM
from scrape_anything import RemoteFeedController,OutGoingData,IncommingData
from queue import Queue
import os
import glob

user_task = "log in to my account,user name is 'erlichsefi@gmail.com', password is '1234567'"
experiment = "outputs/16_02_14_2023_09_26x6fb55dca_e942_4426_861c_75d312cedeb3"


feed_from_chrome = Queue(maxsize=1)
feed_from_agent = Queue(maxsize=1)

controller = RemoteFeedController(
    incoming_data_queue=feed_from_chrome,
    outgoing_data_queue=feed_from_agent
    ) 
controller.unpickle(experiment,0)

agnet = Agent(llm=ChatLLM(),max_loops=1)
thread = agnet.run_parallel(controller,task_to_accomplish=user_task)

call_to_action = feed_from_agent.get()

thread.stop()
    