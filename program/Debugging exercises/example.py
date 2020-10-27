def tailRecursion(factorial, result = 1):
    if factorial == 1:
        return result
    else:
        tempResult = factorial * result
        return tailRecursion((--factorial), tempResult)