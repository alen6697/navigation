import requests

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return "Welcome to Navigation Servie"

@app.route('/navigation', methods=['GET'])
def navigate():
    # http://0.0.0.0:8081/navigation?start=8.681495%2C49.41461&end=8.687872%2C49.420318

    start = request.args.get("start")
    end = request.args.get("end")

    url = "http://ors-app:8080/ors/v2/directions/driving-car?start={0}&end={1}".format(start, end)
    res = requests.get(url)

    return res.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
