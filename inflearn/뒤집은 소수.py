''' 뒤집은 소수

N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력 한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하 여 프로그래밍 한다.

- 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 100,000를 넘지 않는다.

- 출력설명
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.
'''

#내 문제 풀이
# import sys
# sys.stdin = open("/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt", "rt")

# N = int(input())
# number_list = list(map(int, input().split()))

# def reverse(x):
#     x = str(x)
#     reverse_x = int(x[len(x)::-1])
#     return reverse_x

# def isPrime(x):
#     cnt = 0
#     for i in range(1, x+1):
#         if x%i==0:
#             cnt +=1
#     if cnt == 2:
#         return x

# for i in number_list:
#     rev = reverse(i)
#     if isPrime(rev):
#         print(isPrime(rev), end=' ')

# 다른 문제 풀이
import sys
sys.stdin = open("/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt", "rt")

N = int(input())
number_list = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10+t
        x = x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else :
        return True

for i in number_list:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=' ')