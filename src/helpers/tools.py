import os
import pandas as pd
from src.models.data_model import Person


def read_file(app_directory, files_directory, file):
    file_name = os.path.join(app_directory, files_directory)
    file_name = os.path.join(file_name, file)
    # print("read_file function:")
    extension = file_name.split('.')[-1]
    # print(extension)
    if(extension == 'txt'):
        # print("If txt")
        return read_txt(file_name)
    elif(extension == 'xlsx'):
        # print("If xlsx")
        return read_excel(file_name)
    elif(extension == 'csv'):
        # print("If csv")
        return read_csv(file_name)
    elif(extension == 'json'):
        # print("if json")
        return read_json(file_name)


def read_txt(file_name):
    data_text = []
    with open(file_name)as f:
        for line in f:
            row = line.split(',')
            p = Person(row[0], row[1], row[2])
            data_text.append(p)
    return data_text


def read_csv(file_name):
    data_csv = []
    # print("read_csv function")

    def get_data(row):
        data_csv.append(Person(row.iloc[0], row.iloc[1], row.iloc[2]))

        # return Person(a, b, c)
    df = pd.read_csv(file_name)
    # print(df)
    df.apply(lambda row: get_data(row), axis=1)
    return data_csv


def read_excel(file_name):
    data_excel = []
    # print("read_excel function")

    def get_data(row):
        data_excel.append(Person(row.iloc[0], row.iloc[1], row.iloc[2]))
    df = pd.read_excel(file_name)
    df.apply(lambda row: get_data(row))
    return data_excel


def read_json(file_name):
    data_json = []
    # print("read_json function")

    def get_data(row):
        data_json.append(Person(row.iloc[0], row.iloc[1], row.iloc[2]))
    df = pd.read_json(file_name, orient='records')
    df.apply(lambda row: get_data(row))
    # print(df)
    return data_json


def append_to_db(con, data):
    cur = con.cursor()
    try:
        cur.execute('''CREATE TABLE data
                    (FirstName text, LastName text, Age text)''')
    except Exception as e:
        print(e)
    for item in data:
        # print(type(item))
        fname = item.first_name
        lname = item.last_name
        age = item.age
        querystring = F"INSERT INTO data VALUES ('{fname}','{lname}','{age}')"
        # print(querystring)
        cur.execute(querystring)
    cur.close()


def show_data(con):
    cur = con.cursor()
    cur.execute('SELECT COUNT(*) FROM data')
    print(cur.fetchall())


def remove_file(app_directory, files_directory, file):
    file_name = os.path.join(app_directory, files_directory)
    file_name = os.path.join(file_name, file)
    os.remove(file_name)
