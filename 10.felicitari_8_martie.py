import pandas as pd

df = pd.read_excel("users_rentals.xlsx")

mask = (df['active'] == 'Y') & (df['gender'] == 'female')
new_df = df[mask]

print(new_df.to_string)