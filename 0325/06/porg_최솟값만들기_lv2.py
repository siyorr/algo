import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    ans = 0

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        ans += A[i] * B[i]

    print(f'#{tc}')
    print(ans)
