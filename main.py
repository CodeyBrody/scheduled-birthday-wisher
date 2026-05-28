from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
NUMBER_OF_LETTERS = 3

birthday_list = pandas.read_csv("birthdays.csv")

today = dt.datetime.today()
month = today.month
day = today.day
birthday_people = birthday_list[(birthday_list["day"] == day) & (birthday_list["month"] == month)]
birthday_people_list = birthday_people.to_dict(orient="records")

for person in birthday_people_list:
    rand_letter_index = rand.randint(1, NUMBER_OF_LETTERS)
    with open(rf"letter_templates\letter_{rand_letter_index}.txt") as letter:
        letter_text = letter.read()
        letter_text = letter_text.replace("[NAME]", person["name"].split()[0])
        
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:HAPPY BIRTHDAY!! :)\n\n{letter_text}"
        )
