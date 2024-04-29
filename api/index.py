from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError
from datetime import datetime
import pytz

app = Flask(__name__)
manila_timezone = pytz.timezone('Asia/Manila')

class CoordinatesSchema(Schema):
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)

coordinates = {
    'latitude': 14.0833428,
    'longitude': 121.1440427,
    'updated_at': datetime.now(manila_timezone).isoformat(),
}

coordinates_schema = CoordinatesSchema()

@app.route('/')
def home():
    return "Hello World!"

@app.route('/api/coordinates', methods=['GET', 'POST'])
def handle_coordinates():
    global coordinates

    if request.method == 'GET':
        return jsonify(coordinates), 200

    elif request.method == 'POST':
        try:
            data = coordinates_schema.load(request.json)
            coordinates.update(data)
            manila_time = datetime.now(manila_timezone).isoformat()
            coordinates['updated_at'] = manila_time
            print(coordinates)
            return jsonify(coordinates), 200
        except ValidationError as err:
            return str(err), 400

if __name__ == '__main__':
    app.run(debug=True)
