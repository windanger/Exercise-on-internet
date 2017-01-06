#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
#程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

list = [2,3,4,5,6,77]
n = int(input('數字 : '))
i = 0
l = len(list)
while l :
    if n < list[l-1] :
        l -= 1
    else :
        list.insert(l,n)
        print(list)
        break
