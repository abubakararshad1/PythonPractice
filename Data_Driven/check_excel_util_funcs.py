from Data_Driven import excel_utils

file = "E:\\excel_auto_files\\myfile.xlsx"

excel_utils.write_data(file, "sheet1", 1, 1, "Name")
excel_utils.write_data(file, "sheet1", 1, 2, "Age")
excel_utils.write_data(file, "sheet1", 1, 3, "ID")

excel_utils.write_data(file, "sheet1", 2, 1, "Jack")
excel_utils.write_data(file, "sheet1", 2, 2, "24")
excel_utils.write_data(file, "sheet1", 2, 3, "001")

# fetch rows and column data

print(excel_utils.get_row_count(file, "sheet1"))             #2
print(excel_utils.get_column_count(file, "sheet1"))          #3


excel_utils.fill_red(file, "sheet1", 1, 1)
excel_utils.fill_green(file, "sheet1", 1, 2)


# reading data
print(excel_utils.read_data(file, "sheet1", 1, 1))
print(excel_utils.read_data(file, "sheet1", 1, 2))
print(excel_utils.read_data(file, "sheet1", 1, 3))
print(excel_utils.read_data(file, "sheet1", 2, 1))
print(excel_utils.read_data(file, "sheet1", 2, 2))
print(excel_utils.read_data(file, "sheet1", 2, 3))
