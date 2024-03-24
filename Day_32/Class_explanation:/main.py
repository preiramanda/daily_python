import smtplib
import datetime as dt
import random as r

#DELETE HERE 
password = "your pass here"
sender = "your email"
receiver = "the recipient email"

now = dt.datetime.now().weekday()
week_days = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}


if now == 6: #monday
    #connecting to the email server from my email (sender)
    #Its important to check which SMTP will send, so if your email is outlook, it will be :
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        #securing the connection (encrypt the message if intercepted)
        connection.starttls()
        #loggin 
        connection.login(user=sender, password=password)

        with open("quotes.txt") as quotes_txt:
            quotes = quotes_txt.readlines()
            msg = quotes[r.randint(0, len(quotes))]
            
        email_content = f"Subject: Sunday's quote\n\n{msg}"

        connection.sendmail(from_addr=sender, to_addrs=receiver, msg=email_content.encode('utf-8'))

else:
    today = ", ".join([key for key, value in week_days.items() if value == now])

    print(f"Today's weekday is {today}, we only send emails on Sundays")
