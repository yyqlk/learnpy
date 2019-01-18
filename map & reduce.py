# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# map简单，就是接受一个函数，一个Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# 利用map和reduce实现一个字符串到浮点数的准换，这个实际意义可能不大，eval函数可以直接使用实现，但是eval使用时需要注意，eval时邪恶的



from functools import reduce


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int_part(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

def str2decimal_part(s):
    return reduce(lambda x, y: x * 10 +  y, map(char2num, s)) * pow(10,-len(s))

def str2float(s):
    s1=s.split('.')[0]
    s2=s.split('.')[1]
    return str2int_part(s1)+ str2decimal_part(s2)

print("str2float('123.456') =", str2float('123.456'))


# 输出：
# str2float('123.456') = 123.456
