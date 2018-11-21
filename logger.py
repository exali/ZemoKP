import datetime

date_time = str(datetime.datetime.now())

with open('D:\\pythonlog.txt', 'a+') as file:
    file.write("UPALJEN KOMPJUTER : " + date_time + "\n")
