from website import data


def checkNames(first_name, last_name):

    FName=data.takeFirstNames()
    LName=data.takeLastNames()
    userLen = FName.__len__() 
    flag = False

    for x in range(userLen):
        if(first_name == FName[x]):
            if(last_name == LName[x]):
                flag=True
    
    return flag

def User(first_name, last_name):
    isUser = checkNames(first_name, last_name)
    
    return isUser
