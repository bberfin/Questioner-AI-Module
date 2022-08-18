from glob import glob
import random
# from flask import flash
from flask import request
from flask import Blueprint
from flask import render_template
from flask import redirect, url_for
from website.checkMatch import csv, findMatchedCategoryId, findUserId, printMatch
from website.data import getScore, takeCategories, takeLastNames, takeFirstNames, takeMatches_category, takeMatches_user,  takeQuestions, takeQuestionsAnswer
from website.login import User


intents = Blueprint('intents',__name__)

global first_name
global last_name
global ques
global answers
global dataArr
global score
score=0
first_name=""
last_name=""
dataArr=[]
ques=""
answers=[]

def randomAns(arr):

    newArr=[0,0,0,0]
    op1=random.randint(0,3)
    op2=random.randint(0,3)
    while(op2==op1):
        op2=random.randint(0,3)

    op3=random.randint(0,3)
    while(op3==op1 or op3==op2):
        op3=random.randint(0,3)

    op4=random.randint(0,3)
    while(op4==op1 or op4==op2 or op4==op3):
        op4=random.randint(0,3)
    
    newArr[0]=arr[op1]
    newArr[1]=arr[op2]
    newArr[2]=arr[op3]
    newArr[3]=arr[op4]

    return newArr

def getFirstName():
    global first_name
    return first_name

def getLastName():
    global last_name
    return last_name

# def checkAnswer():
#     global isAnsweredCorrectly
#     return isAnsweredCorrectly   

@intents.route('/home')
def home():
    global score
    name=getFirstName()
    surname=getLastName()    
    userId=findUserId(name,surname)
    categoryId=findMatchedCategoryId(userId)
    score=getScore(userId,categoryId)

    return render_template("home.html",name=name,surname=surname,score=score)

@intents.route('/askedQuestion')
def askQuestion():
    global ques
    global correct_ans
    global answers
    global dataArr
    dataArr=printMatch()
    if(dataArr != False):
        ques= dataArr[0]
        correct_ans=dataArr[1]
        answers=[dataArr[1],dataArr[2],dataArr[3],dataArr[4]]
        answers=randomAns(answers)
        return render_template("askedQuestion.html",theMatch=ques,ans=answers,finish="False")  

    else:
        return render_template("askedQuestion.html",theMatch=ques,ans=answers,finish="True")


@intents.route('/askedQuestion', methods=['GET', 'POST'])
def updateScore():

    global ques
    global correct_ans
    global answers
    global dataArr
    global score
    name=getFirstName()
    surname=getLastName()    
    userId=findUserId(name,surname)
    categoryId=findMatchedCategoryId(userId)

    if request.method == 'POST':
        userAnswer = request.form.get('option')
        correctAnswer=correct_ans
            
        if (userAnswer == correctAnswer):
            csv(dataArr,"1")
            print('TRUE')
        else:
            csv(dataArr,"0")
            print('FALSE')
        
    score=getScore(userId,categoryId)


    dataArr=printMatch()
    if(dataArr != False):
        ques= dataArr[0]
        correct_ans=dataArr[1]
        answers=[dataArr[1],dataArr[2],dataArr[3],dataArr[4]]
        answers=randomAns(answers)
        return render_template("askedQuestion.html",theMatch=ques,ans=answers,finish="False")
    
    else:
        return render_template("askedQuestion.html",theMatch=ques,ans=answers,finish="True")

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


@intents.route('/statistics')
def statistics():
    global score
    return render_template("statistics.html",score=score)  

