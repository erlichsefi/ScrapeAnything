from flask import Flask, request, jsonify

app = Flask(__name__)

def process(data):
    print(data)
    return {"left": 100, "top": 200}

@app.route("/data", methods=["POST"])
def data():
    data = request.get_json()
    coordinates = process(data)
    return jsonify(coordinates)
if __name__ == "__main__":
    app.run(port=3000)
