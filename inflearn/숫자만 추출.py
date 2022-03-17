#내 문제 풀이
from curses.ascii import isdigit
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = input()
tmp_list = []
list = list(N)
for i in list:
    if i.isnumeric():
        tmp_list.append(i)
a = ''.join(tmp_list)
a = int(a)
cnt = 0
for i in range(1, a+1):
    if a %i ==0:
        cnt +=1
print(a)
print(cnt)

#다른 문제 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = input()
res = 0
cnt = 0
for i in N:
    if isdigit(i):
        res = res*10 + int(i)
for x in range(1, res+1):
    if res % x ==0 :
        cnt+=1
print(res)
print(cnt)