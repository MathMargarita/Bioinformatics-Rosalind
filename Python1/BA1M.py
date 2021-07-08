#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem
Problem Title: Implement NumberToPattern
URL: http://rosalind.info/problems/ba1m/
"""


def NumberToPattern(number, k):
    pattern = ""
    D = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    q = number
    for i in range(0, k):
        r = q % 4
        q = q // 4
        pattern=pattern+D[r]
    return(pattern[::-1])


if __name__ == '__main__':

    #import sys

    #inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    x="45\n4"
    inlines=x.split()
    number = int(inlines[0])
    k = int(inlines[1])

    res = NumberToPattern(number, k)
    print(str(res))
    #sys.stdout.write(str(res))