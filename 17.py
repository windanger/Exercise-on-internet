#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#程序分析：利用while语句,条件为输入的字符不为'\n'。

import string

s = input('請輸入字串 :')
letter = 0
number = 0
space = 0
other = 0

for i in s :
    if i.isalpha() :
        letter +=1
    elif i.isdigit() :
        number +=1
    elif i.isspace() :
        space +=1
    else :
        other +=1
print('letter:{},number :{},space :{},other{}'.format(letter,number,space,other))