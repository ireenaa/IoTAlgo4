from collections import deque

row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


def check(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target


def floodfill(mat, x, y, replacement):
    if not mat or not len(mat):
        return

    q = deque()
    q.append((x, y))

    target = mat[x][y]

    if target == replacement:
        return

    while q:

        x, y = q.popleft()

        mat[x][y] = replacement

        for k in range(len(row)):

            if check(mat, x + row[k], y + col[k], target):
                q.append((x + row[k], y + col[k]))


