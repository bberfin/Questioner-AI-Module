
import csv
import pandas as pd

from website import  intents


file_name="csvFiles/askedQuestions.csv"
# asked_data = pd.read_csv("csvFiles\\askedQuestions.csv")

def writeToCsv (user_id,question_id,category_id,is_correct):

  with open(file_name,'a', encoding='UTF8', newline='') as writeFile:
      csvwriter=csv.writer(writeFile)
      csvwriter.writerow([user_id,question_id,category_id,is_correct])


      # if(checkAsked(user_id)==False):
      #   # print("user is NOT here")
      #   csvwriter.writerow([user_id,question_id,category_id,is_correct])
      # else:
      #   # print("user is here")
      #   csvwriter.writerow([user_id,question_id,category_id,is_correct])