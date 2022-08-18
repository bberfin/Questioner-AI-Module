import pandas as pd

# user_data = pd.read_csv("csvFiles\\users.csv")  #read_csv : virgülle ayrılmış veri tabloları için
# category_data = pd.read_csv("csvFiles\\categories.csv") 
# question_data = pd.read_csv("csvFiles\\questions.csv") 
# match_data = pd.read_csv("csvFiles\\user_category_match.csv")
# asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")

global askedNum
askedNum=0

def takeFirstNames():
    user_data = pd.read_csv("csvFiles\\users.csv")
    user_names = user_data.get("user_first_name")   
    return user_names

def takeLastNames():
    user_data = pd.read_csv("csvFiles\\users.csv")
    user_last_names = user_data.get("user_last_name")
    return user_last_names


def takeUserId():
    user_data = pd.read_csv("csvFiles\\users.csv")
    user_id = user_data.get("user_id")
    return user_id

def takeCategories():
    category_data = pd.read_csv("csvFiles\\categories.csv") 
    category_names = category_data.get("category_name")

    return category_names

def takeCategoryId():
    category_data = pd.read_csv("csvFiles\\categories.csv") 
    category_id = category_data.get("category_id")
    return category_id

def takeQuestions():
    question_data = pd.read_csv("csvFiles\\questions.csv") 
    question_names = question_data.get("question")
    return question_names

def takeQuestionsId():
    question_data = pd.read_csv("csvFiles\\questions.csv") 
    question_id = question_data.get("question_id")
    return question_id

def takeQuestionsAnswer():
    question_data = pd.read_csv("csvFiles\\questions.csv") 
    question_answer = question_data.get("question_answer")
    return question_answer

def takeFalseAnswers(x):
    question_data = pd.read_csv("csvFiles\\questions.csv") 
    data1=(question_data.get("option2"))[x]
    data2=(question_data.get("option3"))[x]
    data3=(question_data.get("option4"))[x]
    falseAnswers = [data1,data2,data3]
    return falseAnswers

def takeCategoryQuesId():
    question_data = pd.read_csv("csvFiles\\questions.csv") 
    ctgry_id = question_data.get("category_id")
    return ctgry_id

def takeMatches_user():
    match_data = pd.read_csv("csvFiles\\user_category_match.csv")
    match_user = match_data.get("user_id")
    return match_user

def takeMatches_category():
    match_data = pd.read_csv("csvFiles\\user_category_match.csv")
    match_category = match_data.get("category_id")
    return match_category

def getScore(user_id,category_id):
    counter=0
    categoryName=""
    scoreArr=[]
    asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")
    askedId=asked_data.get("user_id")
    categoryId=asked_data.get("category_id")
    isCorrect=asked_data.get("is_correct")
    quesLen = askedId.__len__()

    categoryNames=takeCategories()
    categoryIds=takeCategoryId()
    categoryLen=categoryIds.__len__()

    for x in range(quesLen):
        if((str(user_id)==str(askedId[x])) and (str(category_id)==str(categoryId[x]))):
            if(str(isCorrect[x])=="1"):
                counter+=1 
    
    tempArr=[counter]

    for y in range(categoryLen):
        if(str(category_id)==str(categoryIds[y])):
            categoryName=categoryNames[y]

    tempArr2=[categoryName]
    tempArr=tempArr+tempArr2
    
    scoreArr=scoreArr+tempArr

    return scoreArr


# def findUserId(firstname,lastname):
#     user_data = pd.read_csv("csvFiles\\users.csv")
#     user_Fnames = user_data.get("user_first_name")
#     user_Lnames = user_data.get("user_last_name")    
#     userLen=user_Fnames.__len__()

#     userIds=takeUserId()
#     for x in range(userLen):
#         if((str(firstname)==str(user_Fnames[x])) and (str(lastname)==str(user_Lnames[x]))):
#             return userIds[x]


def isAsked(user_id,question_id):
    asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")
    askedId=asked_data.get("user_id")
    askedIdLen = askedId.__len__()
    askedQuesId=asked_data.get("question_id")
    flag=False
    for x in range(askedIdLen):
        if(user_id==askedId[x]):
            if(str(question_id)==str(askedQuesId[x])):
                flag=True
                break

    return  flag

def findQuesId(question):
    ques=takeQuestions()
    quesLen=ques.__len__()
    quesIds=takeQuestionsId()
    for x in range(quesLen):
        if(str(question)==str(ques[x])):
            return quesIds[x]

def findAskedQuesNum(user_id):
    global askedNum
    asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")
    askedId=asked_data.get("user_id")
    askedIdLen = askedId.__len__()
    for x in range(askedIdLen):
        if(user_id==askedId[x]):
            askedNum=askedNum+1
    num = askedNum
    askedNum=0
    return num

def checkAsked(user_id):
    asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")
    askedId=asked_data.get("user_id")
    askedIdLen = askedId.__len__()
    flag=False 
    for x in range(askedIdLen):
        if(user_id==askedId[x]):
            flag=True
            break
        
    return  flag
