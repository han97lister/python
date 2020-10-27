def product(n):
    total = 1 #removed one equal sign
    for i in n: #changed n to i
        total *= i
    return total #added indent

print(product([4,4,5]))