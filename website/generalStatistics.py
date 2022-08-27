from website.data import takeAskedQuestionsCategoryId, takeCategories, takeCategoryId


def names():

    categoryNames=takeCategories()
    categoryLen=categoryNames.__len__()

    categoryIds=takeCategoryId()
    trainCategoryId=-1

    askedQuestionsIds=takeAskedQuestionsCategoryId()
    askedLen=askedQuestionsIds.__len__()


    #find the category id of the train category
    for y in range(categoryLen):
        if(str(categoryNames[y]) == "train"):
            trainCategoryId=categoryIds[y]



    # the names of categories ( except "train category")
    # and the number of asked questions for each category
    statisticsArr=[]
    for y in range(categoryLen):
        counter=0
        if(str(categoryNames[y]) != "train"):
 
            for x in range(askedLen):
                if(categoryIds[y]==askedQuestionsIds[x]):
                    counter+=1

            statisticsArr=statisticsArr+[[str(categoryNames[y]),counter]]


    return statisticsArr



