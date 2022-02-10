def decimal_to_binary(num):
    highest_power = 1
    while 2 ** (highest_power +1) <= num:
        highest_power += 1
    binary_num = 0
    while highest_power > -1:
        print(str(num) + "- 2^" + str(highest_power))
        if 2 ** highest_power > num:
            # add a 0 at this place. will never be true first iteration
            binary_num = binary_num * 10
        else:
            # add a 1 at this place. Subtract num.
            binary_num = binary_num * 10 + 1
            num = num - 2 ** highest_power
        highest_power -= 1
        print("binary num: " + str(binary_num))
    return binary_num


if __name__ == "__main__":
    #print(decimal_to_binary(5))
    print(decimal_to_binary(43))