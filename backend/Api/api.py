import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def jsonString(name,email):
  dummy_data = [{
    "steps":[{
     "locationTitle": "DHA Phase 8",
     "vehicleType": "Car"
  },{
     "locationTitle": "Walton road lahore",
     "vehicleType": "Bus"
  },{
     "locationTitle": "Gulberg",
     "vehicleType": "Car"
  }],
     "totalCost": "450",
     "arrivalTime": "9:45 PM"
  },{
    "steps":[{
     "locationTitle": "Liberty Market",
     "vehicleType": "Car"
  },{
     "locationTitle": "Mall road canal bridge",
     "vehicleType": "Bus"
  },{
     "locationTitle": "Mughalpura Zakir tikka",
     "vehicleType": "Car"
  }],
     "totalCost": "350",
     "arrivalTime": "1:45 PM"
  },{
    "steps":[{
     "locationTitle": "Hafeez Center",
     "vehicleType": "Car"
  },{
     "locationTitle": "Firozpur road canal bridge",
     "vehicleType": "Bus"
  },{
     "locationTitle": "Johar town",
     "vehicleType": "Car"
  }],
     "totalCost": "275",
     "arrivalTime": "2:45 PM"
  }
  ]
  return json.dumps(dummy_data)

@app.route('/', methods=['GET'])
def home():

    query_parameters = request.args

    name = query_parameters.get('name')
    email = query_parameters.get('email')

    # output = "My name is "
    # + name+ " and email is"+ email
    return jsonString(name,email)

app.run()

