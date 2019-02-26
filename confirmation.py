from app import app
from flask import render_template
from flask import session
from flask import request
from helpers import clear_score

@app.route('/confirmation')
def confirmation():

    
    return render_template("confirmation.html")
