#题目：对10个数进行排序。
#程序分析：
#可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。


list = []
q = 1
n = input('輸入數字(Q離開)')
while q :
    if n != 'Q' :
        list.append(n)
    else :
        break
    n = input('輸入數字(Q離開)')
    list.sort()
print(list)