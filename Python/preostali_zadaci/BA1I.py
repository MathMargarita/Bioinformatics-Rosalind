"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find the Most Frequent Words with Mismatches in a String
Rosalind ID: BA1I
URL: http://rosalind.info/problems/ba1i
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

def NumberToPattern(number, k):
    pattern = ""
    D = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    q = number
    for i in range(0, k):
        r = q % 4
        q = q // 4
        pattern=pattern+D[r]
    return(pattern[::-1])

def FindingFrequentWordsWithMismatchesBySorting(Text, k, d):
    FrequentPatterns=[]
    Neighborhoods=[]
    for i in range(0,len(Text)-k+1):
        Neighborhoods.append(Neighbors(kmer(Text,i,k),d))
    NeighborhoodArray=[]
    for hood in Neighborhoods:
        for n in hood:
            NeighborhoodArray.append(n)
    Index=[0]*(len(NeighborhoodArray))
    Count=[0]*(len(NeighborhoodArray))
    for i in range (0,len(NeighborhoodArray)):
        Pattern=NeighborhoodArray[i]
        Index[i]=PatternToNumber(Pattern)
        Count[i]=1
    SortedIndex=sorted(Index)
    for i in range (0,len(NeighborhoodArray)-1):
        if SortedIndex[i]==SortedIndex[i+1]:
            Count[i+1]=Count[i]+1
    maxCount=max(Count)
    for i in range (0,len(NeighborhoodArray)):
        if Count[i]==maxCount:
            Pattern=NumberToPattern(SortedIndex[i],k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

if __name__ == '__main__':
    x = '''ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d = int(inlines[2])
    res=FindingFrequentWordsWithMismatchesBySorting(text,k,d)
    print(" ".join(res))

    x = '''CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC
10 2'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d = int(inlines[2])
    res=FindingFrequentWordsWithMismatchesBySorting(text,k,d)
    print(" ".join(res))

    x = '''CACGTGGGCCGCAGTCACCAGAACCCTGAAGTAGAACGACAGACAGAACCCCGCAGTCACCACGTGGGCCGCAGTCACACGACAGACAGAACCCCACGTGGGCTGAAGTAGAACGACAGACAGAACCCCAGAACCCACGACAGACACGTGGGCCGCAGTCACACGACAGACGCAGTCACCGCAGTCACTGAAGTAGACAGAACCCCACGTGGGCCAGAACCCCGCAGTCACTGAAGTAGACACGTGGGCTGAAGTAGACAGAACCCCACGTGGGCCAGAACCCACGACAGAACGACAGACGCAGTCACACGACAGATGAAGTAGACACGTGGGCCGCAGTCACCAGAACCCTGAAGTAGACGCAGTCACTGAAGTAGACAGAACCCTGAAGTAGAACGACAGATGAAGTAGACGCAGTCACCACGTGGGCTGAAGTAGATGAAGTAGACAGAACCCCGCAGTCACACGACAGACAGAACCCTGAAGTAGACACGTGGGCACGACAGACGCAGTCACCGCAGTCACACGACAGAACGACAGACGCAGTCACACGACAGACACGTGGGCACGACAGACACGTGGGCCACGTGGGCTGAAGTAGAACGACAGACACGTGGGCTGAAGTAGACGCAGTCACCAGAACCCACGACAGACGCAGTCACCAGAACCCTGAAGTAGACACGTGGGCACGACAGACAGAACCCCAGAACCCCACGTGGGCACGACAGACAGAACCCTGAAGTAGACACGTGGGCACGACAGATGAAGTAGATGAAGTAGACACGTGGGCCAGAACCCCGCAGTCACCAGAACCCACGACAGA
6 3'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    d = int(inlines[2])
    res=FindingFrequentWordsWithMismatchesBySorting(text,k,d)
    print(" ".join(res))