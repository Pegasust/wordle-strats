from collections import deque

def generate_neighbor_map(sea):
  interests, neighbor_map = set(), dict()
  m, n = len(sea[0]), len(sea)
  for r in range(n):
    for c in range(m):
      if arr[r][c] != '1':
        continue
      index = r * len(sea[0]) + c
      
      # check down
      if r+1 < n and sea[r+1][c] == '1':
        neighbor_map[index].add(index + m)
        neighbor_map[index + m].add(index)
      # check right
      if c+1 < m and sea[r][c+1] == '1':
        neighbor_map[index].add(index + 1)
        neighbor_map[index + 1].add(index)
      #check up
      if r-1 >= 0 and sea[r-1][c] == '1':
        neighbor_map[index].add(index - m)
        neighbor_map[index - m].add(index)
      # check left
      if c-1 >= 0 and sea[r][c-1] == '1':
        neighbor_map[index].add(index - 1)
        neighbor_map[index - 1].add(index)

def main():
  cases = input()
  while cases != '0 0':
    n, m = map(int, cases.split())
    sea = [input().strip().split(' ') for i in range(n)]
    interests, neighbor_map = generate_neighbor_map(sea)

