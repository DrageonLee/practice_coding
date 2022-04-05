'''회의실 배정(그리디)
한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들 려고 한다. 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 단, 회의는 한번 시작하면 중간에 중 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

- 입력설명
첫째 줄에 회의의 수 n(1<=n<=100,000)이 주어진다. 둘째 줄부터 n+1 줄까지 각 회의의 정 보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.

- 출력설명
첫째 줄에 최대 사용할 수 있는 회의 수를 출력하여라.
'''


#내 문제 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
n = int(input())
num_list = list(tuple(map(int, input().split())) for _ in range(n))
num_list.sort(key = lambda x:x[1])

cnt = 1
ep = num_list[0][1]

for i in range(n):
    if ep <= num_list[i][0]:
        cnt += 1
        ep = num_list[i][1]
print(cnt)

#다른 문제 풀이(조금 더 다듬어 짐)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
n = int(input())
num_list = []
for i in range(n):
    s, e = map(int, input().split())
    num_list.append((s, e))
num_list.sort(key = lambda x : (x[1], x[0]))

cnt = 0
ep = 0
for s, e in num_list:
    if s >= ep:
        cnt +=1
        ep = e
print(cnt)