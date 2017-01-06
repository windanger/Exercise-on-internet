#题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。

first = input('字母 :')
while first != 'Q' :
    if first == 's' :
        first == input('字母 :')
        if first == 'u' :
            print('Sunday')
        else :
            print('Saturday')
    elif first == 'm' :
        print('Monday')
    elif first == 'w' :
        print('Wednesday')
    elif first == 'f' :
        print('Friday')
    else :
        first == input('字母 :')
        if first == 'u' :
            print('Tuesday')
        else :
            print('Thursday')