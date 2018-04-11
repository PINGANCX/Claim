
from lib.input import *
row = read_excel()

for i in row:
    i._print_accident()

from lib.random_input import *



from lib.output import *

accidents=[]

for i in range(1,200):
    accidents.append(random_accident())
    '''不要误会，这是声明了199个对象'''

output(accidents,199)

