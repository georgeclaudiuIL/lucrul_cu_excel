import pandas as pd


df = pd.read_excel("users_rentals.xlsx")

mask = (pd.Timestamp.today() - df["rental_date"]) > pd.Timedelta(days=31)

new_df = df[mask]

new_df2= new_df.sort_values(by="rental_date", ascending = True)

new_df2["overdue_days"] = (pd.Timestamp.today() - new_df2["rental_date"]).dt.days - 31

new_df2.drop(['address', 'gender', 'city', 'active'], axis = 1, inplace = True)

print(new_df2)