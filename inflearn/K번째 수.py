'''
title : K번째 수
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

-  입력설명
첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
각 케이스별
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다. 두 번째 줄에 N개의 숫자가 차례로 주어진다.

- 출력설명
각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.
'''

import sys
sys.stdin=open("/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt", "rt")
T = int(input())
# print(T)
for i in range(T):
    N, s, e, k = map(int, input().split())
    list_N = list(map(int, input().split()))

    list_split = list_N[s-1:e]
    list_split.sort()
    print(f'#{i+1}', list_split[k-1])
    # print(list_split)


    # print(list_N)
# N, s, e, k = map(int, input().split())
# print(N,s,e,k)