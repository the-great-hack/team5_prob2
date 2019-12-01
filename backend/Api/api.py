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
     "locationTitle": "Firdous Market",
     "vehicleType": "Car"
  },{
     "locationTitle": "Hafeez Center",
     "vehicleType": "Completed"
  }],
     "totalCost": "250",
     "arrivalTime": "9:45 PM"
  },{
    "steps":[{
     "locationTitle": "DHA Phase 8",
     "vehicleType": "Car"
  },{
     "locationTitle": "Hafeez Center",
     "vehicleType": "Completed"
  }],
     "totalCost": "450",
     "arrivalTime": "9:15 PM"
  },{
    "steps":[{
     "locationTitle": "DHA Phase 8",
     "vehicleType": "Car"
  },{
     "locationTitle": "Khayabane Jinah",
     "vehicleType": "Bus"
  },{
     "locationTitle": "Siddique Trade center",
     "vehicleType": "Bike"
  },{
     "locationTitle": "Hafeez Center",
     "vehicleType": "Completed"
  }],
     "totalCost": "230",
     "arrivalTime": "10:00 PM"
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

