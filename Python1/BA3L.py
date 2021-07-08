"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Construct a String Spelled by a Gapped Genome Path
Rosalind ID: BA3L
URL: http://rosalind.info/problems/ba3l/
"""

def GappedPatterns(Patterns):
    gappedPatterns=[]
    for pattern in Patterns:
        pat=pattern.split('|')
        gappedPatterns.append([pat[0],pat[1]])
    return gappedPatterns

def stringSpelledByGappedPatterns(GappedPatterns,k,d):
    firstPatterns=[pair[0] for pair in GappedPatterns]
    secondPatterns=[pair[1] for pair in GappedPatterns]
    prefixString=stringSpelledByPatterns(firstPatterns, k)
    suffixString=stringSpelledByPatterns(secondPatterns, k)
    for i in range(k + d + 1, len(prefixString)):
        if prefixString[i] != suffixString[i-k-d]:
            return 'there is no string spelled by the gapped patterns'
    return prefixString+suffixString[-(k+d):]

def stringSpelledByPatterns(patterns,k):
    string=patterns[0]
    for x in patterns[1:]:
        string=string+x[-1]
    return string

if __name__ == '__main__':

    x='''4 2
GACC|GCGC
ACCG|CGCC
CCGA|GCCG
CGAG|CCGG
GAGC|CGGA'''
    inlines = x.split()
    k=int(inlines[0])
    d = int(inlines[1])
    res = stringSpelledByGappedPatterns(GappedPatterns(inlines[2:]),k,d)
    print(res)
    print(res=='GACCGAGCGCCGGA')
