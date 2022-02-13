from collections import deque

def within_bounds(x,y,sea):
  return y >= 0 and y < len(sea) and x >= 0 and x < len(sea[0])

def valid_neighbors(x, y, sea, visited):
  valid = []
  for offset_y, offset_x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    _y, _x = y + offset_y, x + offset_x
    if within_bounds(_x, _y, sea) and sea[_y][_x] == '1' and not visited[_y][_x]:
      valid.append((_y,_x))
  return valid
  
def bfs(x0, y0, sea, visited):
  """BFS through sea from x0 y0. Marks any visited node into `visited`
  Returns area of the chunk from x0 y0.

  Args:
      x0 ([type]): [description]
      y0 ([type]): [description]
      sea ([type]): [description]
      visited ([type]): [description]
  """
  bfs_q = deque()
  bfs_q.appendleft((y, x))
  area = 0
  while len(bfs_q) > 0:
    (_y, _x) = bfs_q.pop()
    area += 1
    # check 4 sides
    for __y, __x in valid_neighbors(_x, _y, sea, visited):
      bfs_q.appendleft((__y, __x))
      visited[__y][__x] = True
  return area

def adjacent_ones(sea):
  """
  Args:
      sea ([type]): [description]
  Returns:
      Dict[int, int]: mapping of area to count
  """
  visited = [[False for _ in range(len(sea[0]))] 
              for _ in range(len(sea))]
  adj_counts = dict()
  for y in range(len(sea)):
    for x in range(len(sea[0])):
      if visited[y][x]:
          continue
      visited[y][x] = True
      if sea[y][x] != '1':
          continue # just ignore 0
      area = bfs(x, y, sea, visited)
      adj_counts[area] = adj_counts.get(area, 0) + 1
  return adj_counts

if __name__ == "__main__":
  def main():
      cases = input()
      while cases != '0 0':
          n, m = map(int, cases.split())
          sea = [input().strip().split(' ') for i in range(n)]
          adjacents = adjacent_ones(sea)
          # report the total amount of areas
          print(f"{sum(adjacents.values())}")
          for area in sorted(adjacents.keys()):
              print(area, adjacents[area])
          cases = input()
  main()