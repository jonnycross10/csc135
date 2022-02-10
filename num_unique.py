def num_unique_values(l):
    tmp = []
    for x in range(0,len(l)):
        x = l.pop(0)
        if x not in tmp:
            #if x isn't unique
            print(x)
            tmp.append(x)
        else:
            continue
    return(len(tmp))

if __name__ == "__main__":
    print(num_unique_values([3, 7, 3, -1, 2, 3, 7, 2, 15, 15]))