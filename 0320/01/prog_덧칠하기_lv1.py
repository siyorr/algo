import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    section = list(map(int, input().split()))

    wall = [0] * N

    for n in section:
        wall[n-1] = 1

    ans = 0

    i = 0
    while True:
        if i + M <= N: # 찾아야 하는 벽이 롤러 보다 많이 남았을 때
            if wall[i] == 1:
                for k in range(i, i+M):
                    if wall[k] == 1:
                        wall[k] = 0
                ans += 1
                i += M
                continue
        else: # 찾아야 하는 벽이 롤러 보다 적게 남았을 때
            for k in range(i, N):
                if wall[k] == 1:
                    ans += 1
                    break
            break

        i += 1


    print(ans)

