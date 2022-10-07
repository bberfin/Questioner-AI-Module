from flask import flash
import random
# from flask import flash
from flask import request
from flask import Blueprint
from flask import render_template
from flask import redirect, url_for
from website.checkMatch import csv, findMatchedCategoryId, findUserId, printMatch
from website.data import findAnswersPercentages, findQuesId, getScore, show_all_statistics, takeCategories, takeLastNames, takeFirstNames, takeMatches_category, takeMatches_user,  takeQuestions, takeScore_subCategories
from website.findWinners import findWinners, theWinner
from website.generalStatistics import categoryStatistics, names
from website.login import User


intents = Blueprint('intents',__name__)

global first_name
global last_name
global ques
global answers
global dataArr
global score
global correct_ans
global ans_prctng
ans_prctng=0
correct_ans=""
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
    global ans_prctng
    dataArr=printMatch()
    if(dataArr != False):
        ques= dataArr[0]
        ques_id=findQuesId(str(ques))
        ans_prctng=findAnswersPercentages(str(ques_id))
        correct_ans=dataArr[1]
        answers=[dataArr[1],dataArr[2],dataArr[3],dataArr[4]]
        answers=randomAns(answers)
        return render_template("askedQuestion.html",theMatch=ques,ans=answers,finish="False",cAns=correct_ans,answers_percentage=ans_prctng)  

    else:
        return render_template("askedQuestion.html",theMatch=ques,ans=answers,finish="True",cAns=correct_ans,answers_percentage=ans_prctng)


@intents.route('/askedQuestion', methods=['GET', 'POST'])
def updateScore():

    global ques
    global correct_ans
    global answers
    global dataArr
    global score
    global ans_prctng
    name=getFirstName()
    surname=getLastName()    
    userId=findUserId(name,surname)
    categoryId=findMatchedCategoryId(userId)

    if request.method == 'POST':
        userAnswer = request.form.get('option')
        correctAnswer=correct_ans
            
        if (userAnswer == correctAnswer):
            csv(dataArr,"1")
            # print('TRUE')
        else:
            csv(dataArr,"0")
            # print('FALSE')
        
    score=getScore(userId,categoryId)


    dataArr=printMatch()
    if(dataArr != False):
        ques= dataArr[0]
        ques_id=findQuesId(str(ques))
        ans_prctng=findAnswersPercentages(str(ques_id))
        correct_ans=dataArr[1]
        answers=[dataArr[1],dataArr[2],dataArr[3],dataArr[4]]
        answers=randomAns(answers)
        return render_template("askedQuestion.html",theMatch=ques,ans=answers,finish="False",cAns=correct_ans,answers_percentage=ans_prctng)
    
    else:
        return render_template("askedQuestion.html",theMatch=ques,ans=answers,finish="True",cAns=correct_ans,answers_percentage=ans_prctng)

@intents.route('/username')
def username():

    global score
    name=getFirstName()
    surname=getLastName()    
    userId=findUserId(name,surname)
    categoryId=findMatchedCategoryId(userId)
    score=getScore(userId,categoryId)

    arr = findWinners()
    winnerId = theWinner()

    data = takeFirstNames()
    data2 =takeLastNames()
    return render_template("users.html", user_names=data, user_last_names=data2, user_names_len=data.__len__(),arr=arr,winnerId=winnerId)

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
        password = request.form.get('password')

        isUser = User(first_name, last_name, password)

        if isUser:
            print('LOGGED SUCCESSFULLY')
            return redirect(url_for('intents.home'))
        else:
            print('TRY AGAIN')
            
    return render_template("login.html")


@intents.route('/statistics')
def statistics():

    name=getFirstName()
    surname=getLastName()    
    userId=findUserId(name,surname)
    allStatistics=show_all_statistics(userId)
    allStatistics_len=allStatistics.__len__()

    global score
    sub_score=takeScore_subCategories()
    sub_score_len=sub_score.__len__()
    return render_template("statistics.html",score=score,subScore=sub_score,subScore_len=sub_score_len,allStatistics=allStatistics,allStatistics_len=allStatistics_len)  

@intents.route('/generalStatistics')
def generalStatistics():
    arr=names() 
    arrLen=arr.__len__()   
    ctgryArr=categoryStatistics()
    ctgryLen=ctgryArr.__len__()
    return render_template("generalStatistics.html",DATA=arr,DATALEN=arrLen,CTGRY=ctgryArr,CTGRYLEN=ctgryLen)

@intents.route('/signup')
def signup():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        
        nameF = User.query.filter_by(first_name=first_name).first()
        nameL = User.query.filter_by(last_name=last_name).first()

        if nameF and nameL:
            flash('The User already exists.', category='error')
        else:
            new_user = User(first_name=first_name,last_name=last_name )
            return redirect(url_for('views.home'))
    return render_template("signup.html")

