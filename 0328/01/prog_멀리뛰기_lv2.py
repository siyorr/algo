import sys
sys.stdin = open('input.txt')

T = int(input())

def fibo(c):
    fibo_list = [1, 2]
    for i in range(c):
        fibo_list.append(fibo_list[i] + fibo_list[i+1])
    return fibo_list[c-1] % 1234567

for tc in range(1, T+1):
    n = int(input())

    ans = fibo(n)



    print(f'#{tc}')
    print(ans)