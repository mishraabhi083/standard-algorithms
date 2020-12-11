def hash_generate(s):
    hash = 0
    for i in range(len(s)):
        hash += ord(s[i]) * (len(s)**(i))
    return hash


def search_pattern(data, pat):
    res = []
    p = hash_generate(pat)
    last_hash = hash_generate(data[0:len(pat)])
    for i in range(len(data) - len(pat) + 1):
        print(last_hash)
        rolling_factor = (ord(data[len(pat) + i - 1]) - ord(data[i - 1]))
        last_hash += rolling_factor
        if last_hash == p:
            print(f'schoric hit for {p} at {i}')
            flag = True
            for x, y in zip(pat, data[i:i + len(pat)]):
                if x != y:
                    flag = False
            if flag: res.append(i)
    return res


if __name__ == "__main__":
    print(search_pattern(input("Enter string : "), input("Enter pattern : ")))
