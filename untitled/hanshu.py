from _collections import deque
def hanshu1 ():
    print(range(1,10))

def area (width ,hight) :
    print(width*hight)
    return width* hight


area(12,9) # 函数的调用

def  raere (list):
    print(list)

list = ['1','4','0']
raere(list)
list[0] = '9'
print(list)

def changge (a):
    a = 9

j = 1
changge(j)
print(j)

queue = deque(['1','w','e'])
queue.append("df")
print(queue)

ass = queue.pop()
print(ass)