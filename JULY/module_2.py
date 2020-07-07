from JULY import module_1
from JULY.module_1 import a as module_1_a,name,Test

a = "我是模块2中的a变量"

def name():
    print("我是模块2中的name方法")

class Test():
    name = "我是模块2中的Test类"

if __name__== '__main__':
    print(module_1_a)
    name()
    print(Test.name)


