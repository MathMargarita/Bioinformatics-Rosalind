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

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def kmerswithapproxcount(text,k,d):
    D=dict()
    for window in Lwindows(text,k):
        for pattern in Neighbors(window,d):
            D[pattern]=ApproximatePatternCount(text,pattern,d)
    return D

def mostfrequentapproxkmers(text, k,d):
    D = kmerswithapproxcount(text,k,d)
    maxcount = max(D.values())
    return [x[0] for x in D.items() if x[1] == maxcount]

def PatternToNumber(pattern):
    def allkmers(k):
        nucleotides = {'A', 'C', 'G', 'T'}
        kmers = []
        if k == 0:
            return kmers
        if k == 1:
            for n in nucleotides:
                kmers.append(n)
            return kmers
        for x in allkmers(k - 1):
            for n in nucleotides:
                kmers.append(n + x)
        return kmers
    all=allkmers(len(pattern))
    all.sort()
    return (all.index(pattern))

def NumberToPattern(number, k):
    pattern = ""
    D = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    q = number
    for i in range(0, k):
        r = q % 4
        q = q // 4
        pattern=pattern+D[r]
    return(pattern[::-1])

def FrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns=set()
    Close=[]
    FrequancyArray=[]
    for i in range (4**k):
        Close.append(0)
        FrequancyArray.append(0)
    for i in range (len(Text)-k+1):
        Neighborhood=Neighbors(kmer(text,i,k),d)
        for Pattern in Neighborhood:
            index=PatternToNumber(Pattern)
            Close[index]=1
    for i in range (4**k):
        if Close[i]==1:
            Pattern=NumberToPattern(i,k)
            FrequancyArray[i]=ApproximatePatternCount(Text,Pattern,d)
    maxCount=max(FrequancyArray)
    for i in range (4**k):
        if FrequancyArray[i]==maxCount:
            Pattern=NumberToPattern(i,k)
            FrequentPatterns.add(Pattern)
    return FrequentPatterns

if __name__ == '__main__':
    x='''ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d=int(inlines[2])
    #print(" ".join(mostfrequentapproxkmers(text,k,d)))
    #print(" ".join(FrequentWordsWithMismatches(text, k, d)))

    x='''CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC
10 2'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d=int(inlines[2])
    #print(" ".join(mostfrequentapproxkmers(text,k,d)))
    #print(" ".join(FrequentWordsWithMismatches(text, k, d)))


    x='''TGAACGAAATGTCTTCAAGGAATCCAGGAATCCAGTGCCTAGAACGGAACTGAACGAAATGTCTTCATGAACGAAAACGGAACATGTCTTCATGAACGAATGAACGAAAGTGCCTAGAGGAATCCTGAACGAAAGGAATCCAACGGAACAGGAATCCAGGAATCCTGAACGAATGAACGAAATGTCTTCAAACGGAACAGGAATCCAGGAATCCATGTCTTCAATGTCTTCAATGTCTTCAATGTCTTCAAACGGAACAACGGAACAGGAATCCAGTGCCTAGATGTCTTCAAGGAATCCATGTCTTCAAGGAATCCAGGAATCCAGGAATCCATGTCTTCAAACGGAACTGAACGAAAGGAATCCATGTCTTCAAGTGCCTAGAACGGAACATGTCTTCAAGGAATCCAACGGAACATGTCTTCATGAACGAAAGGAATCCATGTCTTCAAGGAATCCTGAACGAAAGTGCCTAGAGGAATCCAACGGAACATGTCTTCAAGTGCCTAGATGTCTTCAAACGGAACAGTGCCTAGAGGAATCCAACGGAACATGTCTTCAATGTCTTCAAGTGCCTAGAACGGAACAGTGCCTAGATGTCTTCATGAACGAAAGTGCCTAGATGTCTTCAATGTCTTCAAACGGAACATGTCTTCAAGTGCCTAGAACGGAACATGTCTTCAAGTGCCTAGAACGGAACAACGGAACTGAACGAAAGGAATCCAGGAATCCATGTCTTCAATGTCTTCATGAACGAATGAACGAAATGTCTTCAAGTGCCTAGATGTCTTCATGAACGAAAACGGAACATGTCTTCAAGGAATCCAGTGCCTAGAACGGAACATGTCTTCA
5 3'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d=int(inlines[2])
    #print(" ".join(mostfrequentapproxkmers(text,k,d)))
    #print(" ".join(FrequentWordsWithMismatches(text, k, d)))

    x='''CGTCCTGTGATCCATCCTATCCATCCTATCCATCCTTGTTAGACCAATCGAGCGTCCTGTGCGTCCTGTGTGTTAGACTGTTAGACCAATCGAGCGTCCTGTGGGGACAGGCTTGTTAGACGGGACAGGCTCAATCGAGTGTTAGACGGGACAGGCTTGTTAGACATCCATCCTCAATCGAGGGGACAGGCTATCCATCCTCAATCGAGGGGACAGGCTCGTCCTGTGCAATCGAGTGTTAGACTGTTAGACTGTTAGACATCCATCCTATCCATCCTGGGACAGGCTGGGACAGGCTATCCATCCTATCCATCCTCAATCGAGTGTTAGACTGTTAGACTGTTAGACCAATCGAGCGTCCTGTGTGTTAGACCGTCCTGTGCAATCGAGCGTCCTGTGTGTTAGACATCCATCCTATCCATCCTCGTCCTGTGGGGACAGGCTCGTCCTGTGATCCATCCTCGTCCTGTGCAATCGAGGGGACAGGCTATCCATCCTATCCATCCTGGGACAGGCTTGTTAGACATCCATCCTCGTCCTGTGGGGACAGGCTGGGACAGGCTATCCATCCTGGGACAGGCTATCCATCCTATCCATCCTGGGACAGGCTGGGACAGGCTGGGACAGGCTATCCATCCTGGGACAGGCTGGGACAGGCTATCCATCCTTGTTAGACATCCATCCTGGGACAGGCTTGTTAGACTGTTAGACCGTCCTGTGCGTCCTGTGGGGACAGGCTCGTCCTGTGGGGACAGGCTCGTCCTGTGATCCATCCTTGTTAGACTGTTAGACGGGACAGGCTATCCATCCTTGTTAGACATCCATCCTATCCATCCTCGTCCTGTGATCCATCCTCAATCGAGATCCATCCTCAATCGAGCAATCGAGGGGACAGGCTGGGACAGGCTTGTTAGACCAATCGAGCAATCGAGTGTTAGACCGTCCTGTGCAATCGAGATCCATCCT
7 3'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d=int(inlines[2])
    #print(" ".join(mostfrequentapproxkmers(text,k,d)))
    print(" ".join(FrequentWordsWithMismatches(text, k, d)))
