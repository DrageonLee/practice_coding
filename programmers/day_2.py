'''
기능개발

프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

입출력 예
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
입출력 예 설명
입출력 예 #1
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

입출력 예 #2
모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.

따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.
'''


# deque 사용
from collections import deque                       #collections 모듈에서 deque를 불러 옴

def solution(progresses, speeds):
    deq1 = deque(progresses)                        #progresses의 deque화
    deq2 = deque(speeds)                            #speeds의 deque화
    answer = []                                     #빈 배열
    number = 0                                      #count는 0으로 부터 시작해야 함(answer내의 값)
    day = 0                                         #걸리는 날짜                        
    while deq1:                                     #progresses deque가 True일 동안
        day +=1                                     #day는 하루씩 중가
        if deq1[0] + deq2[0]*day >= 100:            #progresses의 첫번째 값 + speeds 첫번째 값*days이 100이상 일 경우
            number +=1                              #count+1하고
            deq1.popleft()                          #progresses에서 popleft()하여 지운다
            deq2.popleft()                          #speeds에서도 popleft()하여 지운다
            day -=1                                 #day+1인 상태에서 진행되면 day별 비교를 할 수가 없음(만약 다음 원소가 day=2인 상태에서 계산되면 바로 추가가 됨)
        else :                                      #if의 조건이 아닐 경우
            if number > 0:                          #day가 1씩 증가되고 100이 넘는 경우가 아닐 경우, 더 이상 하루에 같이 제거 될 요소가 없기에 count가 0보다 큰 경우 
                answer.append(number)               #count를 answer list에 삽입함
                number = 0                          #그리고 다시 count는 reset

    answer.append(number)                           #while문을 다돌았을 경우는 아직 count를 append 못했기에 추가해 줌
    return answer                                   #answer return 반환

print(solution([99,98,97,98], [1,2,2,3]))

#list로 사용 시
def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0
    while progresses:
        days = days+1
        if progresses[0] + speeds[0]*days >=100:
            count = count +1
            progresses.pop(0)
            speeds.pop(0)
            days = days -1
        else:
            if count > 0 :
                answer.append(count)
                count = 0
    answer.append(count)
    return answer

print(solution([99,98,97,98], [1,2,2,3]))