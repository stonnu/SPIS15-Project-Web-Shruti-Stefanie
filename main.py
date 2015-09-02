import os
from flask import Flask, url_for, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key='asdfghjkl123456789';


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('home'))

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

shopping = "Shopping"
adventure = "Exploring"
exercise = "Exercising"
cook = "Cooking"
active = "Being Active"

activities = [shopping, "Staying at Home", "Eating",
              adventure, active, exercise, cook,
              "Staying Home"]

activity_urls = {shopping:"/shopping",
                 "Staying at Home":"/stayinghome",
                 "Eating":"/eat",
                 adventure:"/explore",
                 active:"/active",
                 exercise:"/activealone",
                 cook:"/eatalone",
                 "Staying Home":"/alonetime"}

def calculateResults():
    '''this calculates results using values in the session'''
    points = {}
    shopping = "Shopping"
    adventure = "Exploring"
    exercise = "Exercising"
    cook = "Cooking"
    active = "Being Active"

    activities = [shopping, "Staying at Home", "Eating",
              adventure, active, exercise, cook,
              "Staying Home"]
    
    for a in activities:
        points[a] = 0
        
    #Question 1
    if session["number in group"]=="1 Person":
        points[exercise] = points[exercise] + 20
        points["Staying Home"] = points["Staying Home"] + 20
        points[cook] = points[cook] + 20
        points[shopping] = points[shopping] + 20
    
    if session["number in group"]=="2-6 People":
        points[cook] = points[cook] + 10
        points[shopping] = points[shopping] + 20
        points["Eating"] = points["Eating"] + 20
        points[adventure] = points[adventure] + 20
        points[active] = points[active] + 20
        points["Staying at Home"] = points["Staying at Home"] + 20
        
    if session["number in group"]=="More than 6 People":
        points[shopping] = points[shopping] + 10
        points["Eating"] = points["Eating"] + 20
        points[adventure] = points[adventure] + 20
        points[active] = points[active] + 20
        points["Staying at Home"] = points["Staying at Home"] + 20

    #Question 2
    if session["hungry"]=="Yes":
        points[exercise] = points[exercise] + 3
        points["Staying Home"] = points["Staying Home"] + 5
        points[cook] = points[cook] + 8
        points[shopping] = points[shopping] + 5
        points["Eating"] = points["Eating"] + 8
        points[adventure] = points[adventure] + 3
        points[active] = points[active] + 3
        points["Staying at Home"] = points["Staying at Home"] + 5

    if session["hungry"]=="No":
        points[cook] = points[cook] - 5
        points["Eating"] = points["Eating"] - 5

    #Question 3
    if session["indoors or outdoors"]=="Indoors":
        points["Staying Home"] = points["Staying Home"] + 8
        points[cook] = points[cook] + 3
        points[shopping] = points[shopping] + 5
        points["Eating"] = points["Eating"] + 3
        points["Staying at Home"] = points["Staying at Home"] + 8

    if session["indoors or outdoors"]=="Outdoors":
        points[exercise] = points[exercise] + 8
        points[shopping] = points[shopping] + 5
        points["Eating"] = points["Eating"] + 2
        points[adventure] = points[adventure] + 8
        points[active] = points[active] + 8

    #Question 4
    if session["money"]=="None":
        points[exercise] = points[exercise] + 6
        points["Staying Home"] = points["Staying Home"] + 8
        points[cook] = points[cook] + 5
        points[active] = points[active] + 6
        points["Staying at Home"] = points["Staying at Home"] + 8

    if session["money"]=="Under $10":
        points[exercise] = points[exercise] + 8
        points["Staying Home"] = points["Staying Home"] + 8
        points[cook] = points[cook] + 8
        points[shopping] = points[shopping] + 3
        points["Eating"] = points["Eating"] + 8
        points[active] = points[active] + 8
        points["Staying at Home"] = points["Staying at Home"] + 8

    if session["money"]=="$10-$25":
        points[exercise] = points[exercise] + 8
        points["Staying Home"] = points["Staying Home"] + 8
        points[cook] = points[cook] + 8
        points[shopping] = points[shopping] + 5
        points["Eating"] = points["Eating"] + 8
        points[adventure] = points[adventure] + 5
        points[active] = points[active] + 8
        points["Staying at Home"] = points["Staying at Home"] + 8

    #Question 5
    if session["active"]=="None":
        points["Staying Home"] = points["Staying Home"] + 6
        points[cook] = points[cook] + 3
        points["Eating"] = points["Eating"] + 3
        points["Staying at Home"] = points["Staying at Home"] + 6

    if session["active"]=="Little":
        points["Staying Home"] = points["Staying Home"] + 6
        points[cook] = points[cook] + 6
        points[shopping] = points[shopping] + 3
        points["Eating"] = points["Eating"] + 6
        points["Staying at Home"] = points["Staying at Home"] + 6

    if session["active"]=="Lot":
        points[exercise] = points[exercise] + 6
        points["Staying Home"] = points["Staying Home"] + 3
        points[cook] = points[cook] + 6
        points[shopping] = points[shopping] + 6
        points["Eating"] = points["Eating"] + 6
        points[active] = points[active] + 6
        points["Staying at Home"] = points["Staying at Home"] + 3

    if session["active"]=="You are crazy":
        points[exercise] = points[exercise] + 6
        points[cook] = points[cook] + 6
        points[shopping] = points[shopping] + 6
        points["Eating"] = points["Eating"] + 6
        points[adventure] = points[adventure] + 6
        points[active] = points[active] + 6

    #Question 6
    if session["character traits"]=="Active":
        points[exercise] = points[exercise] + 5
        points[adventure] = points[adventure] + 3
        points[active] = points[active] + 3

    if session["character traits"]=="Calm":
        points["Staying Home"] = points["Staying Home"] + 5
        points["Staying at Home"] = points["Staying at Home"] + 5

    if session["character traits"]=="Foodie":
        points[cook] = points[cook] + 5
        points["Eating"] = points["Eating"] + 5

    if session["character traits"]=="Spontaneous":
        points[adventure] = points[adventure] + 5

    if session["character traits"]=="Creative":
        points["Staying Home"] = points["Staying Home"] + 3
        points[cook] = points[cook] + 5
        points["Staying at Home"] = points["Staying at Home"] + 3

    if session["character traits"]=="Children at Heart":
        points["Staying Home"] = points["Staying Home"] + 5
        points[active] = points[active] + 3
        points["Staying at Home"] = points["Staying at Home"] + 5

    if session["character traits"]=="Competitive":
        points[active] = points[active] + 5
        points["Staying at Home"] = points["Staying at Home"] + 3

    if session["character traits"]=="Trendy":
        points[shopping] = points[shopping] + 5

        
    sortedActivities = sorted(activities, key=lambda a:points[a], reverse=True) 
    return (sortedActivities, points)


@app.route('/results',methods=['get','post'])
def results():
    session["character traits"]=request.form["character traits"]
    (recommendedActivities, points) = calculateResults()
    return render_template('results.html', activities = recommendedActivities,
                           points = points, activity_urls = activity_urls)

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
