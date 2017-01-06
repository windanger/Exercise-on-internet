#题目：求1+2!+3!+...+20!的和。
#程序分析：此程序只是把累加变成了累乘。

def resut(i) :
    total = 1
    while i :
        total = total * i
        i -=1
    return total

adds = 0
for i in range(1,21) :
    adds += resut(i)
print(adds)