"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find All Occurrences of a Pattern in a String
Rosalind ID: BA1D
URL: http://rosalind.info/problems/ba1d/
"""


def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]


def patternposition(text, pattern):
    p=list()
    np = len(pattern)
    for i in range(0, len(text) - np + 1):
        if kmer(text, i, np) == pattern:
            p.append(i)
    return p


if __name__ == '__main__':
    x="ATAT\nGATATATGCATATACTT"
    inlines = x.split()
    pattern = inlines[0]
    text = inlines[1]

    res = patternposition(text, pattern)

    print(str(res))