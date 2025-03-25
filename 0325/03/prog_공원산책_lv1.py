import sys

sys.stdin = open('input.txt')

def search_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'S':
                return i, j

def search_dis(arr):
    res = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                res.append([i,j])
    return res

T = int(input())
for tc in range(1, T+1):

    park = list(input().split())
    routes = list(input().split(','))

    for i in range(len(park)):
        park[i] = list(park[i])

    for i in range(len(routes)):
        routes[i] = list(routes[i].split())

    N, M = len(park), len(park[0])

    start_x, start_y = search_start(park)
    dis = search_dis(park)
    now_x, now_y = start_x, start_y

    for d, num in routes:
        num = int(num)
        if d == 'E':
            if now_y + num >= M:
                continue
            for dy in range(1, num+1):
                if [now_x, now_y+dy] in dis:
                    break
            else:
                now_y += num
        elif d == 'W':
            if now_y - num < 0:
                continue
            for dy in range(1, num+1):
                if [now_x, now_y-dy] in dis:
                    break
            else:
                now_y -= num
        elif d == 'S':
            if now_x + num >= N:
                continue
            for dx in range(1, num+1):
                if [now_x+dx, now_y] in dis:
                    break
            else:
                now_x += num
        elif d == 'N':
            if now_x - num < 0:
                continue
            for dx in range(1, num+1):
                if [now_x-dx, now_y] in dis:
                    break
            else:
                now_x -= num

    result = [now_x, now_y]

    print(f'#{tc}')
    print(result)