import copy
import sys
from collections import deque


def part12(grid,part):
    # convert S and E to regular characters representing elevation
    q = deque()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                grid[r][c] = 'a'
                if part == 1:
                    q.append((0, r, c))
            elif grid[r][c] == 'E':
                end_row,end_column=r,c
                grid[r][c] = 'z'
                if part == 2:
                    q.append((0, r, c))
    visited = set()

    while q:
        d, r, c = q.popleft()
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            rr=r+dr
            cc=c+dc
            if (rr,cc) in visited:
                continue
            # bounds check
            if not (0<=rr<len(grid) and 0<=cc<len(grid[0])):
                continue

            # can we step to next field?
            if part == 1 and ord(grid[rr][cc]) - ord(grid[r][c]) > 1:
                continue
            if part == 2 and ord(grid[rr][cc]) - ord(grid[r][c]) < -1:
                continue

            # have we reached the end?
            if part == 1 and rr==end_row and cc==end_column:
                return d+1
            if part == 2 and grid[r][c]=='a':
                return d

            # standard bfs
            q.append((d+1, rr, cc))
            visited.add((rr,cc))




if __name__ == "__main__":
    with open(sys.argv[1] if len(sys.argv)>1 else "input-day-12.txt", "r") as f:
        data = f.read().strip()
        grid = [list(line) for line in data.split('\n')]
        grid_copy=copy.deepcopy(grid)
        print(part12(grid,1))
        grid=copy.deepcopy(grid_copy)
        print(part12(grid,2))
