'''주사위 게임
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게 임이 있다.
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된 다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금 으로 받게 된다.
N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램 을 작성하시오

- 입력 설명
첫째 줄에는 참여하는 사람 수 N(2<=N<=1,000)이 주어지고 그 다음 줄부터 N개의 줄에 사람 들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

- 출력 설명
첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.

'''

#내 문제 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
max_money = 0
for i in range(N):
    list_N = list(map(int, input().split()))
    # print(list_N)
   
    if len(set(list_N)) == 1:
        res = 10000 + list_N[0]*1000
        # print(res)
    elif len(set(list_N)) == 2:
        for i in set(list_N):
            if list_N.count(i) == 2:
                res = 1000 + i*100
                # print(res)
    elif len(set(list_N)) == 3:
        max = 0
        for i in list_N:
            if i >max:
                max = i
        res = 100 * max
    if res > max_money:
        max_money = res

print(max_money)


# 다른 문제 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
max = 0
for i in range(N):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    
    # print(a, b, c)
    if a==b==c :
        res = 10000 + a*1000
    elif a==b or a==c:
        res = 1000 + 100*a
    elif b==c:
        res = 1000 + 100*b
    else :
        res = 100 * c
    if res > max:
        max = res

print(max)