import csv
filename = "csvFiles/askedQuestions.csv"
fields=['user_id','question_id','isTrue']

with open(filename,'a') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['4','1','1'])