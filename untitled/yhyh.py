print("hello world")
a = 111.0
b = isinstance(a,int)
print(b)

class A :
    pass

class B(A) :
    pass

c = isinstance(A(),A)
print(c)

print(type(A()) == A)
print("##################")

print(isinstance(B(),A)) # python 中isinstance 会认为 自雷是父类的类型
print(type(B()) == A)

boo1 = 0
if(boo1) :
    print("true!!@#@#@#@#@!")
else :
    print("false 3434343243432")
print("@@@@@@@@@@@@@@@")
str1 = 'asdfg'
print(str1[1],str1[4])
print(str1[-1],str1[-5])