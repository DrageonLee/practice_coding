'''수들의 합
N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

- 입력 설명
첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], ..., A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

- 출력 설명
첫째 줄에 경우의 수를 출력한다.

'''


#내 문제 풀이(for문 사용)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N, M = map(int,input().split())
list_num = list(map(int, input().split()))
cnt = 0
for i in range(N):
    res = list_num[i]
    if res == M : 
        cnt+=1
    for j in range(i+1, N):
        res += list_num[j]
        if res == M:
            cnt+=1
            break
print(cnt)

#다른 문제 풀이(while 문 사용)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N, M = map(int, input().split())
list_numbers = list(map(int, input().split()))
tot = list_numbers[0]
lt = 0
rt = 1
cnt = 0
while True:
    if tot < M :
        if rt < N:
            tot += list_numbers[rt]
            rt += 1
        else :
            break
    elif tot == M :
        cnt +=1
        tot -= list_numbers[lt]
        lt +=1
    else :
        tot -= list_numbers[lt]
        lt += 1

print(cnt)
