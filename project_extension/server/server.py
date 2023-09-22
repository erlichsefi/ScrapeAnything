from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/recommend", methods=["POST"])
def data():
    data = request.get_json()
    coordinates = process(data)
    return jsonify(coordinates)
if __name__ == "__main__":
    app.run(port=3000)
