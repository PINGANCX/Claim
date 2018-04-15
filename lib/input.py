from lib.accident import *
def read_excel():
    from lib import accident
    import xlrd
    ExcelFile = xlrd.open_workbook(r'data/input.xls')
    print (ExcelFile.sheet_names())
    '''告诉你这个文件已经成功读入了'''

    sheet1 = ExcelFile.sheet_by_name('Sheet1')
    '''确定我只要Sheet1'''

    a=1
    row=[]
    while 1:
        if a!=sheet1.nrows:
            year = int(sheet1.row_values(a)[0].split("-")[0])
            month = int(sheet1.row_values(a)[0].split("-")[1])
            day = int(sheet1.row_values(a)[0].split("-")[2])
            hour = int(sheet1.row_values(a)[1].split(":")[0])
            minute = int(sheet1.row_values(a)[1].split(":")[1])
            second = int(sheet1.row_values(a)[1].split(":")[2])
            x = float(sheet1.row_values(a)[2])
            y = float(sheet1.row_values(a)[3])
            row.append(Accident(year, month, day, hour, minute, second, x, y))
            '''print(row[a-1])'''
            a+=1
        else:
            break
    '''将每一行数据分别存进一个对象里面，然后返回list'''

    return row





