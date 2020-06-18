#
#
# a,b = 0,1
# while b< 10 :
#     print(b , end=' ')
#     a,b = b,a+b
#
# if (b>0):
#     print("aaa")
#
# while(1==1) :
#     # print('asadsd')
#     pass
#
import sys
langgeuges = ['c','java','php','python']
for x in langgeuges:
    print(x)
else:
    print('##',x)


for i in range(10):
    pass
    print(i)
print('@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!')
list =['1','2','3','6','7']
it = iter(list)
while 1:
    try:
        print(next(it),'qa')
    except StopIteration:
        sys.exit()

print('!!!!!!!!!!!!!!!!!!!!!!!!')
for x in it:
    print(x)
