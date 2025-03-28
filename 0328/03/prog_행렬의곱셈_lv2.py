import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n1, n2 = map(int, input().split())
    arr1 = [list(map(int, input().split())) for _ in range(n1)]
    arr2 = [list(map(int, input().split())) for _ in range(n2)]

    arr2_cp = [[0] * n2 for _ in range(len(arr2[0]))]

    for i in range(len(arr2)):
        for j in range(len(arr2)):
            arr2_cp[i][j] = arr2[j][i]

    res = [[0] * n1 for _ in range(len(arr1[0]))]

    # for i in range(len(arr1)):
    #     for j in range(len(arr2_cp)):


    print(f'#{tc}')
    print(res)