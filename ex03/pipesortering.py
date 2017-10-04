#!/usr/bin/python3
from sys import stdin
import math

def get_digit(number, base, pos):
  return (number // base ** pos) % base

def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array

def radixsort(l, base=10):
  passes = int(math.log10(max(l))+1)
  output = [0] * len(l)
  for pos in range(passes):
    count = [0] * base
    for i in l:
      digit = get_digit(i, base, pos)
      count[digit] +=1
    count = prefix_sum(count)
    for i in reversed(l):
      digit = get_digit(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i
    l = list(output)
  return output

def find_lower_index(A, target):
     min = 0
     max = len(A)-1
     prev_val = -1
     while(True):
        mid = (min+max) // 2
        mid_val = A[mid]
        #print("mid_val=", mid_val,"mid=",mid, "min=", min, "max=", max)
        if(mid_val == target):
            return mid_val
        if(min >= max and prev_val > -1): # Target value not in list, return closest higher value
            if(mid > 0): # boundary condition, start of list
                return A[mid-1]
            else:
                return A[mid]
        else:
            if(A[mid] > target):
                max = mid-1
                prev_val = A[mid]
            else:
                min = mid+1
                prev_val = A[mid]

def find_upper_index(A, target):
     min = 0
     max = len(A)-1
     prev_val = 0
     while(True):
        mid = (min+max) // 2
        mid_val = A[mid]
        #print("mid_val=", mid_val,"mid=",mid, "min=", min, "max=", max)
        if(mid_val == target): # target = value of first try
            return mid_val
        if(min >= max and prev_val > -1): # Target value not in list, return closest higher value
            if(max > len(A)-2): # boundary condition, end of list
                return A[max]
            else:
                return A[max+1]
        else:
            if(A[mid] > target): # continue on right tree
                max = mid-1
                prev_val = A[mid]
            else: # continue on left tree
                min = mid+1
                prev_val = A[mid]

def sort_list(A):
    return radixsort(A)

def find(A, lower, upper):
    return (find_lower_index(A,lower),find_upper_index(A,upper))

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)
    print(sorted_list)
    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
