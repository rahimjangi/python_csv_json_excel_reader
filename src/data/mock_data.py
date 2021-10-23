def initData():
    from src.models.data_model import Person
    import json
    import xlsxwriter

    p1 = Person("firstName1", "lastName11", 10)
    p2 = Person("firstName2", "lastName12", 23)
    p3 = Person("firstName3", "lastName13", 34)
    p4 = Person("firstName4", "lastName14", 54)
    p5 = Person("firstName5", "lastName15", 23)
    p6 = Person("firstName6", "lastName16", 12)
    p7 = Person("firstName7", "lastName17", 12)
    p8 = Person("firstName8", "lastName18", 34)
    p9 = Person("firstName9", "lastName19", 56)

    obj_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

    data = '\n'.join(map(str, obj_list))
    workbook = xlsxwriter.Workbook('src/files/files.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    worksheet.write(0, 0, "first_name")
    worksheet.write(0, 1, "last_name")
    worksheet.write(0, 2, "age")
    for item in obj_list:
        worksheet.write(row, 0, item.first_name)
        worksheet.write(row, 1, item.last_name)
        worksheet.write(row, 2, item.age)
        row += 1
    workbook.close()
    print("Excel file created")

    with open("src/files/files.csv", "w") as f:
        f.write(data)
        print("CSV file created")

    with open("src/files/files.txt", "w") as f:
        f.write(data)
        print("Text file created")

    with open("src/files/file.json", "w") as f:
        json_string = json.dumps([ob.__dict__ for ob in obj_list])
        f.write(json_string)
        print("Json file created")
