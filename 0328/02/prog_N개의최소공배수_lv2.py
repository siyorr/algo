import sys
sys.stdin = open('input.txt')

# def yaksu(num):
#     ret = []
#     for a in range(2, num):
#         if num % a == 0:
#             ret.append(a)
#     return ret

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    # answer = 1
    # n = 2
    # n_list = []
    #
    # for i in range(len(arr)):
    #     yaksu_list = yaksu(arr[i])
    #     for j in range(len(arr)):
    #         if arr[j] in yaksu_list:
    #             arr[j] //= arr[j]
    #
    # arr = [i for i in arr if i != 1]
    #
    # while True:
    #     if max(arr) < n:
    #         break
    #     for i in range(len(arr)):
    #         if arr[i] % n != 0:
    #             break
    #     else:
    #         for j in range(len(arr)):
    #             arr[j] //= n
    #         n_list.append(n)
    #     n += 1
    #
    # for i in range(len(n_list)):
    #     answer *= n_list[i]
    #
    # for i in range(len(arr)):
    #     answer *= arr[i]

    arr.sort()
    for i in range(len(arr)-1):
        n = 2
        n_list = []
        tmp = 1
        while True:
            if arr[i+1] <= n:
                break
            if arr[i] % n == 0 and arr[i+1] % n == 0:
                n_list.append(n)
            n += 1
        for j in range(len(n_list)):
            tmp *= n_list[j]
        arr[i+1] = (arr[i] * arr[i+1]) // tmp

    print(f'#{tc}')
    print(arr[-1])