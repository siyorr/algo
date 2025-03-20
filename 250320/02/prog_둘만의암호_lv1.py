import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    skip = input()
    index = int(input())

    abc = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z'
    ]

    ans = ''

    for w in s:
        n = abc.index(w)
        i = 1
        cnt = 0
        while cnt != index:
            k = n+i
            if k > 25:
                k -= 26
            if abc[k] in skip:
                i += 1
                continue
            i += 1
            cnt += 1
        k2 = n + i - 1
        if k2 > 25:
            k2 -= 26
        ans += abc[k2]

    print(ans)

