

def fib(n: int):
    if n <= 1:
        return n

    map = {0: 0, 1: 1}
    for i in range(2, n + 1):
        map[0] = map[i - 2]
        map[1] = map[i - 1]
        
    
    return map[0] + map[1]

print(fib(3))
print(fib(8))

