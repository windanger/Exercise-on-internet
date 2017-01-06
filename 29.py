#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
#程序分析：学会分解出每一位数。

n = input('輸入數字 : ')
if len(n) == 0 :
    print('輸入錯誤')
elif len(n) > 5 :
    print('輸入錯誤')
else :
    print(len(n),'位數')
    for i in n[::-1] :
        print(i)