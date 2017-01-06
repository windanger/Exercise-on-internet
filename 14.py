#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成
#(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
#(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
n = int(input('請輸入需要分解的數 : '))

def Factorization(n):                  #判斷因數
    n = int(n)
    for a in range(2, 10000):
        if n % a == 0 :
            return a
    return 0

def f(n):                               #判斷質數
    i = 2
    prime = 0
    while i <= int(n) ** 0.5:
        if n % i == 0:
            prime = 1
        i += 1
    return prime

val = int(Factorization(n))
list = []
if f(n):
    while val > 1:
        n = n / val
        list.append(val)
        val = Factorization(n)
    print(list)
    l = len(list)
else:
    print(n, '是質數')
