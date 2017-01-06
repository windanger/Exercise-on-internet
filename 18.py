#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
#程序分析：关键是计算出每一项的值。

n = int(input('輸入數字 : '))
t = int(input('輸入次數 : '))
c = n
times = 1
list = []

while times <= t :
    list.append(n)
    n = n*10 + c
    times +=1
print(list)

result = 0
for number in list :
    result += number
print(result)