def func(n: int):
    if n<=0:
        return 0
    else:
        return (n//2) + func(n-1)
    
print(func(8))