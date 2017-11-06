# -*- coding: utf- 8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")


def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    # escucha a cualquier interfaz, desde cualquier sitio y (modo debug) SOLO EN DEV, NO EN PRODUCCION
