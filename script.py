from datetime import datetime as date
from openLink import openBrowser
today= date.today().strftime("%A")
path="W:\\timetable\\"+today+".txt"
file = open(path,"r")
lines=file.readlines()
for i in range(0,len(lines),3):
    start_time=lines[i].strip()
    end_time=lines[i+1].strip()
    link=lines[i+2].strip()
    openBrowser(start_time,end_time,link)
