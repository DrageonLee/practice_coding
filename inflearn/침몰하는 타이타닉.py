'''침몰하는 타이타닉(그리디)
유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고 있습니다. 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있 으며, 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 프로그램을 작성하세요.

- 입력 설명
첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다. 각 승객의 몸무게는 M을 넘지는 않습니다. 즉 탈출을 못하는 경우는 없습니다.

- 출력 설명
첫째 줄에 구명보트의 최소 개수를 출력합니다.
'''

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