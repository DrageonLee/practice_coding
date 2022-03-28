'''이분 검색
임의의 N개의 숫자가 입력으로 주어집니다. N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요. 단 중복값은 존재하지 않습니다.

- 입력 설명
첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다. 두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.

- 출력 설명
첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.
'''


import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N, M = map(int, input().split())
list_N = list(map(int, input().split()))

#내가 푼 풀이(간단하게)
list_N.sort()
for i in range(len(list_N)):
    if list_N[i] == M:
        print(i+1)

#내가 푼 풀이(이분 검색)
list_N.sort()
l = 0
r = N-1
# while True:                 # while문을 true로 해도 되나 l <= r로 해도 됨(l이 r보다 커지면 안되니까)
while l<=r:
    avg = (l+r)//2
    if M == list_N[avg] :
        print(avg+1)
        break
    elif M > list_N[avg] :
        l = avg+1
    elif M < list_N[avg] :
        r = avg -1