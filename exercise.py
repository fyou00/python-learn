def loop(n):
    if n>0:
        loop(n-1)
    return n
        
print("recursive loop: ", loop(5))

print('\n')

def loopfor(n):
    for n in range(n):
        n+=1
        return n

print("loopfor: ", loopfor(5))