'''마굿간 정하기
N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마 구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다. 각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.

- 입력 설명
첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다. 둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.

- 출력 설명
첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.
'''

#내 문제 풀이(C가 다양화 되는 것을 생각하지 못함)

import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N, C = map(int, input().split())
point_list = list(int(input()) for _ in range(N))
def distance(number):
    point_list.sort()
    for x in range(N):
        for y in range(x, N):
            for z in range(y, N):
                if point_list[y]-point_list[x] >= number and point_list[z] - point_list[y] >= number :
                    return True
    else :
        return False
l=0
r=N
max = 0
while l <= r:
    avg = (l+r)//2
    tmp = distance(avg)
    if tmp == True :
        max = avg 
        l = avg + 1
    else : 
        r = avg - 1

print(max)

#다른 문제 풀이

import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N, C = map(int, input().split())
point_list = list(int(input()) for _ in range(N))
point_list.sort()
def Count(number):    
    ep = point_list[0]
    cnt = 1
    for i in range(1, N):
        if point_list[i] - ep >= number:
            cnt+=1
            ep = point_list[i]
    return cnt
l=1
r= point_list[N-1]
res = 0
while l <= r:
    avg = (l+r)//2
    if Count(avg)>=C :
        res = avg 
        l = avg + 1
    else : 
        r = avg - 1

print(res)