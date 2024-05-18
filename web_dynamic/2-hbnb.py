#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from flask import Flask, render_template
from api.v1.views import app_views
from flask import jsonify
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def teardown_db(exception):
    """ Closes storage on teardown """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ Handles 404 errors """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', '5003'))
    app.run(host=host, port=port, threaded=True)
