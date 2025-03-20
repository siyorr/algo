import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    schedules = list(map(int, input().split()))
    N = len(schedules)
    timelogs = [list(map(int, input().split())) for _ in range(N)]
    startday = int(input())
    result = int(input())



    sat = 6 - startday
    sun = 7 - startday
    if sat == -1:
        sat = 6
    hope = 0 # 출근 인정 시간

    ans = 0

    for i in range(7):
        if schedules[i] % 100 > 49:
            hope = (((schedules[i] // 100) + 1) * 100) + (schedules[i] % 100 - 50)
        else:
            hope = schedules[i] + 10

        for j in range(N):
            if j == sat or j == sun:
                continue

            if timelogs[i][j] > hope:
                break
        else:
            ans += 1

    print(ans)