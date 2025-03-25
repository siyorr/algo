import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    skip = input()
    index = int(input())

    # 실패1
    # abc = [
    #     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    #     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    #     'w', 'x', 'y', 'z'
    # ]
    #
    # ans = ''
    #
    # for w in s:
    #     n = abc.index(w)
    #     i = 1
    #     cnt = 0
    #     while cnt != index:
    #         k = n+i
    #         if k > 25:
    #             k -= 26
    #         if abc[k] in skip:
    #             i += 1
    #             continue
    #         i += 1
    #         cnt += 1
    #     k2 = n + i - 1
    #     if k2 > 25:
    #         k2 -= 26
    #     ans += abc[k2]
    #
    # print(ans)


    # 실패2
    # abc = [
    #     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    #     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    #     'w', 'x', 'y', 'z'
    # ]
    #
    # ans = ''
    #
    # for w in s:
    #     k = abc.index(w)
    #     k_ = abc.index(w) + index
    #     tmp_list = []
    #     if k_ > 25:
    #         k_ -= 26
    #         tmp_list = abc[k+1:] + abc[:k_+1]
    #     else:
    #         tmp_list = abc[k+1:k_+1]
    #
    #     cnt = 0
    #     for skip_word in skip:
    #         if skip_word in tmp_list:
    #             cnt += 1
    #
    #     new_k = k_+cnt
    #     if new_k > 25:
    #         new_k -= 26
    #
    #     ans += abc[new_k]
    #
    # print(ans)

    abc = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z'
    ]

    ans = ''
    for skip_word in skip:
        abc.pop(abc.index(skip_word))
    # 나머지 연산을 통한 로테이션!!!
    for w in s:
        k = (abc.index(w) + index) % len(abc)
        ans += abc[k]

    print(ans)