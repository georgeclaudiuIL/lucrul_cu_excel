import pandas as pd


df = pd.read_excel('users_rentals.xlsx')

rows = []

today = pd.Timestamp.today()

for index, row in df.iterrows():

    interval = today - row['rental_date']

    if(interval > pd.Timedelta(days=31)):

        rows.append(row)

new_df = pd.DataFrame(data=rows, columns=df.columns)

print(new_df)