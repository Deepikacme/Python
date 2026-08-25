def check_prime(n):
    if n<2:
        return"Not Prime"
    for i in range(2,n):
        if n%i==0:
            return"Not Prime"
        return"Prime"
print(check_prime(7))