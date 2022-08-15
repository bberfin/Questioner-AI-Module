import imp
import random
from flask import flash
from flask import request
from flask import Blueprint
from flask import render_template
from flask import redirect, url_for
from website import checkMatch
from website.checkMatch import findMatchedCategoryId, findUserId, printMatch
from website.data import takeCategories, takeFalseAnswers, takeLastNames, takeFirstNames, takeMatches_category, takeMatches_user,  takeQuestions, takeQuestionsAnswer
from website.login import User


intents = Blueprint('intents',__name__)

global first_name
global last_name
global score
score=0
first_name=""
last_name=""
global ques
global ans
# global falseAns
global answers

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

@intents.route('/home')
def home():
    global score
    name=getFirstName()
    surname=getLastName()
    return render_template("home.html",name=name,surname=surname,score=score)

@intents.route('/askedQuestion')
def askQuestion():
    global ques
    global correct_ans
    global answers
    # global falseAns
    data=printMatch()
    ques= data[0]
    # falseAns=[data[2],data[3],data[4]]
    correct_ans=data[1]
    answers=[data[1],data[2],data[3],data[4]]
    answers=randomAns(answers)
    # data3=checkMatch.theAnswer
    # data3=(takeQuestionsAnswer())[3]
    # data2= data.__len__() 
    # index=random.randint(0,data2-1)   
    # dataRandom=data[index]
    # return render_template("askedQuestion.html",theMatch=ques,falseAnswers=falseAns,correctAns=ans)
    return render_template("askedQuestion.html",theMatch=ques,ans=answers)

@intents.route('/askedQuestion', methods=['GET', 'POST'])
def updateScore():

    global ques
    global correct_ans
    global answers
    # global falseAns

    if request.method == 'POST':
        userAnswer = request.form.get('option')
        correctAnswer=correct_ans
            
        # print("-----PYTHON-------")
        # print("ques: "+ques)
        # print("user: "+userAnswer)
        # print("correct: "+correctAnswer)
        if (userAnswer == correctAnswer):
            global score
            print('TRUE')
            # flash("TRUE")
            score+=1
        else:
            print('FALSE')
            # flash("FALSE")

    data=printMatch()
    ques= data[0]
    # falseAns=[data[2],data[3],data[4]]
    correct_ans=data[1]
    answers=[data[1],data[2],data[3],data[4]]
    answers=randomAns(answers)
    # return render_template("askedQuestion.html",theMatch=ques,falseAnswers=falseAns,correctAns=ans)
    return render_template("askedQuestion.html",theMatch=ques,ans=answers)

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

# @intents.route('/askedQuestion', methods=['GET', 'POST'])
# def updateScore():

#     data= printMatch()
#     if request.method == 'POST':
#         userAnswer = request.form.get('answer')
#         correctAnswer = checkMatch.theAnswer

#         if (userAnswer == correctAnswer):
#             global score
#             print('TRUE')
#             score+=1
#             # return redirect(url_for('intents.home'))
#         else:
#             print('FALSE')
            
#     return render_template("askedQuestion.html",theMatch=data)

# @intents.route('/askedQuestion', methods=['GET', 'POST'])
# def updateScore():

#     data=printMatch()
#     data1= data[0]
#     data2=takeFalseAnswers(3)


#     if request.method == 'POST':
#         userAnswer = request.form.get('option')
#         correctAnswer=data[1]

#         print("ques: "+data1)
#         print("user: "+userAnswer)
#         print("correct: "+correctAnswer)
#         if (userAnswer == correctAnswer):
#             global score
#             print('TRUE')
#             score+=1
#             # return redirect(url_for('intents.home'))
#         else:
#             print('FALSE')
#     return render_template("askedQuestion.html",theMatch=data1,falseAnswers=data2,correctAns=correctAnswer)


    

