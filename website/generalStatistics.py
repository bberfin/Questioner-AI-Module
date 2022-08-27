from website.data import takeAskedQuestionsCategoryId, takeAskedQuestionsResult, takeCategories, takeCategoryId, takeMatches_category

def names():

    categoryNames=takeCategories()
    categoryLen=categoryNames.__len__()

    categoryIds=takeCategoryId()

    userCategories=takeMatches_category()
    userCategoryLen=userCategories.__len__()


    statisticsArr=[]
    for y in range(categoryLen):
        counter=0
        for x in range(userCategoryLen):
            if(categoryIds[y]==userCategories[x]):
                counter+=1

        statisticsArr=statisticsArr+[[str(categoryNames[y]),counter]]

    return statisticsArr

def categoryStatistics():

    categoryNames=takeCategories()
    categoryIds=takeCategoryId()
    categoryLen=categoryIds.__len__()

    askedQuestionsIds=takeAskedQuestionsCategoryId()
    asked_data = takeAskedQuestionsResult()
    askedLen=askedQuestionsIds.__len__()


    falseCounter=0
    trueCounter=0
    ctgryArr=[]
    for y in range(categoryLen):
        falseCounter=0
        trueCounter=0
        for x in range(askedLen):
            if(categoryIds[y]==askedQuestionsIds[x]):
                if(str(asked_data[x])=="1"):
                    trueCounter+=1
                else:
                    falseCounter+=1

        
        ctgryArr=ctgryArr+[[str(categoryNames[y]),str(falseCounter),str(trueCounter)]]
    return ctgryArr



