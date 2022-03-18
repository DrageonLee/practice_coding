'''두리스트 합치기
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.

- 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

- 출력설명
오름차순으로 정렬된 리스트를 출력합니다.


'''

#내가 푼 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
list_N = list(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))
list_new = list_N + list_M
for i in sorted(list_new):
    print(i, end=' ')

#다른 문제 풀이(sort가 사용되지 않아서 시간 복잡도 면에서 더 효율적임)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
list_N = list(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))
x = 0
y = 0
new_list = []
while x< N and y < M :
    if list_N[x] <= list_M[y] :
        new_list.append(list_N[x])
        x+=1
    else :
        new_list.append(list_M[y])
        y+=1
if x < N:
    new_list = new_list + list_N[x:]
elif y <M:
    new_list = new_list + list_M[y:]
for i in new_list:
    print(i, end=' ')