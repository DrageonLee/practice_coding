'''소수(에라토스테네스 체)

자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 제한시간은 1초입니다.

- 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

- 출력설명
첫 줄에 소수의 개수를 출력합니다.

'''


#내 문제 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
res = 0
for i in range(2,N+1):
    # print('i =', i)
    cnt = 0
    for x in range(1,i+1):
        # print('x = ', x)
        if i%x==0:
            cnt+=1
    # print(cnt)
    if cnt == 2:
        res +=1
print(res)

#다른 문제 풀이 방법(count_list를 따로 만들어서 해당 하는 값을 0==>1로 변경)

import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
count_list = [0]*(N+1)
cnt = 0

for i in range(2, N+1):
    if count_list[i] == 0:
        cnt +=1
        for j in range(i, N+1, i):
            count_list[j]=1
print(cnt)