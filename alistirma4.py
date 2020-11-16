#[1 1 2 3 5 8 13 ...]

def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-2)+fibo(n-1)
