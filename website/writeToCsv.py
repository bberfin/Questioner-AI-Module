
import csv
import pandas as pd

from website import  intents


file_name="csvFiles/askedQuestions.csv"

def writeToCsv (user_id,question_id,category_id,is_correct,sub_category_id):

  with open(file_name,'a', encoding='UTF8', newline='') as writeFile:
      csvwriter=csv.writer(writeFile)
      csvwriter.writerow([user_id,question_id,category_id,is_correct,sub_category_id])

def writeMatchToCsv(user_id,category_id):
  with open("csvFiles\\user_category_match.csv",'a', encoding='UTF8', newline='') as wFile:
      csvwriter=csv.writer(wFile)
      csvwriter.writerow([user_id,category_id]) 
