
import random
from website import data, intents
from .writeToCsv import writeToCsv


def findUserId(firstName,lastName):

    user_id=-1
    FName=data.takeFirstNames()
    LName=data.takeLastNames()
    userId=data.takeUserId()
    userLen = FName.__len__() 

    for x in range(userLen):
        if(firstName == FName[x] and lastName == LName[x]):
            user_id=userId[x]
    
    return user_id

def findMatchedCategoryId(user_id):

    category_id=-1
    matchedUserId=data.takeMatches_user()
    matchedCategoryId=data.takeMatches_category()
    matchedLen = matchedUserId.__len__()

    for x in range(matchedLen):
        if(user_id == matchedUserId[x]):
            category_id = matchedCategoryId[x]
    
    return category_id

def findQuestion(category_id):

    quesIdArr=[]
    quesId=data.takeQuestionsId()
    ctgryQuesId = data.takeCategoryQuesId()
    quesLen = quesId.__len__()

    for x in range(quesLen):
        if(category_id == ctgryQuesId[x]):
            newArr=[quesId[x]]
            quesIdArr=quesIdArr+newArr
    
    return quesIdArr

def printQuestion(quesIdArr):

    quesArr=[]
    global theQuestion
    global theAnswer
    quesAndAns=[]
    question = data.takeQuestions()
    answer=data.takeQuestionsAnswer()
    quesId=data.takeQuestionsId()
    quesIdLen = quesIdArr.__len__()
    quesLen=question.__len__()

    for x in range(quesIdLen):
        for y in range(quesLen):
            if((quesIdArr[x] == quesId[y]) and (data.isAsked(findUserId(intents.getFirstName(),intents.getLastName()),quesId[y])==False)):
                newArr=[question[y]]
                quesArr=quesArr+newArr
    
    index = random.randint(0,quesArr.__len__()-1)
    while(data.isAsked(findUserId(intents.getFirstName(),intents.getLastName()),data.findQuesId(quesArr[index]))==True):
        index = random.randint(0,quesArr.__len__()-1)
    
    theQuestion= quesArr[index]


    op1=random.randint(0,3)
    op2=random.randint(0,3)
    while(op2==op1):
        op2=random.randint(0,3)

    op3=random.randint(0,3)
    while(op3==op1 | op3==op2):
        op3=random.randint(0,3)

    op4=random.randint(0,3)
    while(op4==op1 | op4==op2 | op4==op3):
        op4=random.randint(0,3)

    for x in range(quesLen):
            if(theQuestion==question[x]):  
                theAnswer=answer[x]
                falseAnswers=data.takeFalseAnswers(x)
                quesAndAns=[theQuestion,theAnswer]
                quesAndAns=quesAndAns+falseAnswers
                break

    return quesAndAns

def printMatch():


    theQuestionId=0

    first_name = intents.getFirstName()
    last_name = intents.getLastName()
    data1 = findUserId(first_name,last_name)
    data2 = findMatchedCategoryId(data1)
    data3 =findQuestion(data2)
    data4 = printQuestion(data3)

   

    question = data.takeQuestions()
    quesId=data.takeQuestionsId()
    quesLen = question.__len__()

    for x in range(quesLen):
        if(data4[0]== question[x]):  
            theQuestionId= quesId[x]

    writeToCsv(data1,theQuestionId)  

    return data4
