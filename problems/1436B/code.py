def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
 
def generate_prime_square(n):
    p = n
    while True:
        if is_prime(p) and not is_prime(p - (n - 1)):
            break
        p += 1
    
    row = [1] * n
    row[0] = p - (n - 1)
    
    square = []
    for i in range(n):
        square.append(row[i:] + row[:i])
    return square
 
t = int(input())
for _ in range(t):
    n = int(input())
    grid = generate_prime_square(n)
    for row in grid:
        print(' '.join(map(str, row)))
