#내가 푼 문제 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
blocks = [list(map(int, input().split())) for _ in range(9)]
print(blocks)
correct = [1,2,3,4,5,6,7,8,9]
set_correct = set(correct)

for i in range(9):
    a = []
    for j in range(9):
        a.append(blocks[i][j])
    set_a = set(a)

    if set_a != set_correct:
            print("No")
            break
    else : 
        pass
for i in range(9):
    b = []
    for j in range(9):
        b.append(blocks[j][i])
    set_b = set(b)

    if set_b != set_correct:
        print("No")
        break
    else : 
        pass
    #좌상, 상, 우상, 좌하, 하, 우하, 좌, 우, 중간
dx = (-1, -1, -1, 1, 1, 1, 0, 0, 0)
dy = (-1, 0, 1, -1, 0, 1, -1, 1, 0)

for i in range(1,9,3):
    for j in range(1,9,3):
        c = []

        for u in range(9):
            c.append(blocks[i+dx[u]][j+dy[u]])
        set_c = set(c)
    if set_c != set_correct :
        print("No")
        break
    else : pass
print("Yes")

#다른 문제 풀이(함수 사용)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
blocks = [list(map(int, input().split())) for _ in range(9)]
def check_duplication(a):
    for i in range(9):
        ch_horizon = [0] * 10
        ch_vertical = [0] * 10
        for j in range(9):
            ch_horizon[blocks[i][j]] = 1
            ch_vertical[blocks[j][i]] = 1
        if sum(ch_horizon) != 9 or sum(ch_horizon) != 9:
            return False
    
    for i in range(3):
        for j in range(3):
            ch_surround = [0]*10
            for k in range(3):
                for s in range(3):
                    ch_surround[blocks[i*3 + k][j*3 + s]] = 1
            if sum(ch_surround) != 9:
                return False
    return True

b = check_duplication(blocks)
if b == True : 
    print('Yes')
else : 
    print('No')

#내 문제 풀이 + 다른 문제 풀이(다른 문제 풀이에 내문제 풀이 추가(네모 범위 부분))
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
blocks = [list(map(int, input().split())) for _ in range(9)]

def check_duplication(a):
    for i in range(9):
        ch_horizon = [0] * 10
        ch_vertical = [0] * 10
        for j in range(9):
            ch_horizon[blocks[i][j]] = 1
            ch_vertical[blocks[j][i]] = 1
        if sum(ch_horizon) != 9 or sum(ch_horizon) != 9:
            return False
    #내가 푼 문제 풀이 추가
    dx = (-1, -1, -1, 1, 1, 1, 0, 0, 0)
    dy = (-1, 0, 1, -1, 0, 1, -1, 1, 0)
    for i in range(1,9,3):
        for j in range(1,9,3):
            ch_surround = [0] * 10
            for k in range(9):
                ch_surround[blocks[i + dx[k]][j + dy[k]]] = 1
            if sum(ch_surround) != 9 : 
                return False
    return True

b = check_duplication(blocks)
if b == True : 
    print('Yes')
else : 
    print('No')