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