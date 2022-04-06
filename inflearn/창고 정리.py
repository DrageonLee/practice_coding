'''창고 정리
창고에 상자가 가로방향으로 일렬로 쌓여 있습니다. 만약 가로의 길이가 7이라면
[자료구조와 알고리즘]
1열은 높이가 6으로 6개의 상자가 쌓여 있고, 2열은 3개의 상자, 3열은 9개의 상자가 쌓여 있 으며 높이는 9라고 읽는다.
창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.
가장 높은 곳이나 가장 낮은 곳이 여러곳이면 그 중 아무거나 선택하면 된다.
위에 그림을 1회 높이 조정을 하면 다음과 같아진다.

창고의 가로 길이와 각 열의 상자 높이가 주어집니다. m회의 높이 조정을 한 후 가장 높은 곳 과 가장 낮은 곳의 차이를 출력하는 프로그램을 작성하세요.

- 입력 설명
첫 번째 줄에 창고 가로의 길이인 자연수 L(1<=L<=100)이 주어집니다.
두 번째 줄에 L개의 자연수가 공백을 사이에 두고 입력됩니다. 각 자연수는 100을 넘지 않습니다
세 번째 줄에 높이 조정 횟수인 M(1<=M<=1,000)이 주어집니다.

- 출력 설명
M회의 높이 조정을 마친 후 가장 높은곳과 가장 낮은 곳의 차이를 출력하세요.
'''

import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
L = int(input())
num_list = list(map(int, input().split()))
M = int(input())
num_list.sort(reverse=True)

for i in range(M):
    num_list[0] -= 1 
    num_list[-1] += 1
    num_list.sort(reverse=True)
print(num_list[0] - num_list[-1])
