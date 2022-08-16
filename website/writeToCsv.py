
import csv
import pandas as pd

from .data import checkAsked

file_name="csvFiles/askedQuestions.csv"
# asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")

def writeToCsv (user_id,question_id):

  with open(file_name,'a', encoding='UTF8', newline='') as writeFile:
      csvwriter=csv.writer(writeFile)
      if(checkAsked(user_id)==False):
        # print("user is NOT here")
        csvwriter.writerow([user_id,question_id])
      else:
        # print("user is here")
        csvwriter.writerow([user_id,question_id])

# def writeToCsv (user_id,question_id):
#   askedId=asked_data.get("user_id")
#   askedQues=asked_data.get("question_id")
#   askedIdLen = askedId.__len__()
#   with open(file_name,'r') as readFile, open(file_name,'a', encoding='UTF8', newline='') as writeFile:
#       csvwriter=csv.writer(writeFile)
#       if(checkAsked(user_id)==False):
#         print("user is NOT here")
#         csvwriter.writerow([user_id,question_id])
#       else:
#         print("user is here")
#         for row in csv.reader(readFile):
#           if (str(row[0])==str(user_id)):
#               df=asked_data.drop(asked_data[asked_data.get("user_id") == int(row[0])].index,axis=0,inplace=True)

#   print(asked_data.get("user_id"))
#   print(df)

