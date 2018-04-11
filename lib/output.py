def output(accident,index):
        import xlwt
        excel = xlwt.Workbook()
        sheet = excel.add_sheet("sheet1",cell_overwrite_ok=True)
        #新增一个sheet

        sheet.write(1,1,"year")
        sheet.write(1,2,"hours")
        sheet.write(1,3,"minutes")
        sheet.write(1,4,"x")
        sheet.write(1,5,"y")

        i=0
        while(1):
            if(i!=index):
                 sheet.write(i+2,1,accident[i][0])
                 sheet.write(i+2,2,accident[i][1])
                 sheet.write(i+2,3,accident[i][2])
                 sheet.write(i+2,4,accident[i][3])
                 sheet.write(i+2,5,accident[i][4])
                 i+=1
            else:
                break

        excel.save(r"data/output.xls")


