##################### Normal Starting Project ######################

import pandas
import smtplib
import random
import datetime as dt

my_email = "your-email"
my_password = "your-password"

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pandas.read_csv("birthdays.csv")

birthday_list_of_dicts_v2 = data.to_dict(orient="records")

for person_dict in birthday_list_of_dicts_v2:
    birthday = (person_dict["month"], person_dict["day"])
    if birthday == today:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            message = letter.read().replace("[NAME]", person_dict["Name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=person_dict["email"],
                                msg=f"Subject:Happy Birthday!\n\n{message}")
