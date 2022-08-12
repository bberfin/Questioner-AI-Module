import pandas as pd

user_data = pd.read_csv("csvFiles\\users.csv")  #read_csv : virgülle ayrılmış veri tabloları için
category_data = pd.read_csv("csvFiles\\categories.csv") 
question_data = pd.read_csv("csvFiles\\questions.csv") 
match_data = pd.read_csv("csvFiles\\user_category_match.csv")


def takeFirstNames():
    user_names = user_data.get("user_first_name")
    
    return user_names

def takeLastNames():
    user_last_names = user_data.get("user_last_name")
    return user_last_names


def takeUserId():
    user_id = user_data.get("user_id")
    return user_id

def takeCategories():
    category_names = category_data.get("category_name")

    return category_names

def takeCategoryId():
    category_id = category_data.get("category_id")

    return category_id

def takeQuestions():
    question_names = question_data.get("question")

    return question_names

def takeQuestionsId():
    question_names = question_data.get("question_id")

    return question_names

def takeQuestionsAnswer():
    question_answer = question_data.get("question_answer")

    return question_answer

def takeCategoryQuesId():
    ctgry_id = question_data.get("category_id")

    return ctgry_id

def takeMatches_user():
    match_user = match_data.get("user_id")

    return match_user

def takeMatches_category():
    match_category = match_data.get("category_id")

    return match_category



