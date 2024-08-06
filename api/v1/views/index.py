#!/usr/bin/python3
"""My End-Points With their routes"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def Status():
    """My Status"""
    data = {
            "status": "OK"
            }
    return jsonify(data)
