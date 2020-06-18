tuple = ('abcd',789,2.33,'zdq' ,10.2)
tinytuple = (123,'zdq')

print(tuple)
print(tuple[0])
print(tuple[-1])
print(tuple*2)
print(tuple[1:])
print("#########")
print(tuple + tinytuple)


list1 = ['1','2','3']

tuple2 = (list1,)
print('@@@@@@@')
print(tuple2)
list1 = ['a','3']
print(tuple2)