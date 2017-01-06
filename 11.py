#题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
#假如兔子都不死，问每个月的兔子总数为多少？
#程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

n = int(input('請輸入月份: '))
def Rabbit(n) :
    if n == 1 or n== 2 :
        return 1
    else :
        return Rabbit(n-1)+Rabbit(n-2)

print(Rabbit(n))