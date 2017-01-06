#目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
#程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

scores = int(input('輸入成績 : '))
grades = ''
if scores > 90 :
    grades = 'A'
elif 60 <= scores <= 89 :
    grades = 'B'
else :
    grades = 'C'

print('{} belongs to {}'.format(scores,grades))