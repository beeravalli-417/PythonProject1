#n = 5
#for i in range(1, n+1):
 #   print(" " * (n - i) + "*" * (2 * i - 1))
#for i in range(n-1, 0, -1):
 #   print(" " * (n - i) + "*" * (2 * i - 1))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))  # True
