from lib.accident import *
from lib.input import *

class Car():
    def __init__(self, x = 0.0, y = 0.0, dest_x = 100, dest_y = 100):
        self.x = x
        self.y = y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.state = 'wait'

class Algorithm1():
    def __init__(self):
        self.accident_list = []
        self.accident_list = read_excel()
        self.car_list = []
        self.car_list.append(Car(0, 0))
        self.car_count = 1
        self.wait_time = 0
        self.cost = 0
        self.score = 0

    def process(self):
        for accident in self.accident_list:
            pass

