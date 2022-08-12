
import csv

file_name="csvFiles/askedQuestions.csv"

def writeToCsv (user_id,question_id):
  with open(file_name,'a', encoding='UTF8', newline='') as csvfile:
      csvwriter=csv.writer(csvfile)
      csvwriter.writerow([user_id,question_id])