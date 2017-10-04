#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict
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

def flexradix(A, d):
    return radixsort(A)


def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()
