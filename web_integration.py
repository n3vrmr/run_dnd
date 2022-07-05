# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 13:37:31 2022

@author: Nevermore
"""

from campaign import Campaign
from flask import Flask, render_template, request
from player_character import Character, Player

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('init_index.html')

@app.route("/games", methods=['GET', 'POST'])
def games():
    if request.method == 'POST':
        name=request.form['Player name']
        char_name=request.form['Character name']
        level=request.form['Character level']
        race=request.form['Race']
        classe=request.form['Class']
        skills=request.form['Skills']
        char = Character(name, char_name, level, race, classe, skills)
        return render_template('character.html',char=char)
    return render_template('game.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')