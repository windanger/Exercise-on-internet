#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
#程序分析：请参照程序Python 练习实例14。


def result(n) :
    result_n =0
    for d in range(1,n) :
        if n % d == 0:
            result_n += d
    return result_n

for i in range(1,1000) :
    if result(i) == i:
        print(i)