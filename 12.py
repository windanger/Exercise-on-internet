#题目：判断101-200之间有多少个素数，并输出所有質数。


def f(n) :
    i=2
    prime = 0
    while i<= int(n)**0.5 :
        if n % i == 0 :
            prime = 1
        i +=1
    return prime

for n in range(101,201) :
    if f(n) == 0 :
        print(n)

print(f(7))