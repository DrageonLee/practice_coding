
# #내가 푼 문제 풀이 1(max를 비교해 가며 풀기)
# import sys
# sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
# N = int(input())
# number_list = list(map(int, input().split()))
# res = []
# max = 0
# def digit_sum(x):
#     str_x = str(x)
#     list_int = list(map(int, list(str_x)))
#     return sum(list_int)

# for i in number_list:
#     tmp = digit_sum(i)
#     if tmp>max:
#         max = tmp
#         max_number = i
# print(max_number)

# #내가 푼 문제 풀이2(max 함수 사용)

# import sys
# sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
# N = int(input())
# number_list = list(map(int, input().split()))
# res = []

# def digit_sum(x):
#     str_x = str(x)
#     list_int = list(map(int, list(str_x)))
#     return sum(list_int)

# for i in number_list:
#     res.append(digit_sum(i))
# max_number = max(res)
# index = res.index(max_number)
# print(number_list[index])

# #다른 문제 풀이 1(함수 내에 while 문 안에 수의 나머지와 몫을 이용)

# import sys
# sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
# N = int(input())
# number_list = list(map(int, input().split()))

# def digit_sum(x):
#     sum = 0
#     while x>0:
#         sum += x%10
#         x=x//10
#     return sum

# max = 0
# for i in number_list:
#     total = digit_sum(i)
#     if total > max:
#         max = total
#         number = i

# print(number)

#다른 문제 풀이 2(함수 내 sum 을 list를 쓰지 않고 더하기 해주는 것)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
number_list = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum
max = 0
for i in number_list:
    total = digit_sum(i)
    if total > max:
        max = total
        number = i

print(number)