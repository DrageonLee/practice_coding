'''격자판 최대합

N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합 니다.

- 입력 설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.

- 출력 설명
최대합을 출력합니다.
'''

#내가 푼 문제 풀이

import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

largest = 0
for i in range(N):
    horizon=vertical = 0
    for j in range(N):
        horizon += numbers[i][j]
        vertical += numbers[j][i]
        if horizon > largest:
            largest = horizon
        if vertical > largest :
            largest = vertical

horizon_vertical =0
reverse_horizon_vertical =0
for i in range(N):
    horizon_vertical += numbers[i][i]
    reverse_horizon_vertical += numbers[i][-i-1]
 
if horizon_vertical or reverse_horizon_vertical > max:
    max = horizon_vertical or reverse_horizon_vertical
print(max)

#다른 문제 풀이

import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

largest = 0
for i in range(N):
    horizon=vertical = 0
    for j in range(N):
        horizon += numbers[i][j]
        vertical += numbers[j][i]
        if horizon > largest:
            largest = horizon
        if vertical > largest :
            largest = vertical

horizon_vertical =0
reverse_horizon_vertical =0
for i in range(N):
    horizon_vertical += numbers[i][i]
    reverse_horizon_vertical += numbers[i][-i-1]
if horizon_vertical > largest:
    largest = horizon_vertical
if reverse_horizon_vertical > largest:
    largest = reverse_horizon_vertical    
print(largest)  