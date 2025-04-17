import sys
from copy import deepcopy

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    want = list(input().split(', '))
    number = list(map(int, input().split()))
    discount = list(input().split(', '))
    for i in range(len(discount)):
        discount[i] = discount[i].replace('"', '')

    res = 0

    com = []
    for i in range(len(want)):
        com += [want[i]] * number[i]
    com.sort()


    for i in range(len(discount)-9):
        com2 = deepcopy(discount[i:i+10])
        com2.sort()

        if com == com2:
            res += 1


    print(f'#{tc}번 케이스')
    print(res)