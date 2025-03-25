import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    stack = []
    res = 'true'
    for w in s:
        if not stack:
            stack.append(w)
            continue

        if w == '(':
            stack.append(w)

        elif w == ')' and stack:
            stack.pop(-1)

        elif w == ')' and not stack:
            res = 'false'
            break

    if stack and res == 'true':
        res = 'false'

    print(res)