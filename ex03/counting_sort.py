#!/usr/bin/python3
from sys import stdin
import math

def counting_sort(A):
    k = max(A)+1
    C = [0] * k
    B = [0] * len(A)
    for j in range(0,len(A)):
        C[A[j]] = C[A[j]] + 1
    # C[i] now contains the number of elements equal to i
    for i in range(1,k): # l-1 to get k=largest number in input
        C[i] = C[i] + C[i-1]
    # C[i] now contains the number of elements less than or equal to i
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1
    return B

def radix_sort(A):
    print(A[0])
    d = int(math.log10(max(A)))+1
    print(d)


def sort_list(A):
    sorted_list = radix_sort(A)
    sorted_list = A
    return sorted_list


def find(A, lower, upper):
    # Binært søk
    print(" ")
    #print("A=",A, "lower=",lower, "upper=",upper)

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))
    sorted_list = sort_list(input_list)
    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        #print(str(result[0]) + " " + str(result[1]))
    counting_sort(input_list)


if __name__ == "__main__":
    main()
