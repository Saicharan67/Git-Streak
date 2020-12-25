from bs4 import BeautifulSoup
from datetime import datetime as date
import schedule
import requests
import smtplib
from email.message import EmailMessage


page = requests.get("https://github.com/Saicharan67")
soup = BeautifulSoup(page.content, "html.parser")


def SendMail(count):
    msg = EmailMessage()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("gachibowlydiwalkar@gmail.com", "gachibowly@02")
    if count != "0":
        msg["Subject"] = "Well Done You Are Maintaining Your Git Streak..!"

        text = """
        
         You Have Made {} Contributions Today...!""".format(
            count
        )
        msg.set_content(text)
    else:
        msg["Subject"] = "Your Git Streak About To Break...!"
        text = """
        
        Your GitHub streak is about to break. Go and make a commit quick!

        """
        msg.set_content(text)
    s.sendmail(
        "gachibowlydiwalkar@gmail.com", "mahankalisaicharan@gmail.com", msg.as_string()
    )

    print("sent")
    s.quit()


def EmailStreak():
    Date = date.today()
    Todays_Date = str(Date.year) + "-" + str(Date.month) + "-" + str(Date.day)
    Todays_Streak = soup.find_all("rect", attrs={"data-date": Todays_Date})
    count = Todays_Streak[0]["data-count"]

    SendMail(count)
    print(count)


schedule.every().day.at("15:00").do(EmailStreak)
while True:
    schedule.run_pending()


#!/usr/bin/python
