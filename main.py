import os
from flask import Flask, url_for, render_template, request
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/question1')
def firstQuestion():
    return render_template('question1.html')


@app.route('/question2')
def secondQuestion():
    return render_template('question2.html')


@app.route('/question3')
def thirdQuestion():
    return render_template('question3.html')


@app.route('/question4')
def fourthQuestion():
    return render_template('question4.html')


@app.route('/question5')
def fifthQuestion():
    return render_template('question5.html')


if __name__ == "__main__":
    app.run(port=5006, debug = False)
