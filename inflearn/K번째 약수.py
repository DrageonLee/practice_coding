# 내 문제 풀이(list 사용)

# N, K = map(int, input().split())

# def devisor(N, K):
#     result = []
#     for i in range(1,N+1):
#         if N%i ==0:
#             result.append(i)
#     if len(result)>=K:
#         return result[K-1]
#     else:
#         return -1

# print(devisor(N, K))

#해답 문제풀이(count 사용, 함수 사용 X)
N, K = map(int, input().split())

# count = 0
# for i in range(1, K+1):
#     if N%i==0:
#         count+=1
#     if count==K:
#         print(i)
#         break
# else :
#     print(-1)

#해답 문제풀이(count 사용, 함수 사용)
def devisor(N, K):
    count = 0
    for i in range(1, K+1):
        if N%i == 0:
            count+=1
        if count==K:
            return i
    else :
        return -1

print(devisor(N,K))