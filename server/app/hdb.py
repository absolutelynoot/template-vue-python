from app import app
from flask import request, jsonify

@app.route("/hdb/test")
def testHdb():
    return "hdb data application is working" 