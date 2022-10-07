from website import data


def checkNames(first_name, last_name, password):

    FName=data.takeFirstNames()
    LName=data.takeLastNames()
    userPassword = data.takePasswords()
    userLen = FName.__len__() 
    flag = False

    for x in range(userLen):
        if(first_name == FName[x]):
            if(last_name == LName[x]):
                if(password == userPassword[x]):
                    flag=True
    
    return flag

def User(first_name, last_name, password):
    isUser = checkNames(first_name, last_name, password)
    
    return isUser
