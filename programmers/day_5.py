#1 시간 초과 뜸
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    list = []
    dicReport = {id : [] for id in id_list}
    for i in set(report):
        split = i.split(" ")
        list.append(split[1])
        dicReport[split[0]].append(split[1])
    print(dicReport)
    pick = set([x for x in list if list.count(x)>=k])
    for key, value in dicReport.items():
        for x in pick:
            if x in value:
                answer[id_list.index(key)] +=1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))


#2 약간의 수정 = 통과
def solution(id_list, report, k):
    answer = [0] * len(id_list)                 #answer에 id_list의 길이만큼의 빈 list 확보
    dicReport = {id : [] for id in id_list}     #id_list의 dictionary 화
    for i in set(report):                       #report가 중복된 거 없게(중복 되어도 1개만 인정되니까)
        split = i.split(" ")                    #split을 사용하여 2개로 나눈다.
        dicReport[split[1]].append(split[0])    #몇명이 신고했는지를 파악하기 위해 신고 당한 사람을 key로 두고 신고한 사람을 value의 list 내에 append 한다.
    for key, value in dicReport.items():        #dictionary의 key와 value를 for문을 돌려서
        if len(value)>=k:                       #value의 길이가 k이상이면(k명 이상이 신고 했으면)
            for x in value:                     #해당 하는 value를 for문을 돌려서
                print(x)
                print(value)
                answer[id_list.index(x)] +=1    #answer의 각 index(value)에 대한 id_list 자리에 +1을 한다.
                print(dicReport)
                print(answer)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
