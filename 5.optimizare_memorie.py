import pandas as pd


df = pd.read_excel('users_rentals.xlsx')

df["id"] = df['id'].astype('int16')

print(df.dtypes)