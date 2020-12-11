def solve(num, base=[]):
    if base == []:
        base = ['9' + '0' * (len(str(num)) - 1)]
    while base != []:
        # print(base[0])
        if int(base[0]) % num == 0: return int(base.pop(0))
        else:
            last = base.pop(0)
            base = (base + [last + '0'] + [last + '9'])


if __name__ == "__main__":
    print(f'least num is {solve(int(input("Enter num to test: ")))}')