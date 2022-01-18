#나의 풀이(16번 오답 / 효율성 bad)
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0]<K :
        if not (K>=0 and K<=1000000000):
            break
        if len(scoville) >=2:
            a = scoville[0] + scoville[1]*2
            scoville.pop(0)
            scoville.pop(0)
            scoville.insert(0,a)
            scoville.sort()
            answer+=1
            print(scoville)
            if len(scoville) <2:
                return -1
        else:
            return -1
            
    return answer
print(solution([3,4,5,6],10000000000 ))

#2 heapq 사용
import heapq                                                                        #python의 heapq module 불러옴

def solution(scoville, k):                                                          #solution 함수 set, scoville과 k를 argument로 받음
    heap = []                                                                       #빈 heap list를 setting 한다.
    for i in scoville:                                                              #scoville의 element에 대해 for문을 돌려서 heapq.heappush를 사용하여 heap에 해당 element i를 넣는다.
        heapq.heappush(heap, i)                                                     
    count = 0                                                                       #횟수를 return 해야 하므로 count=0을 setting
    while heap[0] < k:                                                              #heap[0]이 k보다 작을 경우 while문이 돌아감
        try :                                                                       #try / except를 써써 효율을 높임. if / else 문일 경우 못잡는 case가 있었음
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))   #heapq.heappush를 할 경우 자동 sorting됨
        except :                                                                    
            return -1                                                               #조건에서 벗어나는 경우 -1로 return 해야 하기에
        count += 1                                                                  #한번 섞을 때 마다 1씩 증가함
    return count                                                                    #횟수를 return 한다.

print(solution([3,4,5,6],10000000000 ))
