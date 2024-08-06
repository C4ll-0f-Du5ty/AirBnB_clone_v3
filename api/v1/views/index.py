#!/usr/bin/python3
"""My End-Points With their routes"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.engine.db_storage import classes


@app_views.route('/status', strict_slashes=False)
def Status():
    """My Status"""
    data = {
            "status": "OK"
            }
    return jsonify(data)


@app_views.route('/stats', strict_slashes=False)
def Stats():
    """Endpoint that retrieves the number of each objects by type"""
    return jsonify({
        key: storage.count(value) for key, value in classes.items()
    })
