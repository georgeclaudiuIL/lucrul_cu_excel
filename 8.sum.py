import pandas as pd


df = pd.read_excel('users_rentals.xlsx')

# df["total_rentals"] = df['total_rentals'].astype('int')

df["total_rentals"] = pd.to_numeric(df["total_rentals"],errors="coerce")

sum = df["total_rentals"].sum()

print(sum)