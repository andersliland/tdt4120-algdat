#!/usr/bin/python3
from sys import stdin
from itertools import repeat


def merge(decks):
    while len(decks) > 1:
        L = decks.pop(0)
        R = decks.pop(0)
        result = []
        i = 0
        k = 0
        # MergeSort the lists L and R until on of them reach its end
        # Assumption: L and R are always sorted internaly
        while( len(L) > i and len(R) > k):
            if L[i][0] < R[k][0]:
                result.append(L[i])
                i += 1
            else:
                result.append(R[k])
                k += 1
        if i >= len(L):
            result.extend(R[k::])
        else:
            result.extend(L[i::])
        decks.append(result)

    word = ""
    for characters in result:
        word += characters[1] # index character in tuple pairs
    return word


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))



if __name__ == "__main__":
    main()
