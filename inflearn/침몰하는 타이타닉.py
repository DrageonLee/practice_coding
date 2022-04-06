import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
cnt = 0
while len(num_list) :
    if num_list[0] + num_list[-1] > M :
        num_list.pop()
        cnt+=1
    elif num_list[0] + num_list[-1] <= M and len(num_list) >=2 :
        num_list.pop(-1)
        num_list.pop(0)
        cnt+=1
    else :
        num_list.pop(0)
        cnt+=1
        break
print(cnt)

#다른 문제 풀이(if 순서 바꿈)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
cnt = 0
while num_list :
    if len(num_list) == 1:
        cnt+=1
        break
    if num_list[0] + num_list[-1] > M :
        num_list.pop()
        cnt+=1
    else:
        num_list.pop(-1)
        num_list.pop(0)
        cnt+=1
print(cnt)

#다른 문제 풀이(deque 사용)
import sys
from collections import deque
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
num_list = deque(num_list)
cnt = 0
while num_list :
    if len(num_list) == 1:
        cnt+=1
        break
    if num_list[0] + num_list[-1] > M :
        num_list.pop()
        cnt+=1
    else:
        num_list.pop()
        num_list.popleft()
        cnt+=1
print(cnt)