import smtplib
import pandas as pd
import datetime as dt
import random

# Create Dataframe
data = pd.DataFrame({
    "Name": ["Kamran", "Lambda"],
    "Email": ["kamazim121212@gmail.com", "v241649@osfc.ac.uk"],
    "Year": [2024, 2006],
    "Month": [12, 4],
    "Day": [12,3],
})

birth_date = []
for index, row in data.iterrows():
    date = dt.datetime(row["Year"], row["Month"], row["Day"])
    birth_date.append(date)

data["Birth_Date"] = birth_date

# Send email on birthday with appropriate letter
for index, row in data.iterrows():

    if [dt.datetime.now().day, dt.datetime.now().month] == [row.Birth_Date.day, row.Birth_Date.month]: 
        with open(f"letter_{random.randint(1,3)}.txt", "r") as letter:
            text = letter.read().strip()
            text = text.replace("[NAME]", row.Name)
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = "lambdaa112@gmail.com", password = "xxxxx")
            connection.sendmail(from_addr="lambdaa112@gmail.com", to_addrs="kamazim121212@gmail.com", msg = f"Subject:Happy Birthday!\n\n{text}")
