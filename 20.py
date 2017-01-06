#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
#程序分析：无

length = 0
t = 0
list1 = []
list2 = []
def Totaldrop(t) :
    length = 100
    while t > 0 :
        list1.append(length)
        length /= 2
        t -=1
    return list1

print(Totaldrop(10))

def Totalraise(t) :
    length = 100
    while t>0 :
        length /= 2
        list2.append(length)
        t -= 1
    return list2

print(Totalraise(10))
a = Totaldrop(10)
print(a[9])
b = Totalraise(10)
print(b[9])