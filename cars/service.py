from flask import abort, Flask, Response
import json, time

app = Flask(__name__)

data = None
with open('cars.json', 'r') as file:
    data = json.load(file)

state = {"current": "normal"}

@app.route("/cars", methods=['GET'])
def get_cars():
    if state["current"] == "backedup":
        return "", 504
    elif state["current"] == 'slow':
        time.sleep(5)
        return json_response(data)
    else:
        return json_response(data)

@app.route("/state", methods=['GET'])
def get_state():
    return json_response(state)

@app.route("/state/slow", methods=['POST'])
def slowdown():
    state["current"] = "slow"
    return 'ok'

@app.route("/state/backedup", methods=['POST'])
def error():
    state["current"] = "backedup"
    return 'ok'

@app.route("/state/normal", methods=['POST'])
def resolve():
    state["current"] = "normal"
    return 'ok'

def json_response(hash_data):
    response = Response(json.dumps(hash_data))
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == "__main__":
    print(" Starting CARS service")
    print(" Endpoints:")
    print(" * GET /cars")
    print(" * GET /state")
    print(" * POST /state/slow")
    print(" * POST /state/backedup")
    print(" * POST /state/normal")
    app.run("0.0.0.0")
