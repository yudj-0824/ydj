# a = 5
# b = 15
# print(a**b)
#
#
# a = 1,2,3,4,5,6
# print(a)
#
# a,b,c = [1,2,3]
#
#
# print(a)
# print(b)
# print(c)
#
# x,y,*z = (1,2,3,4,5)
# print(x)
# print(y)
# print(z)
#
# a = 2
# b = 2
# print(a != b)
#
# print (a == 10 and b == 10)
# print (not(a == 10 or b == 20))





# z = 12333
# print(z % 10)
# z // 10
# print(z % 10)
# z // 10
# print(z % 10)
#
#
#
#
#
#
#
# q = 45782
# print(q % 10)

# a = ["奥迪","宝马","奔驰"]
# if ("宾利" in a):
#     print ("合作方")
# else:
#     print("非合作方")
#
#
#
#
# score_1 = [50,60,71,85,78,88,56,69]
# for score in score_1:
#     if (score > 0 and score < 60):
#         print("不及格")
#     elif (score >= 60 and score <= 70):
#         print("及格")
#     elif (score >= 71 and score <= 80):
#         print("良好")
#     elif(score >= 81 and score <= 100):
#         print("优秀")
#
# for i in range(12):
#      print(i)
#
# u = 0
# for i in range(2000):
#     u = u + i
# print(u)
#
# for i in range(1,1000,3):
#     print(i)
#
# s = 1
# for i in range(10,0,-1):
#     s *= i
# print(s)

# flag = True
# a = 1000
#
# while flag:
#     b = int (input("请输入数字"))
#     if b > a :
#         print("大了")
#     elif b < a :
#         print("小了")
#     else:
#         print("猜对了")
#         flag = False

# for i in range (1,100):
#     if (i % 6 != 0):
#         continue
#     print(i)

# def level(a,b):
#     print(a // b)
#     print(a % b)
# level(15,5)
# level(5,15)

# def shang_yu(a,b):
#     if (b == 0):
#         return None
#     else:
#         return (a//b,a%b)
#
# res = shang_yu(15,5)
# res =shang_yu(b=5,a=15)
#
# if res is None:
#     print("参数错误")
# else:
#     print("商为：",res[0],"余数为：",res[1])



# def sm(a,b=2):
#     return  a+b
# print (sm(2))

# c = 1,2,3,4
# a,*b = (1,2,3,4)
#
# def sum1(*args):
#     s = 0
#     for i in args:
#         s += i
#         s= s + i
#     return s
# print(sum1(1,2,3,4,5,6,12,13,14,15))




# c = 1,2,3,4
# a,*b = (1,2,3,4)
#
# def sum1(name,*args,**kwargs):
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum1(1,2,3,4,5,6,12,13,14,15))
# print(sum1(name="王大锤"))


# class calc():
#     a=None
#     b=None
#     res=None
#     def input (self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc()
#
# c.input(20,5)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()

# class calc():
#     res = None
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
# c = calc(20,20)
# c.sum()
# c.get_result()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",j*i,end="\t")
#     print()


# l = [1,34,544,666,23,56,89,197,21]
#
# length = len(l)
# for i in range (length-1,0,-1):
#     for j in range(i):
#         if (l[j] > l[j+1]):
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)

# l = [23,34,56,777,88,12,90,1]
#
# length = len(l)
# for i in range (length-1,0,-1):
#     for j in range(i):
#         if (l[j] > l[j+1]):
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)

# class Parent():
#
#     money =100000000000
#     house = 100
#     cloth = "鞋子"
#
#
#     def shou_yi(self):
#         print("点石成金")
#
# class Chlid(Parent):
#     ai_hao = "花钱"
#     pass
#
# c = Chlid()
# print(c.ai_hao)
# print(c.money)
# print(c.house)
#
#
#
# class aaa():
#     pub_res = "公有变量"
#     __pri_res = "私有变量"
#     _pri_res = "私有变量"
#
#
#     def pub_function(self):
#         print("公有方法")
#     def _pri_function(self):
#         print("私有方法")
#     def __pri_function(self):
#         print("私有方法")
#
# print(aaa.pub_res)
# print(aaa._pri_res)
# print(aaa().pub_function())
# print(aaa()._pri_function())

# a = 11,12,13,14,15
# l = [1,2,3,4,5,]
# t = (9,8,7,6,5,4)
# s ={12,13,14,15,16}
# print(tuple(a))
# print(list(a))
# print(set(a))
# print(set(l))

# f = open("abc.txt",'w')
# f.write("snoopy dog")
# f.close()

# f = open("abc.txt",'r')

# print(f.read())
# print(f.read(10))
# print(f.readline())
# print(f.readlines())
# f.close()

# a = "qwertyuiop"
# print(a[0])
# print(a[-1])
# print(a[1:-1])
# print(a[1:-2:2])
# print(a[-1:0:-1])
# print(a[::-1])
# print(a[2:])
# print(a[:-2])

# for i in range(1,10):
#     for j in range(1,i + 1):
#         print("%d X %d = %d"%(j,i,i*j),end="\t" )
#     print()

# for i in range(1,10):
#     for j in range(1,i + 1):
#         print("{} X {} = {}".format(j,i,i*j),end="\t")
#     print()

# l = [1,2,3,4,5,6,7,8,9]
# l[0] = 20
# print(l)
# l[1:3] = 20,3
# print(l)


l = [2,3,4,5,6]
# l.append("武大郎")
# l.append("潘金莲")
# l.extend({'123',123})
# l.insert(4,"武松")
# print(l)

# print(l.pop())
# print(l)

# print(l.pop(1))
# print(l)

# l.remove(2)
# print(l)
#
# l = [1,2,3,4,56,67]
# l.remove(2)
# print(l)
#
# l = [True,1,2,3,4,5]
# l.remove(1)
# print(l)
#
# l.clear()
# print(l)

# d = {"name":"小明","age":18,"sex":"男"}
# # d.update({"addr":"上海闵行","学历":"本科"})
# # print(d)

# try:
#     f = open("bbbb.txt",'r')
#     print(f.read())
#     f.close()
# except:
#     print("文件不存在")

class CustomException(Exception):
    def __init__(self,value="值不能为0"):
        self.value = value


    def __str__(self):
        return  self.value

    a = 0

    try:
        if a == 0:
            print("a = {}触发异常", format(a))
    except CustomException as e:
        print(e)

