#내 문제 풀이(case 확인 필요함)
import sys
from collections import deque
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
num_list = list(map(int, input().split()))
num_list = deque(num_list)

tmp = 0
cnt = 0
str = ''
while True:
    if num_list[0] > tmp and num_list[-1] > tmp :
        if num_list[0] > num_list[-1]:
            cnt +=1
            tmp = num_list[-1]
            num_list.pop()
            str += 'R'
        elif num_list[0] < num_list[-1] :
            cnt+=1
            tmp = num_list[0]
            num_list.popleft()
            str += 'L'
        else : 
            break
    elif num_list[0] > tmp:
        cnt+=1
        tmp = num_list[0]
        num_list.popleft()
        str += 'L'
    elif num_list[-1] > tmp:
        cnt+=1
        tmp = num_list[-1]
        num_list.pop()
        str += 'R'
    else:
        break

print(cnt)
print(str)

#다른 문제 풀이(결정 알고리즘 사용)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
num_list = list(map(int, input().split()))
num_list = deque(num_list)

l = 0
r = N-1
tmp = 0
new_list = []
str = ''

while l<=r:
    if num_list[l] > tmp :
        new_list.append((num_list[l], 'L'))
    if num_list[r] > tmp : 
        new_list.append((num_list[r], 'R'))
    new_list.sort()
    if len(new_list) == 0:
        break
    else : 
        str = str + new_list[0][1]
        tmp = new_list[0][0]
        if new_list[0][1] == 'L':
            l +=1
        else:
            r -=1
    new_list.clear()
print(str)
print(len(str))