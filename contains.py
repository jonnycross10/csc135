def contains(a1,a2):
    a1_len = len(a1)
    a2_len = len(a2)
    for i in range(0,a1_len):
        x =a2
        y = a1[i:a2_len+i]
        #print(x + ": " + y)
        if x == y:
            return True
    return False


if __name__ == "__main__":
    a1 = [1,6,2,1,4,1,2,1,8]
    a2 = [1,2,1]
    print(contains(a1,a2))