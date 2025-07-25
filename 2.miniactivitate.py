import pandas as pd

users = pd.read_excel("users_rentals.xlsx")

tenth_user_data = users.iloc[9]
print(tenth_user_data)
print()

user_56_last_name = users.loc[55,"lastname"]
print(user_56_last_name)
print()

user_1_phone = users.loc[0,"phone"]
print(user_1_phone)
print()

all_phones = users["phone"]
print(all_phones)