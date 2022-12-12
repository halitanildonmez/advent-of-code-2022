import math
import collections

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
Lines = file1.read().splitlines()

input_grid = []

for i, line in enumerate(Lines):
    if len(line.strip()) == 0:
        continue
    input_grid.append(line)

neighs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def height_vals(r, c):
    if input_grid[r][c] == 'S':
        return ord('a')
    if input_grid[r][c] == 'E':
        return ord('z')
    return ord(input_grid[r][c])

def bfs(grid, start, end):
    dists = []
    for i in range(len(grid)):
        vals = []
        for j in range(len(grid[0])):
            vals.append(math.inf)
        dists.append(vals)
    dists[start[0]][start[1]] = 0
    queue = collections.deque([[start[0], start[1]]])
    while queue:
        x, y = queue.popleft()
        for nind in neighs:
            cx = x + nind[0]
            cy = y + nind[1]
            if 0 <= cx < len(grid) and 0 <= cy < len(grid[0]):
                if height_vals(cx, cy) <= height_vals(x, y) + 1 and dists[cx][cy] == math.inf:
                    queue.append((cx, cy))
                    dists[cx][cy] = dists[x][y] + 1
    return dists[end[0]][end[1]]



print('part1:', bfs(input_grid, (20, 0), (20, 72)))

a_paths = []
for r in range(len(input_grid)):
    for c in range(len(input_grid[r])):
        if input_grid[r][c] == 'a':
            a_paths.append((r, c)) 
results = []
for ap in a_paths:
    results.append(bfs(input_grid, (ap[0], ap[1]), (20, 72)))
    
print('part2:', min(results))
