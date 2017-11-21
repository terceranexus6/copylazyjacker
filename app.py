# -*- coding: utf- 8 -*-

from flask import Flask, render_template, jsonify
import json
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

#@app.route("/")


#def status():
#    data={"status":"OK"}
#    return json.dumps(data)
@app.route("/status")
def get():
    schema = {
        "status": "OK"
    }
    return jsonify(schema)

#api.add_resource(status, '/status')


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    # escucha a cualquier interfaz, desde cualquier sitio y (modo debug) SOLO EN DEV, NO EN PRODUCCION
