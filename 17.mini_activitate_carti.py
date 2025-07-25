import pandas as pd


def extract_user_data(file_name):
    return pd.read_excel(file_name)

def filter_users(data):
    mask = (pd.Timestamp.today() - data["rental_date"]) > pd.Timedelta(days=31)
    return data[mask]

def sort_data(data):
    return data.sort_values(by="rental_date", ascentind = True)

def add_new_column(data):
    data["overdue_days"] = (pd.Timestamp.today() - data["rental_date"]).dt.days - 31
    return data

def remove_columns(data):
    data = data.drop(['address', 'gender', 'city', 'active'], axis = 1, inplace = True)
    return data

def extract_books_data(file_name):
    return pd.read_csv(file_name)

def merge_with_books_data(user_data):

    book_data = extract_books_data("books.csv")

    user_data['rental_book_name'] = None

    user_data['rental_book_author'] = None

    for i,row in user_data.iterrows():
        book_row = book_data[book_data["id"] == row["rental_book_id"]]
        if not book_row.empty:
            user_data.loc[i, "rental_book_name"] = book_row["title"].values[0]
            user_data.loc[i, "rental_book_author"] = book_row["author"].values[0]

def load_data(data):
    data.to_excel("overdue_users2.xlsx", index=False)

df = extract_user_data('users_rentals.xlsx').pipe(filter_users).pipe(add_new_column).pipe(remove_columns).pipe(sort_data).pipe(merge_with_books_data)

load_data(df)
