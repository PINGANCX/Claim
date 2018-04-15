class Accident():
    def __init__(self, year = 2018, month = 4, day = 15, hour = 8, minute = 0, second = 0, x = 0, y = 0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.accident_x = x
        self.accident_y = y

    def _print_accident(self):
        print("date: " + str(self.year) + "-" + str(self.month) + '-' + str(self.day) +
              "  time: " + str(self.hour) + ":" + str(self.minute) + ':' + str(self.second) +
              "      x: " + str(self.accident_x) + "      Y: " + str(self.accident_y))
        '''输出这个事件的信息'''

    '''def _deil(self, read_from_excel):
        self.year = int(read_from_excel[0].split("-")[0])
        self.month = int(read_from_excel[0].split("-")[1])
        self.day = int(read_from_excel[0].split("-")[2])
        self.hour = int(read_from_excel[1].split(":")[0])
        self.minute = int(read_from_excel[1].split(":")[1])
        self.second = int(read_from_excel[1].split(":")[2])
        self.x = float(read_from_excel[2])
        self.y = float(read_from_excel[3])
        将excel里面的字符串转化成数字格式储存起来'''

