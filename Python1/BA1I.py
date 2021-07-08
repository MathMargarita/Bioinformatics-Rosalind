"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find the Most Frequent Words with Mismatches in a String
Rosalind ID: BA1I
URL: http://rosalind.info/problems/ba1i
"""
def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

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

def ApproximatePatternCount(text,pattern,d):
    count=0
    for i in range (0,len(text)-len(pattern)+1):
        pattern2=kmer(text,i,len(pattern))
        if (HammingDistance(pattern,pattern2)<=d):
            count=count+1
    return count

def suffix(pattern):
    #substring of pattern without first letter
    return pattern[1:]

def Neighbours(pattern,d):
    nucleotides={'A','C','G','T'}
    if d==0:
        return {pattern}
    if len(pattern)==1:
        return nucleotides
    neighborhood=set()
    suffixNeighbors=Neighbours(suffix(pattern),d)
    for x in suffixNeighbors:
        if (HammingDistance(suffix(pattern),x)<d):
            for n in nucleotides:
                neighborhood.add(n+x)
        else:
            neighborhood.add(pattern[0]+x)
    return neighborhood

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def kmerswithapproxcount(text,k,d):
    D=dict()
    for window in Lwindows(text,k):
        for pattern in Neighbours(window,d):
            D[pattern]=ApproximatePatternCount(text,pattern,d)
    return D

def mostfrequentapproxkmers(text, k,d):
    D = kmerswithapproxcount(text,k,d)
    maxcount = max(D.values())
    return [x[0] for x in D.items() if x[1] == maxcount]

if __name__ == '__main__':
    x="ACGTTGCATGTCGCATGATGCATGAGAGCT\n4 1"
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d=int(inlines[2])
    print(mostfrequentapproxkmers(text,k,d))