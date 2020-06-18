import sys
dict = {}
dict['one'] = 'caiji '
dict [2] = 'asdsd'

print(dict)
print(dict['one'])
print(dict.keys()) # 所有的key
print(dict.values()) #所有的value
'''
多行注释 
...
'''

print(1==2)

print(3**2,'幂等运算')

print('one' in dict)


d = 10
o = 10

print(d == o ,'==')
print(d is o ,'is')#  is 用于判断对象是不是同一个  == 是判断值是不是一样的

print(id(d) == id(o) , 'id 判断地址是否一致')

# suiji = random.choice(range(10)) 随机数
# # print(pi)  圆周率
# # print(e)  自然数 敞亮

print(r'\n')
print('\n')
print(R'\n')

apple = {'a','a','v'}
print(apple)
apple.add('sdsds')
print(apple)
apple.remove('a')
print(apple)