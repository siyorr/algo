import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    res = 0

    stack = []

    if len(s) % 2:
        break

    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
            continue

        if s[i] == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(s[i])

    if stack:
        res = 0
    else:
        res = 1


    print(f'#{tc}')
    print(res)