def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0: #added equals sign
                return False
        return True #removed 1 indent