import sys
sys.stdin = open('input.txt')

def fibo(num):
    fibo_list = [0, 1]
    for i in range(2, num+1):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list[num]

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    res = fibo(n)

    print(f'#{tc}')
    print(res)