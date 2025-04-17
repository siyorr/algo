import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B, N = map(int, input().split())

    cnt = 0

    while True:
        if A > N or B > N:
            break

        if A > B:
            B += A
        else:
            A += B

        cnt += 1

    print(f'#{tc}번 케이스')
    print(cnt)