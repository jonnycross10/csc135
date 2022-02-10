def count_unique(a, b, c):
    lst = [a,b,c]
    unique = 1
    while len(lst) > 1:
        tmp = lst.pop()
        if tmp not in lst:
            unique += 1
        print(str(tmp) + ": " + str(unique))
    return unique
print(count_unique(1,2,3))
print(count_unique(1,1,3))
print(count_unique(1,1,1))