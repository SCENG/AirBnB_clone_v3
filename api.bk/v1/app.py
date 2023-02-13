#!/usr/bin/python3
"""flask app"""

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exceptipon):
    """Tear down method."""
    storage.close()

@app.errorhandler(404)
def error_404(error):
    return  make_response(jsonify(error='Not found'), 404)


if __name__ == '__main__':
    H = getenv('HBNB_API_HOST')
    P = getenv('HBNB_API_PORT')
    Host = H if H else '0.0.0.0'
    Port = P if P else 5000
    app.run(host=Host, port=Port, threaded=True)