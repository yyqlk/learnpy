''' 利用filter，filter类似于一个筛选器，下面是它的一些实现'''

#用filter实现取范围内的回数，两种方法
def is_palindrome_1(n):
    n = str(n)
    return n == n[::-1]
print(list(filter(is_palindrome_1,range(0,1000))))

def is_palindrome_2(n):
    I, m = n, 0
    while I:
        m = m * 10 + I % 10 # 从后获取数字的最后一位然后往前移动一位
        I = I // 10 # 获取到第一位停止，此时m是i翻转的数
    return n == m
print(list(filter(is_palindrome_2,range(0,1000))))

#实现回数的扩展
def is_palindrome(n):
    I, m = n, 0
    while I:
        m = m * 10 + I % 10 # 从后获取数字的最后一位然后往前移动一位
        I = I // 10 # 获取到第一位停止，此时m是i翻转的数
    if n == m:
        print(n)
    else:       
        nn = n + m  #如果不是回数，我们可以把他和他的相反数相加获取回数
        print('%d+%d=%d' % (n, m, nn))
        is_palindrome(nn)

is_palindrome(int(input('输入整数:')))
