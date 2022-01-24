#미로탐색 문제 방법 1
from collections import deque

N, M = map(int, input().split())

root = []

for _ in range(N):
  root.append(list(map(int, input())))
print(root)

# 너비 우선 탐색
def bfs(y, x):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dy = [-1, 1, 0, 0] 
  dx = [0, 0, -1, 1]

  # deque 생성
  queue = deque()
  queue.append((y, x))

  while queue:
    y, x = queue.popleft()
    # print(queue.popleft())
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if ny < 0 or ny >= N or nx < 0 or nx >= M:
        continue
      
      # 벽이므로 진행 불가
      if root[ny][nx] == 0:
        continue
      
      # 벽이 아니므로 이동
      if root[ny][nx] == 1:
        root[ny][nx] = root[y][x] + 1
        queue.append((ny, nx))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return root[N-1][M-1]

print(bfs(0, 0))

#미로탐색 문제 방법 2

from collections import deque

N, M = map(int, input().split())
root = []                               #길
for _ in range(N):
  root.append(list(map(int, input())))

passed= [[-1]*M for _ in range(N)]      #지나온 길
passed[0][0]=1

def find_way(x,y) :
  q=deque()
  q.append((x,y))
    # 상,하,좌,우
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]

  while q:
      x,y=q.popleft()
      for i in range(4):
          nx = x+dx[i]
          ny = y+dy[i]
          if 0<=nx<N and 0<=ny<M and passed[nx][ny]==-1:
              if root[nx][ny]==1:
                  q.append((nx,ny))
                  passed[nx][ny]=passed[x][y]+1
                  print(passed)
  return passed[N-1][M-1]
print(find_way(0,0))
