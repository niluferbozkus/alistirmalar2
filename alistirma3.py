def carpim(n):
    if n==1:
        return 1
    else:
        return n * carpim(n-1)
