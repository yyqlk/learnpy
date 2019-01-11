# AUTHOR : YYQLK

"""getattr，setattr，hasattr的运用，通过输入字符串形式的属性方法名字来取出，设置，判断属性方法"""
# 1.getattr，setattr，hasattr
class student(object):
    def __init__(self,name,cls):
        self.name = name
        self.cls = cls
    def sex(self,sex):
        print('sex is %s'%sex)


lk = student("like",520) # 实例化类，万物皆对象
setattr(student,'socre',99) # 给对象设置一个属性或方法，给类一个方法，他的实例也自然有了
print(hasattr(lk,'socre')) # 判断是否有这个方法
print(lk.socre)
func = getattr(lk,'sex') # 通过getsttr获得了该对象的方法
print(func)
print(getattr(lk,'name')) #!!重要，getattr可以获得该对象的方法或者属性
func("male")

# 输出：
# True
# 99
# <bound method student.sex of <__main__.student object at 0x03526930>>
# like
# sex is male


# 2.内置的__getattr__方法如果遇到对象之中没有的属性和方法时会自动调用。以下是由两种实现，一种是通过这种方法实现字典也可以通过
#object.key 的方法调用，而是链式调用
#一： 
class Student(dict):
    def __init__(self, **kwargs):
        super(Student,self).__init__(**kwargs)
    def __getattr__(self, key):
        return self[key]
    def getvalue(self,key):
        return getattr(self,key,None)
s = Student(name= "li")
print(s.name)
print(s['name'])
print(getattr(s,"name"))

# 输出：
# li
# li
# li



#二 链式调用
class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__


s = Chain()
s2 = Chain('a')
print(s.a.b.c.d)
print(s2)
print(s2.a.b.c)


# 输出:
# /a/b/c/d
# a
# a/a/b/c