from lib.accident import *
def output():
    import xlwt
    excel = xlwt.Workbook()
    sheet = excel.add_sheet("Sheet1",cell_overwrite_ok=True)
    #新增一个sheet

    sheet.write(0, 0, "date")
    sheet.write(0, 1, "time")
    sheet.write(0, 2, "x")
    sheet.write(0, 3, "y")

    excel.save(r"data/input.xls")

    return excel, sheet

def write(accident_list, begin, end, excel, sheet):
    i = 0
    line=begin
    while(1):
        if(line!=end):
            sheet.write(line+1,0,str(accident_list[i].year)+'-'+str(accident_list[i].month)+'-'+str(accident_list[i].day))
            sheet.write(line+1,1,str(accident_list[i].hour)+':'+str(accident_list[i].minute)+':'+str(accident_list[i].second))
            sheet.write(line+1,2,accident_list[i].accident_x)
            sheet.write(line+1,3,accident_list[i].accident_y)
            i+=1
            line+=1
        else:
            break

    excel.save(r"data/input.xls")


