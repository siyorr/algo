import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    w = int(input())
    num = int(input())

    res = 0
    box = []
    for i in range(1, n+1, w):
        tmp = []
        if (i // w) % 2 == 0:
            for j in range(i, i+w):
                if j > n:
                    tmp.append(0)
                else:
                    tmp.append(j)
            box.append(tmp)
        else:
            for j in range(i+w-1, i-1, -1):
                if j > n:
                    tmp.append(0)
                else:
                    tmp.append(j)
            box.append(tmp)

    x,y = 0, 0
    for i in range(len(box)):
        for j in range(len(box[i])):
            if box[i][j] == num:
                x, y = i, j
                break

    if box[-1][y] == 0:
        res = len(box) - x - 1
    else:
        res = len(box) - x

    print(f'#{tc}')
    print(res)