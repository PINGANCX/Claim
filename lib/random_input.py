import random
def random_x():
    return random.random()*100%100 + 0.01* random.random()%100

def random_y():
    return random.random()*100%100 + 0.01* random.random()%100

def random_hour():
    return  random.random()*100% 24

def random_minute():
    return random.random() *100 % 60

def random_accident():
    accident=[]
    accident.append(2018)
    accident.append(random_hour())
    accident.append(random_minute())
    accident.append(random_x())
    accident.append(random_y())
    return accident
