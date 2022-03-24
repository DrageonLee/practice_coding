'''봉우리
지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

- 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.

- 출력설명
봉우리의 개수를 출력하세요.
'''

import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
block = [list(map(int, input().split())) for _ in range(N)]
block.insert(0, [0]*N)
block.append([0]*N)
for i in range(N+2) : 
    block[i].insert(0,0)
    block[i].append(0)
# print(block)
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if block[i][j] >block[i-1][j] and block[i][j] > block[i][j-1] and block[i][j] > block[i+1][j] and block[i][j] > block[i][j+1]:
            cnt +=1

print(cnt)

#다른 풀이(방향 축 setting 하고 all() 함수 사용)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
block = [list(map(int, input().split())) for _ in range(N)]
block.insert(0, [0]*N)
block.append([0]*N)
for i in block : 
    i.insert(0,0)
    i.append(0)
    # 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        #all 함수 사용(방향 포함)
        if all(block[i][j] > block[i + dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)