'''K번째 큰 수
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려 고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값 은 22입니다.

- 입력 설명
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력 된다.

- 출력설명
첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.
'''

# 나의 문제 풀이
import sys
sys.stdin = open("/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt", "rt")
N, K = map(int, input().split())
card_list = list(map(int, input().split()))

result = []
for i in range(len(card_list)-2):
    for y in range(i+1,len(card_list)-1):
        for z in range(y+1, len(card_list)):
            result.append(card_list[i]+card_list[y]+card_list[z])
    # print(result)
result_list = list(set(result))
result.sort(reverse=True)
print(result[K-1])

#다른 문제 풀이(먼저 set() class를 불러오기)

import sys
sys.stdin = open("/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt", "rt")
N, K = map(int, input().split())
card_list = list(map(int, input().split()))

result = set()

for i in range(len(card_list)-2):
    for y in range(i+1,len(card_list)-1):
        for z in range(y+1, len(card_list)):
            result.add(card_list[i]+card_list[y]+card_list[z])

result = list(result)
result.sort(reverse=True)
print(result[K-1])