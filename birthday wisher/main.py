
import pandas as pd
import smtplib
import datetime as dt
import os
import random

my_email = "email"
my_password = "pass"

data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
for index, row in data.iterrows():
    if now.day == row["day"] and now.month == row["month"]:

        folder = "letter_templates/"
        files = os.listdir(folder)

        file = random.choice(files)
        with open("letter_templates/" +file) as letter:
            content = letter.read()

        new_content = content.replace('[NAME]', row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy birthday \n\n{new_content}"
            )
