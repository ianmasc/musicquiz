# You might need to add more of these import statements as you implement your controllers.
from app import app
from flask import render_template
from flask import request
from flask import session
from helpers import GENRES_LIST
from helpers import get_score
from helpers import clear_score

@app.route('/')
def index():
    
    choice = request.args.get("choice")
    
    if choice == 'Change Genre':
        clear_score()
    


    choice = request.args.get("choice")

    if choice == 'a':
        clear_score()

    if 'num_correct' not in session:
        session['num_correct'] = 0
        session['num_total'] = 0


    m = get_score()
    session['m'] = m

    data = {
        "genres": GENRES_LIST,

    }

    return render_template("index.html", m = m, **data)
