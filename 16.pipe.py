import pandas as pd


# extract data

def extract_user_data(file_name):

    return pd.read_excel(file_name)


# filter data

def filter_users(data):

    mask = (pd.Timestamp.today() - data['rental_date']) > pd.Timedelta(days=31)

    return data[mask]


# sort data

def sort_data(data):

    return data.sort_values(by='rental_date', ascending=True)


# add new column

def add_new_column(data):

    data["overdue_days"] = (pd.Timestamp.today() - data['rental_date']).dt.days - 31

    return data


# remove columns

def remove_columns(data):

    data = data.drop(['address', 'gender', 'city', 'active'], axis=1)

    return data


# load data

def load_data(data):

    data.to_excel("overdue_users.xlsx", index=False)


df = extract_user_data('users_rentals.xlsx').pipe(filter_users).pipe(sort_data).pipe(add_new_column).pipe(remove_columns)

load_data(df)