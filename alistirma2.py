def toplam(n):
    if n==1:
        return 1

    else:
        return n + toplam(n-1)
