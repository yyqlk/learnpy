"""详细介绍装饰器"""
# 1.装饰器在不改变员代码的基础上添加功能
# def log(func):
#     def wrapper(*args, **kw):
#         print('获取函数的名字 %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def test(args):
# 	print ('hello,%s' %args)

# if __name__ == '__main__':
# 	test("like")	
# 输出：
# call test():
# hello,like
# 加装饰器等于执行了test = log（test），用同名的test函数指向了新的函数log（test）


# 2.如果新的功能需要传参数
# def log(text):
# 	def decrocate(func):
# 		print("功能需要的参数%s" %text)
# 		def wrapper(*args, **kw):
# 			print("获取函数的名字:%s" %func.__name__)
# 			return func(*args, **kw)
# 		return wrapper
# 	return decrocate
# @log("first")
# def test(args):
# 	print ('hello,%s' %args)

# if __name__ == '__main__':
# 	test("like")

# 输出：
# 功能需要的参数first
# 获取函数的名字:test
# hello,like




# 3.同时添加两个装饰器
# def log1(func):
#     def wrapper(*args, **kw):
#         print('第一个装饰器')
#         return func(*args, **kw)
#     return wrapper

# def log2(text):
# 	def dec(func):
# 		def wrap(*args, **kw):
# 			print("第二个功能需要的参数%s" %text)	
# 			print("第二个装饰器")
# 			return func(*args, **kw)
# 		return wrap
# 	return dec

# @log2("first")
# @log1
# def test(args):
# 	print ('hello,%s' %args)

# if __name__ == '__main__':
# 	test("like")
# print(test.__name__)

# 输出：
# 第二个功能需要的参数first
# 第二个装饰器
# 第一个装饰器
# hello,like
# wrap
#当遇到最上面的装饰器实现时，同名的test先指向log2（”first”）（test），但是发现之后的也是装饰器，
#于是先把函数用log1装饰器执行后，再用同名的test指向新的函数log2（“first”）（log1（test）），所以装饰时log1
#先装饰，但是执行时log2先执行，同时新的函数名字已经办成warp



#4 funtool.wrapper的功能
#打印经过装饰的函数，你会发现他的__name__已经变成wrap，因为只是我们用装饰的函数只是同名，他实际上已经指向了新的函数，名字已经
#变成warpper了，为了保证一些代码依赖函数签名的代码。，我们需要把他的__name__属性变回去


import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def test(args):
	print ('hello,%s' %args)

if __name__ == '__main__':
	test("like")
print(test.__name__)

# 输出：
# call test():
# hello,like
# test
