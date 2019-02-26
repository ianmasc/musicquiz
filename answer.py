from app import app
from flask import render_template
from flask import request
from flask import session
from helpers import get_score
import requests
from bs4 import BeautifulSoup

@app.route('/answer')
def answer():

    userAnswer = request.args.get("choice")

    correctAnswer = session.get('songTitle', None)
    correctAnswer1 = session.get('songArtist', None)

    firstPart = 'https://www.youtube.com/results?search_query='
    secondPart = correctAnswer + ' ' + correctAnswer1
    secondPart = secondPart.replace(' ', '+')
    youtubeUrl = firstPart + secondPart

    resp = requests.get(youtubeUrl)
    soup = BeautifulSoup(resp.text, "html.parser")

    youtube = "https://www.youtube.com/embed/"
    tags = soup.find_all("h3", {"class": "yt-lockup-title"})
    tag = tags[1].find('a')['href']
    tag = tag[9:len(tag)]
    tag = youtube + tag


    genreA = session.get('genre', None)

    mess = get_score()

    answer = "'" + correctAnswer  + "'" + " by " + correctAnswer1
    if userAnswer == answer:
        message = "You are correct!"
        session['num_correct'] = 1 + session.get('num_correct')
        session['num_total'] = 1 + session.get('num_total')
    else:
        message = "Sorry, you are incorrect."
        session['num_total'] = 1 + session.get('num_total')

    mess = get_score()
    session['m'] = mess

    return render_template("answer.html", userAnswer = userAnswer, mess = mess, genreA = genreA, message = message, answer = answer, tag = tag)
