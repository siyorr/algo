import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    arr = list(input().split())
    for i in range(len(arr)):
        arr[i] = list(arr[i])

    flag_i, flag_j = [], []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '#':
                flag_i.append(i)
                flag_j.append(j)

    flag_i.sort()
    flag_j.sort()

    result = [flag_i[0], flag_j[0], flag_i[-1]+1, flag_j[-1]+1]

    print(f'#{tc}')
    print(result)
    print('--------')