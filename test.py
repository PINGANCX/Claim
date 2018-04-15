from lib.random_input import *
from lib.output import *

excel, sheet = output()

for i in range(8):
    '''output_list = []
    for i in random_build(2018, 4, 15, i, 2)'''
    write(random_build(2018, 4, 15, i, 2), i*2, (i+1)*2, excel, sheet)

from lib.input import *
row = read_excel()

for i in row:
    i._print_accident()

