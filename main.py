import os
from flask import Flask, url_for, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key='asdfghjkl123456789';


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/question1')
def firstQuestion():
    return render_template('question1.html')


@app.route('/question2',methods=['get','post'])
def secondQuestion():
    session["number in group"]=request.form["number in group"]
    return render_template('question2.html')


@app.route('/question3',methods=['get','post'])
def thirdQuestion():
    session["hungry"]=request.form["hungry"]
    return render_template('question3.html')


@app.route('/question4',methods=['get','post'])
def fourthQuestion():
    session["indoors or outdoors"]=request.form["indoors or outdoors"]
    return render_template('question4.html')


@app.route('/question5',methods=['get','post'])
def fifthQuestion():
    session["money"]=request.form["money"]
    return render_template('question5.html')

@app.route('/question6',methods=['get','post'])
def sixthQuestion():
    session["active"]=request.form["active"]
    return render_template('question6.html')

@app.route('/eat',methods=['get','post'])
def food():
    return render_template('eat.html')

@app.route('/shopping',methods=['get','post'])
def shopping():
    return render_template('shopping.html')

@app.route('/stayinghome',methods=['get','post'])
def stayAtHome():
    return render_template('stayinghome.html')

@app.route('/active',methods=['get','post'])
def beActive():
    return render_template('active.html')

@app.route('/explore',methods=['get','post'])
def goExplore():
    return render_template('adventure.html')

if __name__ == "__main__":
    app.run(port=5006, debug = False)
