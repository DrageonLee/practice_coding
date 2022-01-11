# Day 1 : 완주하지 못한 선수

'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.'''

# My solution 1(틀린 방법)
#처음에는 set으로 풀려 하였으나 동명이인에 대해서 놓침
def solution(participant, completion):
    if set(participant) - set(completion) != {}:
        result = list(set(participant)-set(completion))
        return result[0]
    
    elif set(participant) == set(completion) :
        for i in participant : 
            if participant.count(i) == 2 :
                return i

# My solution 2(수정)
# list에 sort 사용
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[(len(participant)-1)]

# 다른 풀이 방법 1
# collections를 import 하여 사용, 쌈빡한 접근 법 이었음
import collections

def solution(participant, completion) :
    dict1 = collections.Counter(participant)
    dict2 = collections.Counter(completion)
    return type(dict1), type(dict2)

# 다른 풀이 방법 2
# hash method를 사용
def solution(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer