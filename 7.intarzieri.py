import pandas as pd


df = pd.read_excel("users_rentals.xlsx")

today = pd.Timestamp.today() 

interval = today - df.loc[1,"rental_date"]

print(interval>pd.Timedelta(31))

