import datetime as dt
import pandas as pd
import smtplib
import random as r

### EMAIL CONFIGS -------------------------------------------------------------------------------------
password = "your email pass here"
sender = "your email  here"

### GETTING BIRTHDAYS -------------------------------------------------------------------------------------------

today = dt.datetime.now()
today_list = [today.year, today.month, today.day]
df = pd.read_csv("birthdays.csv")

# Creating a DF with all people making birthday today.
# To read this, I'm tapping inside the dataframe, in the df column "day", then I'm checking
# if matches the second element in today's list & if the df column "moth" also works

matches_today_df = df[(df["day"] == today_list[2]) & (df["month"] == today_list[1])]

dictionary = matches_today_df.to_dict(orient="records")

if not dictionary:
    print("No birthdays for today")
else:
    for person in dictionary:
        person['age'] = int(today_list[0]) - person['year']  # Calculating age and adding it as a new key

### SENDING BIRTHDAY EMAILS -------------------------------------------------------------------------------------

#getting random text to email
file_path = f"letter_templates/letter_{r.randint(1,3)}.txt"

with open(file_path) as letter_txt:
    letter = letter_txt.read()

for person in dictionary:

    msg = letter.replace("[NAME]", person['name']).replace("[YEAR]", str(person['age']))

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        #securing the connection (encrypt the message if intercepted)
        connection.starttls()
        #loggin 
        connection.login(user=sender, password=password)
     
        email_content = f"Subject: Happy Birthday {person['name']}\n\n{msg}"

        connection.sendmail(from_addr=sender, to_addrs=person["email"], msg=email_content.encode('utf-8'))
