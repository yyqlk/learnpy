# AUTHOR : YYQLK
def yhsj(d):
    n = 1
    a=[1]
    while n <= d:
        yield a
        a = [1] + [a[x-1]+a[x]for x in range(1,n)] +[1]
        n= n+1
for i in yhsj(10):
    print(i)


