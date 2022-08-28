from website import data
from website.generalStatistics import names


def sortCategories():
    statisticsArr=names()

    statisticsArr.sort(key=lambda x:x[1],reverse=True) #ikinci sütuna göre sıralıyor

    return statisticsArr

def findUserAskedCategories(user_id):

    user_asked_arr=[]

    category_ids=data.takeCategoryId()
    category_len=category_ids.__len__()
    asked_data=data.takeAskedQuestionsCategoryId()
    asked_user_id=data.takeAskedQuestionsUserId()
    asked_data_len=asked_data.__len__()

    for x in range(category_len):
        for y in range(asked_data_len):
            if(str(asked_user_id[y])==str(user_id)):
                if(str(asked_data[y])==str(category_ids[x])):
                    user_asked_arr=user_asked_arr+[str(category_ids[x])]
                    break
    

    user_asked_len=user_asked_arr.__len__()   

    sorted_categories=sortCategories()
    sorted_categories_len=sorted_categories.__len__()



    flag=False
    for x in range(sorted_categories_len):
        flag=False
        for y in range(user_asked_len):
            if(str(user_asked_arr[y]) == str(data.findCategory_id(str(sorted_categories[x][0])))):
                flag=True
        if(flag==False):
            if(str(sorted_categories[x][0]) != "train"):
                changeToMostUsedCategory(user_id,str(data.findCategory_id(str(sorted_categories[x][0]))))
                return True               
    
    return False

def changeToMostUsedCategory(user_id,category_id):

# find current user category id
    user_ids=data.takeMatches_user()
    user_ctgrys=data.takeMatches_category()
    usersLen=user_ids.__len__()
    user_category_id=""
    for x in range(usersLen):
        if(str(user_id)==str(user_ids[x])):
            user_category_id=str(user_ctgrys[x])

#are all questions of that category asked?
  #find the number of questions of that category:
    quesCounter=0
    questions=data.takeCategoryQuesId()
    quesLen=questions.__len__()
    for x in range(quesLen):
        if(str(questions[x])==str(user_category_id)):
            quesCounter+=1
  #find the number of asked questions of that category by the user:
    askedCounter=0
    askedQuestions=data.takeAskedQuestionsCategoryId()
    askedQuestionsUserId=data.takeAskedQuestionsUserId()
    askedQuesLen=askedQuestions.__len__()
    for x in range(askedQuesLen):
        if(str(user_id)==str(askedQuestionsUserId[x])):
            if(str(user_category_id)==str(askedQuestions[x])):
                askedCounter+=1
   #change the category:
    if(askedCounter==quesCounter):
        data.changeCategory(user_id,category_id)





    # print("all questions: "+str(quesCounter))
    # print("answered questions: "+str(askedCounter))

# data.changeCategory(user_id,category_id)

