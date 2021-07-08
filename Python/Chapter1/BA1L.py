#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem
Problem Title: Implement PatternToNumber
URL: http://rosalind.info/problems/ba1l/
"""


def PatternToNumber(pattern):
    res = 0
    k = 0
    for x in pattern[::-1]:
        if x == "C":
            res = res + 1 * (4**k)
        if x == "G":
            res = res + 2 * (4**k)
        if x == "T":
            res = res + 3 * (4**k)
        k = k + 1
    return(res)


if __name__ == '__main__':

    x='''AGT'''
    inlines=x.split()
    pattern = inlines[0]

    res = PatternToNumber(pattern)
    print(str(res))

    x='''CTTCTCACGTACAACAAAATC'''
    inlines=x.split()
    pattern = inlines[0]

    res = PatternToNumber(pattern)
    print(str(res))

    x='''AACGCTGTGATCCGCACAGTCACGTCACGG'''
    inlines=x.split()
    pattern = inlines[0]

    res = PatternToNumber(pattern)
    print(str(res))
