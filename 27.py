#题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
#程序分析：无。

i = input('輸入 : ')
l = len(i)
def opposite(i,l) :
    if l == 0 :
        return
    print(i[l-1])
    opposite(i,l-1)


opposite(i,l)