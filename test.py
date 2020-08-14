# import module as mod
import os
from module import min as m, plus as p

print(m(12,2))
print(os.getpid())	
try:
	print(p(3, 8))
except NameError:
	print('Такого метода НЕТ !!!')

a = ['aito', 'python']
print(a.add['aito'])

















# import os
# print(os.listdir(path="."))


