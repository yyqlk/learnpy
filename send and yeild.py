# AUTHOR : YYQLK
"""send和yield的运用，相当于简单的协程，下面是两个简单的实现，计数器和生产者消费者模型"""

#一个计数器,可以实现计算了sum函数执行了多少次
def count():
    i = 0
    while True:
        i = yield i + 1
        print(i)

def sum(s):
    n = 0
    s.send(None)
    while n < 5:
        n = s.send(n)
        print("执行{}次".format(n))
s = count()
sum(s)
# 输出：
# 0
# 执行1次
# 1
# 执行2次
# 2
# 执行3次
# 3
# 执行4次
# 4
# 执行5次



#第二个，生产者消费者模型
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[消费者]:收到 %s号产品'%n)
        r = '收到'


def produce(c):
    c.send(None) # 启动生成器，相当把生成器打开，在程序上体现为直接进去到yield循环

    n = 0
    while n < 5:
        n += 1
        print('[生产]: 生产%s号产品' %n)
        r = c.send(n)
        print('[生产]:消费者是否收到： %s' %r)
    c.close()
c = consumer()
produce(c)
#send（None）相当如启动该函数，遇到send函数，将参数发送到yeild，作为yield的返回值。
#往下执行，再次遇到yield结束，将yield返回值接受回来
  
# 输出：
# [生产]: 生产1号产品
# [消费者]:收到 1号产品
# [生产]:消费者是否收到： 收到
# [生产]: 生产2号产品
# [消费者]:收到 2号产品
# [生产]:消费者是否收到： 收到
# [生产]: 生产3号产品
# [消费者]:收到 3号产品
# [生产]:消费者是否收到： 收到
# [生产]: 生产4号产品
# [消费者]:收到 4号产品
# [生产]:消费者是否收到： 收到
# [生产]: 生产5号产品
# [消费者]:收到 5号产品
# [生产]:消费者是否收到： 收到

