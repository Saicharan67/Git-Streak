from bs4 import BeautifulSoup
from datetime import datetime as date
import schedule
import requests
import smtplib


page = requests.get("https://github.com/Saicharan67")
soup = BeautifulSoup(page.content, "html.parser")


def SendMail(count):
    message = ""
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("gachibowlydiwalkar@gmail.com", "gachibowly@02")
    if count:
        message = """
         You Have Made {} Cnntributions Today...!

        """.format(
            count
        )

    else:
        message = """
            
            Your GitHub streak is about to break. Go and make a commit quick!
            """
    s.sendmail("gachibowlydiwalkar@gmail.com", "mahankalisaicharan@gmail.com", message)

    print("sent")
    s.quit()


def EmailStreak():
    Date = date.today()
    Todays_Date = str(Date.year) + "-" + str(Date.month) + "-" + str(Date.day)
    Todays_Streak = soup.find_all("rect", attrs={"data-date": Todays_Date})
    count = Todays_Streak[0]["data-count"]

    SendMail(count)
    print(count)


schedule.every().day.at("18:10").do(EmailStreak)
while True:
    schedule.run_pending()


#!/usr/bin/python
