from flask import Blueprint
from flask import render_template
from website.checkMatch import printMatch
from website.data import takeCategories, takeLastNames, takeFirstNames, takeMatches_category, takeMatches_user,  takeQuestions


intents = Blueprint('intents',__name__)

@intents.route('/')
def home():
    data= printMatch()
    data2= data.__len__()
    return render_template("home.html",theMatch=data,matched_ques_len=data2)

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