#题目：输入某年某月某日，判断这一天是这一年的第几天？
#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于3时需考虑多加一天：

months = [0,31,59,90,120,151,181,212,243,273,304,334]
year = int(input('年 : '))
month = int(input('月 : '))
day = int(input('日 : '))
leap = 0

if (year % 400 == 0 or (year%4==0 and year%100 != 0)) and month>3 :
    sum = months[month-1]+day
    print(sum)
else :
    sum = months[month - 1] + day
    print(sum)