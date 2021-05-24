'''
def f(n):
    if n==1: return 1
    if n==0: return 1
    return n*f(n-2)

while(True):
    c = int(input("원하는 숫자를 입력하십시오."))
    d = int(input("입력한 값이 홀수이면 1번, 짝수면 2번을 입력하십시오. 종료를 원하면 3번 입력"))
    if d % 2 == 1:
        print(f(c))
    elif d % 2==0:
        print(f(c - 1))
    else:
        break

def f1(n):
    if n==1: return 1
    if n%2==0:
        return 1*f1(n-1)
    if n%2==1:
        return n*f1(n-1)


print(f1(5))
print(f1(6))
'''

import matplotlib.pyplot as mp
import random
import math
x=[i for i in range(101)]
y=[]
for i in range(101): y.append(random.randrange(1,50))
mp.plot(x,y,c='#ff0000')
mp.show()








