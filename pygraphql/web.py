from flask import Flask
from flask import jsonify, request

from graphqlmodels.cars import get_cars
import utils

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cars')
def cars():
    return jsonify(get_cars())

@app.route('/car', methods=['POST'])
def car():
    if request.method == 'POST':
        car_name = request.values.get("Name")
        car_price = request.values.get("Price")
        utils.add_car(car_name, car_price)
        return '', 204 
    else:
        return ''
