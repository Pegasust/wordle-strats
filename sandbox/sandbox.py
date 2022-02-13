from collections import deque

def BFS(s):
    # don't need to reset every time
    # previously visited don't need to visit second time
#   for i in range(m*n):
#     visited[i] = False
  q = deque()
  visited[s] = True
  q.appendleft(s)
  global area_id
  while len(q) > 0:
    u = q.pop()
    areas[u] = area_id # instead of path, use area_id
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        q.appendleft(v)
        # path[v] = u
  area_id += 1
       
def translate(n):
  arr = [input().strip().split(' ') for i in range(n)]
  retval = set()
  # generating mapping: vertex = counter
  for r in range(n):
    for c in range(m):
      if arr[r][c] == '1':
        curr = r * m + c
        retval.add(curr)
   
        # check down
        if r+1 < n and arr[r+1][c] == '1':
          graph[curr].add(curr + m)
          graph[curr + m].add(curr)
        # check right
        if c+1 < m and arr[r][c+1] == '1':
          graph[curr].add(curr + 1)
          graph[curr + 1].add(curr)
        #check up
        if r-1 >= 0 and arr[r-1][c] == '1':
          graph[curr].add(curr - m)
          graph[curr - m].add(curr)
        # check left
        if c-1 >= 0 and arr[r][c-1] == '1':
          graph[curr].add(curr - 1)
          graph[curr - 1].add(curr)
     
  return arr, retval


cases = input()
while cases != '0 0':
  n, m = map(int, cases.split())
  visited = [False for i in range(m*n)]
#   path = [0 for i in range(m*n)]
  # slight mod: instead of path, we store
  # area number, that way, no backtrack.
  area_id = 1
  areas = [-1 for _ in range(m*n)]
  graph = [set() for i in range(m*n)]
  arr, ones = translate(n)

  ans = {}

  while len(ones) > 0:
    # print(f"{ones=}")
    temp = ones.pop()
    if visited[temp]:
        continue
    # print(f"{temp=}")
    BFS(temp)
    size = set()
    for o in ones:
      if areas[o] == areas[temp]:
        size.add(o)
    size.add(temp)
    ans[len(size)] = ans.get(len(size), 0) + 1
    ones.difference_update(size)

  s = sorted(ans.keys())
  print(sum(ans.values()))
  for i in s:
    print(i, ans[i])
  cases = input()