class B :
    name  , age = 'allen','12'

    def namecheng(name) :
        print('name')

class V(B) :
    def namecheng(name):
        name = 'assd'
        age = 988
    def __init__(self):
        self.name ='adssdsd'

class C :
    def namecheng(name):
        print('12343433')



class L :
    def namecheng(name):
        print('sadsddf')



class test(C,L,B):
    pass

test1 = test()
test1.namecheng()


# x = B()
# print(x.age)
# print(x.name)
# vv =V()
# print(vv.name)
# print(vv.age)