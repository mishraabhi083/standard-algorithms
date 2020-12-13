# References :
# https://www.geeksforgeeks.org/python-ways-to-find-all-permutation-of-a-string/
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
def recursive_permutation_generator(s):
    if len(s)==1:return s
    else:
        for i in range(len(s)):
            s[0],s[i]=s[i],s[0]
            print("".join(s))
            recursive_permutation_generator(s[1:])
            s[0],s[i]=s[i],s[0]
            
if __name__ == "__main__":
    recursive_permutation_generator(list(
        "ABC"
    ))
