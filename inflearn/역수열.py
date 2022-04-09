'''역수열
1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 1부터 n까지 각각의 수 앞 에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다.
예를 들어 다음과 같은 수열의 경우 48625137
1앞에 놓인 2앞에 놓인 3앞에 놓인
따라서4 8
n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 원래의 수열을 출 력하는 프로그램을 작성하세요.

- 입력 설명
첫 번째 줄에 자연수 N(3<=N<100)이 주어지고, 두 번째 줄에는 역수열이 숫자 사이에 한
칸의 공백을 두고 주어진다.
- 출력 설명
원래 수열을 출력합니다.
'''

import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
num_list = list(map(int, input().split()))

new_list = [0]*N

for i in range(N):
    for j in range(N):
        if num_list[i] ==0 and new_list[j] == 0:
            new_list[j] = i + 1
            break
        elif new_list[j] == 0:
            num_list[i] -= 1

print(new_list)