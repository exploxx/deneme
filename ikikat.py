def bin(n):
    if n==0:
       return 1

    return 2*bin(n-1)