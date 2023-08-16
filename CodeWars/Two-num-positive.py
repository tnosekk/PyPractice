def two_are_positive(a, b, c):
    list = [a, b, c]
    count = 0
    for positive in list:
        if positive > 0:
            count += 1
    return count == 2
