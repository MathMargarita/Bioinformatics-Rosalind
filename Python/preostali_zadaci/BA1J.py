"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find Frequent Words with Mismatches and Reverse Complements
Rosalind ID: BA1J
URL: http://rosalind.info/problems/ba1j
"""

def suffix(pattern):
    #substring of pattern without first letter
    return pattern[1:]

def HammingDistance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1

    dist = 0
    #zip(AB,CD) gives (('A','C'),('B','D'))
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1

    return dist

def Neighbors(pattern,d):
    nucleotides={'A','C','G','T'}
    if d==0:
        return {pattern}
    if len(pattern)==1:
        return nucleotides
    neighborhood=set()
    suffixNeighbors=Neighbors(suffix(pattern),d)
    for x in suffixNeighbors:
        if (HammingDistance(suffix(pattern),x)<d):
            for n in nucleotides:
                neighborhood.add(n+x)
        else:
            neighborhood.add(pattern[0]+x)
    return neighborhood

def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def complement(text):
    """complement of text"""
    compl=""
    nt = len(text)
    for i in range (0,nt):
        if text[i]=="G":
            compl=compl+"C"
        if text[i]=="C":
            compl=compl+"G"
        if text[i]=="A":
            compl=compl+"T"
        if text[i]=="T":
            compl=compl+"A"
    return compl

def reverse(text):
    """reverse of text"""
    return text[::-1]


def FindingFrequentWordsWithMismatchesAndReverseComplementBySorting(Text, k, d):
    FrequentPatterns=[]
    Neighborhoods=[]
    for i in range(0,len(Text)-k+1):
        Neighborhoods.append(Neighbors(kmer(Text,i,k),d))
    NeighborhoodDict=dict()
    for hood in Neighborhoods:
        for n in hood:
            if n in NeighborhoodDict.keys():
                NeighborhoodDict[n]+=1
            else:
                NeighborhoodDict[n]=1

    NeighborhoodDictNew=NeighborhoodDict.copy()
    for key in NeighborhoodDict.keys():
        if reverse(complement(key)) in NeighborhoodDict.keys():
            NeighborhoodDictNew[key]+=NeighborhoodDict[reverse(complement(key))]

    maxCount=max(NeighborhoodDictNew.values())
    for key in NeighborhoodDictNew:
        if NeighborhoodDictNew[key]==maxCount:
            FrequentPatterns.append(key)
    return FrequentPatterns

if __name__ == '__main__':
    x = '''ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d = int(inlines[2])
    res=FindingFrequentWordsWithMismatchesAndReverseComplementBySorting(text,k,d)
    print(" ".join(res))

    x = '''CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT
9 3'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d = int(inlines[2])
    res=FindingFrequentWordsWithMismatchesAndReverseComplementBySorting(text,k,d)
    print(" ".join(res))

    x = '''TTGACCGGGTCCCATTCATTGTACTTGACCGGTTGACCGGTTGACCGGTCATTGTACTTGACCGGTCATTGTACTCATTGTACGTCCCATTCATTGTACGTCCCATGTCCCATGCGGTCATTTGACCGGGTCCCATTTGACCGGGTCCCATGTCCCATTCATTGTACTTGACCGGTTGACCGGGTCCCATTCGACGAGTCGACGAGTCGACGAGGTCCCATTCATTGTACTCGACGAGTCGACGAGTCGACGAGTCGACGAGTCATTGTACTCATTGTACTCATTGTACTCGACGAGGCGGTCATGCGGTCATGCGGTCATTTGACCGGGTCCCATTTGACCGGTCATTGTACTCATTGTACTTGACCGGGCGGTCATGCGGTCATTTGACCGGGTCCCATTCGACGAGTTGACCGGTTGACCGGTTGACCGGTTGACCGGGTCCCATGCGGTCATGCGGTCATTCGACGAGTCGACGAGGCGGTCATTTGACCGGGCGGTCATTTGACCGGGTCCCATGCGGTCATTTGACCGGTCATTGTACGTCCCATTCATTGTACGCGGTCATGCGGTCATTCATTGTACGTCCCATTCGACGAGTCGACGAGTCGACGAGGTCCCATGTCCCATGTCCCATGTCCCATTCATTGTACTCATTGTACTCATTGTACGCGGTCATTTGACCGGTTGACCGGGCGGTCATTCATTGTACTCGACGAGTCGACGAGTCGACGAGTCATTGTACGTCCCATTCATTGTACTCGACGAGGTCCCATTTGACCGGGCGGTCATTTGACCGGGTCCCATTCGACGAGTCGACGAGTCGACGAGGCGGTCAT
7 3'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d = int(inlines[2])
    res=FindingFrequentWordsWithMismatchesAndReverseComplementBySorting(text,k,d)
    print(" ".join(res))

    x = '''GACCCGCATGGGAGCATGGGAGCTGAGAAAACTTGCAGTATGGGAGCATGGGAGCATGGGAGCGACCCGCATGGGAGCTGAGAAAACTTGCAGTATGGGAGCTGAGAAAAGACCCGCTGAGAAAAATGGGAGCGACCCGCGACCCGCAATCCGGTTGAGAAAACTTGCAGTATGGGAGCATGGGAGCGACCCGCCTTGCAGTTGAGAAAATGAGAAAATGAGAAAAAATCCGGTAATCCGGTGACCCGCAATCCGGTTGAGAAAATGAGAAAAGACCCGCATGGGAGCTGAGAAAAGACCCGCAATCCGGTCTTGCAGTATGGGAGCCTTGCAGTATGGGAGCAATCCGGTCTTGCAGTTGAGAAAATGAGAAAATGAGAAAAATGGGAGCATGGGAGCATGGGAGCTGAGAAAAATGGGAGCCTTGCAGTTGAGAAAAATGGGAGCAATCCGGTAATCCGGTAATCCGGTATGGGAGCCTTGCAGTGACCCGCTGAGAAAAATGGGAGCGACCCGCCTTGCAGTAATCCGGTGACCCGCAATCCGGTAATCCGGTTGAGAAAAAATCCGGTATGGGAGCGACCCGCTGAGAAAAAATCCGGTCTTGCAGTTGAGAAAATGAGAAAAGACCCGCAATCCGGTATGGGAGCATGGGAGCATGGGAGCCTTGCAGTTGAGAAAAGACCCGCTGAGAAAAAATCCGGTAATCCGGTCTTGCAGTTGAGAAAAATGGGAGCCTTGCAGTATGGGAGCGACCCGCGACCCGCATGGGAGCATGGGAGCCTTGCAGTATGGGAGCTGAGAAAATGAGAAAA
6 3'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d = int(inlines[2])
    res=FindingFrequentWordsWithMismatchesAndReverseComplementBySorting(text,k,d)
    print(" ".join(res))

    x = '''ACCCGCGACCCGCGACAGTAAGCGAAGTGACCCGCGGCACGCCCTGCACGCCCTACAGTAAGACAGTAAGCCAGAGTCTCCAGAGTCTGCACGCCCTGCACGCCCTACCCGCGACAGTAAGGCACGCCCTCGAAGTGGCACGCCCTACAGTAAGACAGTAAGGCACGCCCTGCACGCCCTACAGTAAGCGAAGTGCCAGAGTCTCGAAGTGACCCGCGCCAGAGTCTACAGTAAGGCACGCCCTACCCGCGGCACGCCCTGCACGCCCTCCAGAGTCTACCCGCGCCAGAGTCTGCACGCCCTGCACGCCCTGCACGCCCTACAGTAAGACCCGCGCGAAGTGACAGTAAGCGAAGTGACCCGCGGCACGCCCTACAGTAAGACCCGCGCGAAGTGGCACGCCCTACAGTAAGACAGTAAGCCAGAGTCTACCCGCGACCCGCGACCCGCGCGAAGTGACCCGCGACAGTAAGACCCGCGCCAGAGTCTACAGTAAGGCACGCCCTGCACGCCCTCGAAGTGCGAAGTGACAGTAAGCCAGAGTCTACAGTAAGGCACGCCCTACAGTAAGACCCGCGCCAGAGTCTACCCGCGCCAGAGTCTACAGTAAGCGAAGTGACCCGCGCCAGAGTCTCCAGAGTCTCCAGAGTCTACAGTAAGCGAAGTGCGAAGTGCCAGAGTCTCCAGAGTCTCGAAGTGCGAAGTGACCCGCGGCACGCCCTCCAGAGTCTCCAGAGTCTACAGTAAGACCCGCGACAGTAAGGCACGCCCTGCACGCCCTGCACGCCCTGCACGCCCTGCACGCCCTCCAGAGTCTGCACGCCCTACCCGCG
6 3'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d = int(inlines[2])
    res = FindingFrequentWordsWithMismatchesAndReverseComplementBySorting(text, k, d)
    print(" ".join(res))