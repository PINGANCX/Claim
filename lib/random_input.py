from lib.accident import *
import random

def random_build(year = 2018, month = 4, day = 15, hour = 0, loop = 2):
    rand_accident_list = []
    for i in range(loop):
        minute = random.randint(60/loop * i, 60/loop * (i+1))
        second = random.randint(0, 60)
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        temp_accident = Accident(year, month, day, hour, minute, second, x, y)
        rand_accident_list.append(temp_accident)
    return rand_accident_list