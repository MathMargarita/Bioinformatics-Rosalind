"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Generate the Frequency Array of a String
Rosalind ID: BA1K
URL: http://rosalind.info/problems/ba1k
"""
def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def ComputingFrequencies(text, k):
    frequencyArray=[0]*(4**k)
    for i in range(0,len(text)-k+1):
        pattern=kmer(text,i,k)
        j=PatternToNumber(pattern)
        frequencyArray[j]=frequencyArray[j]+1
    return frequencyArray

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

if __name__ == '__main__':
    x="ACGCGGCTCTGAAA\n2"
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    print(ComputingFrequencies(text,k))



