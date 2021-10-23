import sqlite3
import os
import time
from src.data.mock_data import initData
from src.helpers.tools import append_to_db, read_file, remove_file, show_data

# Essential Paths
app_directory = os.path.dirname(__file__)
data_directory = os.path.join(app_directory, "data")
files_directory = os.path.join(app_directory, "files")
# Sqlite database
con = sqlite3.connect("src/data/app_data.db")
cur = con.cursor()

data = []

while True:
    initData()
    if os.path.exists(files_directory):
        file_list = [fileName for _, _,
                     fileName in os.walk(files_directory)][0]
        # print(file_list)
        for file in file_list:
            data.extend(read_file(app_directory, files_directory, file))
            remove_file(app_directory, files_directory, file)

    if(len(data) > 0):
        append_to_db(con, data)
        data.clear()
    print("******** Last Data *********")
    show_data(con)
    time.sleep(10)

print(data)
