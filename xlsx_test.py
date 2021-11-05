#Name: xlsx_test.py
#Description: Creates an excel workbook (if it does not already exist) and adds/modifies two additional worksheets. 

import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

worksheet = workbook.add_worksheet()

worksheet.write(1, 1, 'test')

workbook.close()