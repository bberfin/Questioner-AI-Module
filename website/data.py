import math
import pandas as pd
from website import checkMatch
from website import intents 

from website.writeToCsv import writeMatchToCsv

# user_data = pd.read_csv("csvFiles\\users.csv")  #read_csv : virgülle ayrılmış veri tabloları için
# category_data = pd.read_csv("csvFiles\\categories.csv") 
# question_data = pd.read_csv("csvFiles\\questions.csv") 
# match_data = pd.read_csv("csvFiles\\user_category_match.csv")
# asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")

global askedNum
askedNum=0

global temp
temp=[]

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

def takeAskedQuestionsUserId():
    question_data = pd.read_csv("csvFiles\\askedQuestions.csv") 
    user_id = question_data.get("user_id")
    return user_id

def takeAskedQuestionsCategoryId():
    question_data = pd.read_csv("csvFiles\\askedQuestions.csv") 
    category_id = question_data.get("category_id")
    return category_id

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

def take_sub_category(ques_id):
    ques_data = pd.read_csv("csvFiles\\questions.csv")
    ques_idS = takeQuestionsId()
    sub_ctgry = ques_data.get("sub_category_id")   
    quesLen=ques_data.__len__()
    sub_ctgry_id=-1

    for x in range(quesLen):
        if(str(ques_id)==str(ques_idS[x])):
            sub_ctgry_id=sub_ctgry[x]

    if math.isnan(sub_ctgry_id):
        return ""
    else:
        return int(sub_ctgry_id)

def getScore(user_id,category_id):
    counter=0
    ques_counter=0
    trainCategoryId=-1
    categoryName=""
    scoreArr=[]
    subCtgryArr=[]
    asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")
    askedId=asked_data.get("user_id")
    categoryId=asked_data.get("category_id")
    subCategoryId=asked_data.get("sub_category_id")
    isCorrect=asked_data.get("is_correct")
    quesLen = askedId.__len__()

    categoryNames=takeCategories()
    categoryIds=takeCategoryId()
    categoryLen=categoryIds.__len__()

    for y in range(categoryLen):
        if(str(categoryNames[y]) == "train"):
            trainCategoryId=categoryIds[y]

    # if (str(category_id)==str(trainCategoryId)):
    #     for y in range(quesLen):
    #         if((str(user_id)==str(askedId[y])) and (str(category_id)==str(categoryId[y]))):
    #             newArr=[int(subCategoryId[y])]
    #             subCtgryArr=subCtgryArr+newArr
        
    #     findSubCategoryScore(subCtgryArr,subCtgryArr.__len__())



    for x in range(quesLen):
        if((str(user_id)==str(askedId[x])) and (str(category_id)==str(categoryId[x]))):
            ques_counter+=1
            if(str(isCorrect[x])=="1"):
                counter+=1 
            if (str(category_id)==str(trainCategoryId)):
                newArr=[[int(subCategoryId[x]),str(isCorrect[x])]]
                subCtgryArr=subCtgryArr+newArr
                
   
    findSubCategoryScore(subCtgryArr,subCtgryArr.__len__())               

    
    tempArr=[counter]

    for y in range(categoryLen):
        if(str(category_id)==str(categoryIds[y])):
            categoryName=categoryNames[y]

    tempArr2=[categoryName]
    tempArr=tempArr+tempArr2

    tempArr3=[ques_counter]
    tempArr=tempArr+tempArr3
    
    scoreArr=scoreArr+tempArr


    return scoreArr

