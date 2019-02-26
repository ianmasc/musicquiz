# You might need to add more of these import statements as you implement your controllers.
from app import app
from flask import render_template
from flask import request
from helpers import GENRES_LIST
from helpers import get_four_songs
from utility import get_preview_url
from helpers import get_score
import billboard
import random
import flask
from flask import session

@app.route('/question')
def question():

    genreChosen = request.args.get("genreChosen")

    if genreChosen == "Current Pop Hits":
        chart = billboard.ChartData('hot-100')
    if genreChosen == "Dance Club Hits":
        chart = billboard.ChartData('dance-club-play-songs')
    if genreChosen == "Country Classics":
        chart = billboard.ChartData('greatest-country-songs')
    if genreChosen == "Hot Latin Songs":
        chart = billboard.ChartData('latin-songs')
    if genreChosen == "Hot R&B/Hip-Hop Songs":
        chart = billboard.ChartData('r-b-hip-hop-songs')


    songList = get_four_songs(chart)
    songRandom = random.randint(0, 3)
    songPreview = songList[songRandom]
    songPreviewTitle = songPreview.title
    songPreviewArtist = songPreview.artist
    dictionary = get_preview_url(songPreviewTitle, songPreviewArtist)

    while "error" in dictionary:
        songRandom = random.randint(0, 3)
        songPreview = songList[songRandom]
        songPreviewTitle = songPreview.title
        songPreviewArtist = songPreview.artist
        dictionary = get_preview_url(songPreviewTitle, songPreviewArtist)

    dictionary = get_preview_url(songPreviewTitle, songPreviewArtist)["url"]

    session['songTitle'] = songPreviewTitle
    session['songArtist'] = songPreviewArtist


    session['num_correct'] = session.get('num_correct')
    session['num_total'] = session.get('num_total')

    mess = get_score()

    session['genre'] = genreChosen

    data = {
        "songs": songList,
    }

    return render_template("question.html", dictionary = dictionary, mess = mess, genreChosen = genreChosen, **data)
