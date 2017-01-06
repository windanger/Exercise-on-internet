#题目：利用递归方法求5!。

def f(i) :
    result = 0
    if i == 1 :
        return 1
    else :
        return i*f(i-1)

print(f(5))