from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if (functionName == "add"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):

        postedData = request.get_json()

        status_code = checkPostedData(postedData, "add")

        if (status_code != 200):
            retJson = {
                'Message': "An error happened",
                "Status Coe": status_code
            }
            return jsonify(retJson)


        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x + y
        retMap = {
            'Message': ret,
            'Status Code' : 200
        }
        return jsonify(retMap)


class Subtrack(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass

api.add_resource(Add, "/add")


@app.route('/')
def hello_world():
    return "Hello Word"

@app.route("/add_two_nums", methods =["POST"])
def add_two_nums():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]

    z = x+y

    retJSON= {
        "z": z
    }

    return jsonify(retJSON), 200

@app.route('/bye')
def bye():
    c = 2*534

    s = str(c)

    age = 2*5
    retJson = {
        'Name': 'Elfarouk',
        'Age' : age,
        "phones": [
            {
                "phoneName": "Iphone8",
                "phoneNumber": 11111
            },
            {
                "phoneName": "Nokia",
                "phoneNumber": 11121
            }
        ]
    }
    return jsonify(retJson)

if __name__ =='__main__':
    app.run(host="127.0.0.1", port=80)

