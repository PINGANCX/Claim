
#from datetime import date,datetime
class accident():
        def _init_(self,year=0,hour=0,minute=0,x=0.0,y=0.0):
            self.year=year
            self.hour=hour
            self.minute=minute
            self.x=x
            self.y=y
            """初始化事故的值"""

        def _print_accident(self):
            print("time: "+str(self.year)+"."+str(self.hour)+"."+str(self.minute)+"      x: "+str(self.x)+"      Y: "+str(self.y)  )
            """输出这个事件的信息"""

        def _deil(self,read_from_excel):
            self.year=int(read_from_excel[0].split(".")[0])
            self.hour=int(read_from_excel[0].split(".")[1])
            self.minute=int(read_from_excel[0].split(".")[2])
            self.x=float(read_from_excel[1])
            self.y=float(read_from_excel[2])
            """将excel里面的字符串转化成数字格式储存起来"""


def read_excel():
    import xlrd
    ExcelFile = xlrd.open_workbook(r'data/input.xlsx')
    print (ExcelFile.sheet_names())
    """告诉你这个文件已经成功读入了"""

    sheet1 = ExcelFile.sheet_by_name('Sheet1')
    """确定我只要Sheet1"""

    a=1
    row=[]
    while 1:
            if a!=sheet1.nrows:
                row.append(accident())
                """print(row[a-1])"""
                row[a-1]._deil(sheet1.row_values(a))
                a+=1
            else:
                break
    """将每一行数据分别存进一个对象里面，然后返回list"""

    return row





