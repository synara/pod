def isprime(n):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    return prime

def isprime2(n):
    prime = True

    j = n // 2
    for i in range(2, j):
        if n % i == 0:
            prime = False
            break

    return prime

def isprime3(n):
    prime = True

    j = int(math.sqrt(n))
    for i in range(2, j):
        if n % i == 0:
            prime = False
            break

    return prime


if __name__ == '__main__' :
    print(isprime(2))