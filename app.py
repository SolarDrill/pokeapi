from flask import Flask, jsonify
import constants
from files_utils import read_file
from utils import init_pokemons


app = Flask(__name__)

@app.route("/")
def index():
    data = {"data": constants.ENDPOINTS}
    return data, 200

@app.route("/pokemon/a")
def pokemon_a():
    try:
        data = read_file(constants.POKEA)
        return data, 200
    except Exception as e:
        return "Error", 400

@app.route("/pokemon/e")
def pokemon_e():
    try:
        data = read_file(constants.POKEE)
        return data, 200
    except Exception as e:
        return "Error", 400

@app.route("/pokemon/i")
def pokemon_i():
    try:
        data = read_file(constants.POKEI)
        return data, 200
    except Exception as e:
        return "Error", 400

@app.route("/pokemon/o")
def pokemon_o():
    try:
        data = read_file(constants.POKEO)
        return data, 200
    except Exception as e:
        return "Error", 400

@app.route("/pokemon/u")
def pokemon_u():
    try:
        data = read_file(constants.POKEU)
        return data, 200
    except Exception as e:
        return "Error", 400

@app.route("/pokemon/consonant")
def pokemon_consonant():
    try:
        data = read_file(constants.POKEC)
        return data, 200
    except Exception as e:
        return "Error", 400

if __name__ == '__main__':
    init_pokemons()
    app.run('0.0.0.0', 8081, threaded=True)
    print('ok')