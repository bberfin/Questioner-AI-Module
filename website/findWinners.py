import re
import pandas as pd

global winnerId
winnerId = 0  

def findWinners():

    global winnerId

    ques_counter=0
    totalScore=0
    theArr=[]

    maxScore=0
    index=""
    

    asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")
    askedId=asked_data.get("user_id")
    isCorrect=asked_data.get("is_correct")

    user_data = pd.read_csv("csvFiles\\users.csv")
    user_id = user_data.get("user_id")

    quesLen = askedId.__len__()
    userLen = user_id.__len__()


    for y in range(userLen):
        for x in range(quesLen):
            if(str(user_id[y]) == str(askedId[x])):
                ques_counter = ques_counter +1
                if(str(isCorrect[x])=="1"):
                    totalScore+=1
        if(ques_counter != 0):
            currentScore=totalScore/ques_counter  
            currentScore = round(currentScore,2)        
        else:
            currentScore=0
            
        newArr=[str(currentScore)]    

        if(maxScore<currentScore):
            maxScore=currentScore
            index = y

        theArr=theArr+newArr
        ques_counter=0
        totalScore=0
    
    winnerId = int(user_id[index])

    return theArr

def theWinner():

    global winnerId

    return winnerId

                    

