'''사과나무
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다.

- 입력 설명
첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다. 각 격자안의 사과의 개수는 100을 넘지 않는다.

- 출력 설명
수확한 사과의 총 개수를 출력합니다.

'''

# 내 문제 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt','rt')
N = int(input())
blocks = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    if 0<= i and i<= N//2 :
        for j in blocks[i][-i+N//2 : i+1+N//2]:
            cnt += j
    elif i > N//2:
        for j in blocks[i][i-N//2 : N//2-i] :
            cnt += j
        
print(cnt)

#다른 문제 풀이(더 간단)

import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt','rt')
N = int(input())
blocks = [list(map(int,input().split())) for _ in range(N)]
res = 0
l = r = N//2
for i in range(N):
    for j in range(l,r+1):
        res += blocks[i][j]
    if i < N//2 :
        l -= 1
        r += 1
    else :
        l += 1
        r -= 1

print(res)