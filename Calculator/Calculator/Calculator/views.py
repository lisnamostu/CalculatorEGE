"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Calculator import app

@app.route('/')
@app.route('/maket')
def maket():
    """Renders the maket page."""
    return render_template(
        'maket.html',
        title='Home Page',
    )
