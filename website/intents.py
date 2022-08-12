from glob import glob
import random
from tkinter import scrolledtext
from flask import request
from flask import Blueprint
from flask import render_template
from flask import redirect, url_for
from website import checkMatch
from website.checkMatch import findMatchedCategoryId, findUserId, printMatch
from website.data import takeCategories, takeLastNames, takeFirstNames, takeMatches_category, takeMatches_user,  takeQuestions
from website.login import User


intents = Blueprint('intents',__name__)

global first_name
global last_name
global score
score=0
first_name=""
last_name=""

def getFirstName():
    global first_name
    return first_name

def getLastName():
    global last_name
    return last_name

@intents.route('/home')
def home():
    global score
    name=getFirstName()
    surname=getLastName()
    return render_template("home.html",name=name,surname=surname,score=score)

@intents.route('/askedQuestion')
def askQuestion():
    data= printMatch()
    # data2= data.__len__() 
    # index=random.randint(0,data2-1)   
    # dataRandom=data[index]
    return render_template("askedQuestion.html",theMatch=data)

@intents.route('/username')
def username():
    data = takeFirstNames()
    data2 =takeLastNames()
    return render_template("users.html", user_names=data, user_last_names=data2, user_names_len=data.__len__())

@intents.route('/category')
def category():
    data = takeCategories()
    return render_template("categories.html", category_names=data, category_names_len=data.__len__())

@intents.route('/question')
def question():
    data = takeQuestions()
    return render_template("questions.html", question_names=data, question_names_len=data.__len__())

@intents.route('/match')
def match():
    data1 = takeMatches_user()
    data2 = takeMatches_category()
    return render_template("matches.html", match_user_name=data1, match_category_name=data2, match_names_len=data1.__len__())

@intents.route('/', methods=['GET', 'POST'])
def login():

    global first_name
    global last_name

    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')

        isUser = User(first_name, last_name)

        if isUser:
            print('LOGGED SUCCESSFULLY')
            return redirect(url_for('intents.home'))
        else:
            print('TRY AGAIN')
            
    return render_template("login.html")

@intents.route('/askedQuestion', methods=['GET', 'POST'])
def updateScore():

    data= printMatch()
    if request.method == 'POST':
        userAnswer = request.form.get('answer')
        correctAnswer = checkMatch.theAnswer

        if (userAnswer == correctAnswer):
            global score
            print('TRUE')
            score+=1
            # return redirect(url_for('intents.home'))
        else:
            print('FALSE')
            
    return render_template("askedQuestion.html",theMatch=data)


    

