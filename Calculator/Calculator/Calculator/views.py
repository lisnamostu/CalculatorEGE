"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request
from Calculator import app
import pandas as pd

@app.route('/')
def Website():
    """Renders the Calculator page."""
    return render_template('Calculator.html')

@app.route('/calculatefive', methods=["POST"])
def CalculateFive():
    print(request.json)
    return jsonify(message="success"+request.json)

@app.route('/calculateall', methods=["GET", "POST"])
def CalculateAll():
    data = request.json["data"]