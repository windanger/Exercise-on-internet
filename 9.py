#题目：暂停一秒输出。

import time

dictionary = {'a':1,'b':2,'c':3}
for k,v in dictionary.items() :
    print(k,v)
    time.sleep(1)