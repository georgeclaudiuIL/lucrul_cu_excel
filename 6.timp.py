import pandas as pd


df = pd.read_excel('users_rentals.xlsx')

month = df.loc[1,'rental_date'].month

print(month)