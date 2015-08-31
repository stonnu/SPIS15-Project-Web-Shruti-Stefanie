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
    print "fourthQuestion"
    session["indoors or outdoors"]=request.form["indoors or outdoors"]
    return render_template('question4.html')


@app.route('/question5',methods=['get','post'])
def fifthQuestion():
    print "fifthQuestion"
    session["money"]=request.form["money"]
    return render_template('question5.html')

@app.route('/question6',methods=['get','post'])
def sixthQuestion():
    print "sixthQuestion"
    session["active"]=request.form["active"]
    return render_template('question6.html')

def calculateResults():
    '''eventually, this calculates results using values in the session'''
    points = {}
    activities = ["Shopping", "Staying at Home", "Eating",
                  "Adventure", "Active", "Active Alone", "Eating Alone",
                  "Staying Home Alone"]
    for a in activities:
        points[a] = 0
        
    #Question 1
    if session["number in group"]=="1 Person":
        points["Active Alone"] = points["Active Alone"] + 10
        points["Staying Home Alone"] = points["Staying Home Alone"] + 10
        points["Eating Alone"] = points["Eating Alone"] + 10
        points["Shopping"] = points["Shopping"] + 10
    
    if session["number in group"]=="2-6 People":
        points["Eating Alone"] = points["Eating Alone"] + 5
        points["Shopping"] = points["Shopping"] + 10
        points["Eating"] = points["Eating"] + 10
        points["Adventure"] = points["Adventure"] + 10
        points["Active"] = points["Active"] + 10
        points["Staying at Home"] = points["Staying at Home"] + 10
        
    if session["number in group"]=="More than 6 People":
        points["Shopping"] = points["Shopping"] + 5
        points["Eating"] = points["Eating"] + 10
        points["Adventure"] = points["Adventure"] + 10
        points["Active"] = points["Active"] + 10
        points["Staying at Home"] = points["Staying at Home"] + 10

    #Question 2
    if session["hungry"]=="Yes":
        points["Active Alone"] = points["Active Alone"] + 3
        points["Staying Home Alone"] = points["Staying Home Alone"] + 5
        points["Eating Alone"] = points["Eating Alone"] + 8
        points["Shopping"] = points["Shopping"] + 5
        points["Eating"] = points["Eating"] + 8
        points["Adventure"] = points["Adventure"] + 3
        points["Active"] = points["Active"] + 3
        points["Staying at Home"] = points["Staying at Home"] + 5

    if session["hungry"]=="No":
        points["Eating Alone"] = points["Eating Alone"] - 5
        points["Eating"] = points["Eating"] - 5

    #Question 3
    if session["indoors or outdoors"]=="Indoors":
        points["Staying Home Alone"] = points["Staying Home Alone"] + 8
        points["Eating Alone"] = points["Eating Alone"] + 3
        points["Shopping"] = points["Shopping"] + 5
        points["Eating"] = points["Eating"] + 3
        points["Staying at Home"] = points["Staying at Home"] + 8

    if session["indoors or outdoors"]=="Outdoors":
        points["Active Alone"] = points["Active Alone"] + 8
        points["Shopping"] = points["Shopping"] + 5
        points["Eating"] = points["Eating"] + 2
        points["Adventure"] = points["Adventure"] + 8
        points["Active"] = points["Active"] + 8

    #Question 4
    if session["money"]=="None":
        points["Active Alone"] = points["Active Alone"] + 6
        points["Staying Home Alone"] = points["Staying Home Alone"] + 8
        points["Eating Alone"] = points["Eating Alone"] + 5
        points["Active"] = points["Active"] + 6
        points["Staying at Home"] = points["Staying at Home"] + 8

    if session["money"]=="Under $10":
        points["Active Alone"] = points["Active Alone"] + 8
        points["Staying Home Alone"] = points["Staying Home Alone"] + 8
        points["Eating Alone"] = points["Eating Alone"] + 8
        points["Shopping"] = points["Shopping"] + 3
        points["Eating"] = points["Eating"] + 8
        points["Active"] = points["Active"] + 8
        points["Staying at Home"] = points["Staying at Home"] + 8

    if session["money"]=="$10-$25":
        points["Active Alone"] = points["Active Alone"] + 8
        points["Staying Home Alone"] = points["Staying Home Alone"] + 8
        points["Eating Alone"] = points["Eating Alone"] + 8
        points["Shopping"] = points["Shopping"] + 5
        points["Eating"] = points["Eating"] + 8
        points["Adventure"] = points["Adventure"] + 5
        points["Active"] = points["Active"] + 8
        points["Staying at Home"] = points["Staying at Home"] + 8

    #Question 5
    if session["active"]=="None":
        points["Staying Home Alone"] = points["Staying Home Alone"] + 6
        points["Eating Alone"] = points["Eating Alone"] + 3
        points["Eating"] = points["Eating"] + 3
        points["Staying at Home"] = points["Staying at Home"] + 6

    
        
    sortedActivities = sorted( activities, key=lambda a:points[a], reverse=True) 
    return (sortedActivities, points)


##
##    if session["number in group"]=="2-6 People":
##        points["Active Alone"] = points["Active Alone"] + 
##        points["Staying Home Alone"] = points["Staying Home Alone"] + 
##        points["Eating Alone"] = points["Eating Alone"] + 
##        points["Shopping"] = points["Shopping"] + 
##        points["Eating"] = points["Eating"] + 
##        points["Adventure"] = points["Adventure"] + 
##        points["Active"] = points["Active"] + 
##        points["Staying at Home"] = points["Staying at Home"] + 


@app.route('/results',methods=['get','post'])
def results():
    session["character traits"]=request.form["character traits"]
    (recommendedActivities, points) = calculateResults()
    return render_template('results.html', activities = recommendedActivities, points = points)

@app.route('/eat',methods=['get','post'])
def food():
    return render_template('eat.html')

@app.route('/eatalone',methods=['get','post'])
def eatAlone():
    return render_template('eat_alone.html')

@app.route('/shopping',methods=['get','post'])
def shopping():
    return render_template('shopping.html')

@app.route('/stayinghome',methods=['get','post'])
def stayAtHome():
    return render_template('stayinghome.html')

@app.route('/alonetime',methods=['get','post'])
def aloneTime():
    return render_template('alonetime.html')

@app.route('/active',methods=['get','post'])
def beActive():
    return render_template('active.html')

@app.route('/activealone',methods=['get','post'])
def activeAlone():
    return render_template('active_alone.html')

@app.route('/explore',methods=['get','post'])
def goExplore():
    return render_template('adventure.html')

if __name__ == "__main__":
    app.run(port=5678, debug = True)
