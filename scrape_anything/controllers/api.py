from flask import Flask, request, jsonify
from queue import Queue
from scrape_anything import Agent, ChatLLM, RemoteFeedController, IncommingData
import json


app = Flask(__name__)
SOME_DB = dict()

@app.route('/process', methods=['POST'])
def process_json():
    try:
        data = request.get_json()
        if data is not None and "session_id" in data and "user_task" in data:
            user_task = data["user_task"]
            session_id = data["session_id"]
            response_data = init_and_process(session_id, user_task, data)
            return jsonify(response_data)
        else:
            return jsonify({'error': 'Invalid JSON input'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def init_agent(user_task, session_id):
    feed_from_chrome = Queue(maxsize=1)
    feed_from_agent = Queue(maxsize=1)

    controller = RemoteFeedController(
        incoming_data_queue=feed_from_chrome,
        outgoing_data_queue=feed_from_agent
    )
    agent = Agent(llm=ChatLLM(), max_loops=1)
    thread = agent.run_parallel(controller, task_to_accomplish=user_task)

    SOME_DB[session_id] = (feed_from_chrome, feed_from_agent)

def process_request(data, session_id):
    (feed_from_chrome, feed_from_agent) = SOME_DB[session_id]
    feed_from_chrome.put(IncommingData(**data))
    response = feed_from_agent.get()
    return json.dumps(response)

def init_and_process(session_id, user_task, params):
    if session_id not in SOME_DB:
        init_agent(user_task, session_id)
    return process_request(params, session_id)

if __name__ == '__main__':
    app.run(debug=True)
