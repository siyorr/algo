import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    today = input()
    terms = list(input().split(','))
    privacies = list(input().split(','))

    result = []
    terms_dict = {}
    for i in range(len(terms)):
        terms[i] = list(terms[i].split())
        terms_dict[terms[i][0]] = int(terms[i][1])

    for i in range(len(privacies)):
        privacies[i] = list(privacies[i].split())

    for i in range(len(privacies)):
        yy, mm, dd = map(int, privacies[i][0].split('.'))

        dd -= 1

        if dd == 0:
            mm -= 1
            dd = 28

        yy += terms_dict[privacies[i][1]] // 12
        mm += terms_dict[privacies[i][1]] % 12

        if mm > 12:
            yy += mm // 12
            mm %= 12

        yy = str(yy)

        if mm < 10:
            mm = '0' + str(mm)
        else:
            mm = str(mm)

        if dd < 10:
            dd = '0' + str(dd)
        else:
            dd = str(dd)

        yak = yy + '.' + mm + '.' + dd

        if today > yak:
            print(yak)
            result.append(i+1)


    print(f'#{tc}')
    print(result)
    print('--------')