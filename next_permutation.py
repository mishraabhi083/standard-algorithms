#!/bin/python3
from math import inf
import itertools
import string
def biggerIsGreater(w):
    def calculateHash(string, dataset):
        hashcode = 0
        hashfactor = 0
        for i in string[::-1]:
            hashcode += (dataset[i] * (26**hashfactor))
            hashfactor += 1
        return hashcode
    dataset = {}
    for x, y in zip(string.ascii_lowercase,
                    range(1,
                          len(string.ascii_lowercase) + 1)):
        dataset[x] = y
    initialHashCode = calculateHash(w, dataset)
    word="no answer"
    currentMaxHash=inf
    for i in itertools.permutations(w):
        temp_word="".join(i)
        h=calculateHash(temp_word,dataset)
        if h > initialHashCode and h < currentMaxHash:
            currentMaxHash=h
            word=temp_word
    return word
if __name__ == '__main__':
    T = int(input())
    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)

    