from bs4 import BeautifulSoup
from datetime import datetime as date
import schedule
import requests
import smtplib
page = requests.get("https://github.com/Saicharan67")
soup = BeautifulSoup(page.content, 'html.parser')
def SendMail():
    

    host = "server.smtp.com"
    server = smtplib.SMTP(host)
    FROM = "611848@student.nitandhra.ac.in"
    TO = "mahankalisaicharan@gmail.com"
    MSG = "Subject: Test email python\n\nBody of your message!"
    server.sendmail(FROM, TO, MSG)

    server.quit()
    print ("Email Send")
def EmailStreak():
    Date = date.today()
    Todays_Date= str(Date.year)+'-'+str(Date.month)+'-'+str(Date.day)
    Todays_Streak = soup.find_all('rect',attrs={'data-date':Todays_Date})

    SendMail()
    print(Todays_Streak[0]['data-count'])

schedule.every().day.at("19:00").do(EmailStreak)
while True:
    schedule.run_pending()

