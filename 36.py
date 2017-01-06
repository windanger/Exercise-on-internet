#题目：求100之内的素数。
#程序分析：无。

def P(i) :
    a = 2
    prime = 0 #代表質數
    while a < i :
        if i % a == 0 :
            prime = 1 #非質數
            break
        a += 1
    return prime


for i in range(1,101) :
    if P(i) != 1 :
        print(i,'是')
