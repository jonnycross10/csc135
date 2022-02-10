def count_quarters(num):
    # only take last 2 digits
    num = int(str(num)[-2:])
    print(num)
    quarters = 0
    while num >= 25:
        num -= 25
        quarters += 1
    return quarters

print(count_quarters(170))