def findSubCategoryScore(subCtgryArr,arrLen):
    tempArr=[]
    counter=0
    sub_counter=0
    # for x in range(arrLen):
    #     print(str(subCtgryArr[x][0])+":"+str(subCtgryArr[x][1]))

    for x in range(arrLen):
        for y in range(arrLen):
            if(str(subCtgryArr[x][0]) == str(subCtgryArr[y][0])):
                counter+=1
                if(str(subCtgryArr[y][1])=="1"):
                    sub_counter+=1
                # print(str(subCtgryArr[x][0])+"-"+str(subCtgryArr[y][0]))
        # print(str(subCtgryArr[x][0])+":")
        # print(str(findCategoryName(subCtgryArr[x][0]))+str(counter))

        newArr=[[findCategoryName(subCtgryArr[x][0]),str(counter),str(sub_counter)]]
        tempArr=tempArr+newArr
        sub_counter=0
        # print(findCategoryName(subCtgryArr[x][0])+": "+str(tmp))
        counter=0

    global temp
    xArr=[]
    temp=xArr
    percentage=0
    categories=takeCategories()
    categoryIDs=takeCategoryId()
    lenn=categoryIDs.__len__()
    lennArr=tempArr.__len__()
    for z in range(lenn):
        for y in range(lennArr):
            if(str(categories[z]) == str(tempArr[y][0])):
                # print(str(tempArr[y][0])+": "+str(tempArr[y][1]))
                percentage= (int(tempArr[y][2])/int(tempArr[y][1])).__format__(".2")
                newTemp=[[str(tempArr[y][0]),str(tempArr[y][1]),str(tempArr[y][2]),percentage]]
                temp=temp+newTemp
                # findNewCategory(temp,temp.__len__())        
                break 

    name=intents.getFirstName()
    surname=intents.getLastName()    
    userId=checkMatch.findUserId(name,surname)  
    categoryId=checkMatch.findMatchedCategoryId(userId) 

    for y in range(lenn):
        if(str(categories[y]) == "train"):
            trainCategoryId=categoryIDs[y]

    if(str(categoryId)==str(trainCategoryId)):           
        findNewCategory(temp,temp.__len__())        
    # for a in range(temp.__len__()):
    #     print(temp[a][0]+": "+temp[a][1])

def findNewCategory(arr,arrLen):

    trainQuescount=0
    trainID=-1

    categoryNames=takeCategories()
    categoryIDs=takeCategoryId()
    categoryLen=categoryNames.__len__()
    for x in range(categoryLen):
        if("train"==str(categoryNames[x])):
            trainID=categoryIDs[x]
    
    questions=takeCategoryQuesId()
    questionsLen=questions.__len__()
    for x in range(questionsLen):
        if(str(trainID)==str(questions[x])):
            trainQuescount+=1
    
    flag=0
    # theMax=arr[0][3]
    theMax=0
    for x in range(arrLen):
        if(str(arr[x][3])>str(theMax)):
            theMax=arr[x][3]
            flag=x


    askLen=0
    name=intents.getFirstName()
    surname=intents.getLastName()    
    userId=checkMatch.findUserId(name,surname)
    askedQuestionsCtgry=takeAskedQuestionsCategoryId()
    askedQuestionsUser=takeAskedQuestionsUserId()
    askedQuestionsLen=askedQuestionsUser.__len__()
    for x in range(askedQuestionsLen):
        if(str(askedQuestionsCtgry[x])==str(trainID) and (str(userId) == str(askedQuestionsUser[x]))):
            askLen+=1

    # print("new category : "+str(theMax)+"---"+str(arr[flag][0]))
    print("train id :" +str(trainID))
    print("train ques count :" +str(trainQuescount))
    print("asked len : "+str(askLen))  

    # if(trainQuescount == arrLen):
        # print("new category : "+str(theMax)+"---"+str(arr[flag][0]))
        # print("train id :" +str(trainID))
        # print("train ques count :" +str(trainQuescount))
        

def findCategoryName(category_id):
    theName=""
    categoryNames=takeCategories()
    categoryIDs=takeCategoryId()
    ctgryLen=categoryIDs.__len__()

    for x in range(ctgryLen):
        if(str(category_id)==str(categoryIDs[x])):
            theName=categoryNames[x]
    
    return theName

def changeCategory(user_id,category_id):

    file_name="csvFiles\\user_category_match.csv"
    data = pd.read_csv(file_name)  

    data.drop(data[data['user_id']== user_id].index, inplace=True, axis=0)
    newData=data

    file=open(file_name,'w')
    file.truncate()
    file.close()

    newData.to_csv(file_name,mode='w',index=None)
    writeMatchToCsv(user_id,category_id)

def isAsked(user_id,question_id):
    asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")
    askedId=asked_data.get("user_id")
    askedQuesId=asked_data.get("question_id")
    askedIdLen = askedQuesId.__len__()
    flag=False
    for x in range(askedIdLen):
        if((user_id)==askedId[x]) and (question_id==askedQuesId[x]):
            # print("soruldu")
            flag=True

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

def takeScore_subCategories():
    global temp
    return temp
