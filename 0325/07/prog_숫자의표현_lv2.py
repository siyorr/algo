import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    n = int(input())
    res = 0

    for i in range(1, n+1):
        tmp = 0
        for j in range(i, n+1):
            tmp += j
            if tmp == n:
                res += 1
                break

            if tmp > n:
                break



    print(f'#{tc}')
    print(res)