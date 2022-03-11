'''정다면체

두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

- 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

- 출력설명
첫 번째 줄에 답을 출력합니다.

'''
#내 문제 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')

N, M = map(int, input().split())
list = []
count_max = 0
for i in range(1, N+1):
    for j in range(1,M+1):
        list.append(i + j)
for i in set(list):
    tmp = list.count(i)
    if tmp>count_max:
        count_max = tmp
for i in set(list):
    if list.count(i) == count_max:
        print(i, end=' ')

# 다른 문제 풀이(cnt list 만들기)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')

N, M = map(int, input().split())
cnt = [0]*(N+M+5)                   # cnt로 list를 만들어 놓고 count를 올리는 방법

for i in range(1,N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1
for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        print(i, end=' ')