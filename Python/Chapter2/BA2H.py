"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement DistanceBetweenPatternAndStrings
Rosalind ID: BA2H
URL: http://rosalind.info/problems/ba2h/
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

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def distanceBetweenPatternAndStrings(Pattern, Dna):
    k=len(Pattern)
    distance=0
    for Text in Dna:
        hammingDistance=len(Pattern)
        for Pattern1 in Lwindows(Text,k):
            if (hammingDistance>HammingDistance(Pattern, Pattern1)):
                hammingDistance=HammingDistance(Pattern, Pattern1)
        distance=distance + hammingDistance
    return distance

if __name__ == '__main__':

    x='''AAA
TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT'''
    inlines=x.split()
    pattern=inlines[0]
    dna=list()
    for i in range(1,len(inlines)):
        dna.append(inlines[i])
    res=distanceBetweenPatternAndStrings(pattern,dna)
    print(res)

    x='''AATTGGG
TCTGCAGAGCGCAAGCGTCTCAATGTTTTTCGCTGCAAGTGTTAGCTGCGTTTGTCGACACACAAATGAAGTGACCACATCAAACCTAATTATG TCCCGCTCGAGGACAGACACCGGTGCAGCCGAGGGTATTATAGTCTGCTCGTATGGTTTGTATGGAGGATAATAGATGGGGTGACGAAATGAGA CCTCCCTGCCAGGTTGGTGAATTTAAGCATAAAGACCTGGAGGACTGACGGGTCTGGTCGACCACCATTCGTCGGTTCTCGAGCGCTGTTTCTA GATACAGGTCGCTTGAAATGTCCCTGAGACGTCCGGGCCAAGAGCGAAACAAATCTCAGTCCTGGGTGGCGGCAGCGAAGGGATTAGATTACTT ATGGAACCGTGTCACGGCAGTCTACCTTTTACCCAGAGCTGTATATGACGGTTAGTCCCCGAGGCCATCTCGCACCCTACTGAGCACAAATATA AATCCCTGCAGGTCAGGCTGTTCTGAAAGAACCCTGCAGGCTGGTGCTATTCCTTAAGACGCCGAGGTTCAGATACTCTCAGCCAGAGAGCAGA CCTATTAACTTCTCTCTAGATCGTAAACGACTATGGACTTACACGTCCCGCTTTCTTGTCTTGGGTGCCGTCACACTAGCCCACTACAGTCGGG GGCGCACCTTCGATATTAATGCGAGTCAATTGCCGTTTAAGTCCGCGCGTAGCGGATGCACGTAGGGACTTTAAAGCCCCATGCCAACTGTATA TCTTGGTTACAATTACCCTCCTGAGCCGATAAGCGCCTCTCAGGCACACTGTGGCAGTTCATCGTGTCCTTCGTCTTATTCCCTGCCCCCAGCA ATCTCAATGCGATATATATGGTCCTGCCTAAAAATAGAGCTAGTGAGCGTGGTGGTATCATTGTTGACTACCCGGGACAGGCGACACCGTACGA ATCTATAGAAACATCTAGCACAGGAACACCCATAAAAACACCACTAGCCGACCTGTTCGTCGGTTTTCCATGCGAATGGTAATATTACGTTTGT ACGCATACGTCAGAAATCTGTGAAAGTACGACGCCCACTGGACCCACGGTCGCTGCGTTCACAATCATTGTGATCCTGGATCCATAACGCCTAA GACCAAGGCCCGAAAGTGTGGCGAGATAAGAAAACCCACTCCATATGACCGTGGATCCCGTGGGAGTCCTCCTTTCATCCCTCTAGCGCTAGAA ATACCCCCGTAGTTTTCGGACTCAAAAAGTATTTATGTGACTTGCAATAGTAGAGACCGGCGTCTTTGCCGCTGTCACCTGCTGTATGATCACC CGATGGTACCCAAGAGTGGTCGGTCTACCAAGCATCGCGACCCGCTTTCGTTCACCAGCCGAGAGTGCCATGTAAGTCAGCAGCTAACACCCTG TGTCTCAAGCATTACTATGGCTGGCCTCGTTATTAGATTCTGCCTAAGCCGCATGGGCGCGTGACCGTGGGCACATTGCCCTGAATTACCCGCC AGGTGCAATTAACTGTACTAAGCTCAAGATCTCAATCCGCAAAGGCCATTCAGGCGACTCCGTGTGGTGCCTATACCGCACAAACGTAGGAGCG CATTAAGACGGATTGGGACCCGCGGGAGAAAGGCGCGTTGGAGCGAGGGGGTCATTTGCACTGCCGAGCAGACGCGTCTAGGTCATCTTCTCTA CCGAAAAGCCCAAAGGTTTTATGCAAGTTCCACGAGAATCGTCGAGCGCTGAGGTACGGCCACCGAATCACAATTCCATTCACATTCGCGGAGT TTTCTTTGGCAGATGTCCTCCGGACTTCCGGAATGAAGCTTCAGGGCGCGCCTATCGCGAAACCCCGACGTGACGGAACGTCCTGTCCTGGACT AGTTGCCCAAGGTTTGGACCTGCCCGGTTTTCTGGCCGCGTATGAAGTATTCCAGTAGATCCCTGCGATACTTCTCGCTACGCTAGGTCCGATA CTCGTAAATAAACGGGATAACAAAGTGTTATCGATTATGTATAGCGGTCAGGGTGTCTGCACTTATCGGAGTCGGGAGGAGACCCTTCCTAAGA CGCTTATGTCGTAAGTATAGCAACTAAGGGGCCATATGAACAAGTGTAGTACACGCGGCACCAGGTACCCTTAGGCGTTGTTCTTCGGAGGTTT CTAAAGACCCCGCGTGGAATTAGAGGGAGCTCCAACGATAGAAATGAAGGAGGGGGCTTGTATAAATCCAACTGAAGGTGAACGAAGCTATAGA CGTTTCCCTACACGGCCAATGAACAGCGGGCGCATAACATCTCTTAGCCCTGACTTCTGCGACGCATATATTTACCGGGACATGATCACAGTGT TTACAGCACAGCAAGAAATTCCGTGCTTGGGGGATCTACCGTGCATACTCCTGAGCCCAGATATTGGCCCGTAAGAATCATGCATTGAAAATAA TGGTCTCACCAGTGGGCACCGCGTATTGTCAGGCAAGAGCAATTAGTGATTCGTACATAGAGGTCTTCAATCTCATGTATAGAGTCGCTGGTTC ATGCACCTAGAAGAACATAGTTAAGAAGCGTCATGGAGCTACAGAGTTCCGTGGCAATGTACAGTAGCTGTTGCCAATTTGTTGGGACTCAGCC AGGTCTCTTCGAAATAGGTAGTGCCGGAACCATACTGAGAGTCTGCAAACGTTGCTTCGGAATGTACCTGTTGAGGACACTACTCTGACGGGCG GCGATCACCCGCGACTCGTTCACTGGTACTTCCAATGCACTGCGCCCAATGCGCAATACGCGAATTCTCTTAAATGATCTCAAATATATGAGCT'''
    inlines=x.split()
    pattern=inlines[0]
    dna=list()
    for i in range(1,len(inlines)):
        dna.append(inlines[i])
    res=distanceBetweenPatternAndStrings(pattern,dna)
    print(res)

    x='''GATATG
ACCACACGATCTCCGATTGAATAAATATAGTGCCTCAAACTTTTCTTTCCGCAATAAACTAAACAGAGTTTCATAACTTATTTGAAAGCGTGCATCACGTTGTCGAA CCTATATATGTTAGTTCAATTGCGCCACAAGCCATCCACGGCGTGATGGCTCGAGATTGGTCTCGTGTGGACAATGTGATTCTGAGGCCAGACCTAGTTTCAAGCAC TAGTAAGCAGCATAGTAAGTGAGCGTTGATCCATATTTTTAGTTCGATGTATCGGGCGTTGCAACTCCACGAAGCGACACCGGTCAGGGCTGGGCCTCCAGGAGAAC ACAGCCACTTTGGATATCGGGGTACTATTACGTCAGAGACTCAGTTATAGCCATAAAGCGCATTATCATGGAAACCTCATCTAACGTATTAATACCCGGCGCTCCGT ATCTTCTGCCCCGACCGTAATTGGTTAAAGACCCTGCGCCCCGTTCACGATACTCGTGTCAACGAAGATAGGCCGAGCACCTGCCAAGCATAAGTGAATCCTTTTCA CTCAAAGCCAACGCTCCAAGGTGACTACGTAATAAGCCGAGAGACCAACCATTCTCTGTATATCATATACTAATATATCACTGATAATCAAAAAGCTATATTATAAT CACGTCACGAATAGTTTAACCCTGCTCCCTGCGCCCCTGAAGCAGGTCAGACATTAGCACCAATTTAACCTTGCTAGGTCAGGAAATCGCCGGTGCTAGCAGCCACA ATTGCTGCATCAAGAATGCGTAGTTCCAGTCACTGTAAGGTGTCCTAAAAAACGTCGCTCAGAGTGGTTTAGAGGCCCGTATCGCAGTTAGAGATAATATTGTAAGA TAACTCTAAAAAAGGCCTCGGGCAGAGGGGACGTGGTTTTCCTCACTTCTGTCTAACTAGGCCAGCGTGCGCTCATTCCTTACTAATTAAGAAATGTGCTTAAAAGT TCATAGTCGCCCTTCTATCCATTTGGGTCCATTACAGGAACTGGAGCGTAATGAGAGCCACAATGTCCTTGGTCCTCGTGCCTGGAATCCAGCGTATTATCGCCGCG AGCGCGCCTGACGCGTTCCACACGTAAAGCTGTAGTGTTGGGGCGTGGGCGGTTGCTAGCTACTTTCCCATAACTAGGGATCATTCTTCATCATTCGCCGCAAATCT GCCGGAGAAGACGAAAAAGTCCCGGTTCATACTGATTCTGACTCCCCCGTCACGCTTACTGAGGCAGACCAGCCGGTTCAGGGCACTCCGCAACCCCACAGTGAAAA CGCTACTTGAGAGGGTTATTAGCTCCCATCGGGCGAGGCTGTTACTAACCACGCAAGTGCGTAAAATGCTTTATGATAACTGTGTTGTCTCCAAACTGGATTGGCTA AACATTATAGGTTCTAGGATGTGACACAGGGATCCTCTGCAAAGATGGGGGTCCCGTTTGGTTCGCTCCTCTTATTTGACACAGGTAGGGGCGAGATCAATGTCAGT CAACACGGGACAGCAACCTCCACTCAGGTATAGGGCCAGGCCTCACGCGTACTTTACAGCCACGCTGTTTGCCAGTGACTGGGCAACAATCCGCTCTACCTTCCTAC GGTGCGCGGTGTCACGATCTAGTTGAGAATCTGCAACTTTAGCCAGCACTTGACTTGCCCCCACTTCCATGCCTAATTACATGAAATCCAATATGAGTTATCGAGGA ATGAACGGGCAATTGTCCGAAGGATCTGCATTTAACGTAAGCTTTCGCTATATGTCATGGTAATACTCTAGAGAAACGGAACGCATGCTTAACTGGCGCCTTAAGGC CCCTCGCATCGGTCAGCTCGCCGTTGGAGCTGGTATTCCGAATGCTCCCCACTGCCAATCGTGATCATCCCAAGGAAAACGGCCGTTACCGTAAAAAATTTCCTCGC CTCCCAACGTTGACGCATCCACCTACATCTTACATATACACGGTACTCCTTTGCCTTTCCGCGGCAGGCACGCCAATGATGGTATAAACGCACAAATACGAACACGC AGGGTCTTTCTATGGTATATCCCATTGAGCCTTTGTTATGCGTCTTCATGCCTTATCGCTTTCCTCTTGCTGCTCCGCGCCCATGAGTAACCCCATATCGGGCGGGT TCATCTATACACTAGATTCGTGTATGCGATCTTTAGATGTCCGGCTAGTTATTCCAGAACTCAATGATTCAGAACCACAACTGATTCTGGTCCTACGGCTCATTGTG ACATGGGCATTCAGCTTGCATCTGCTCCCGGCGCTTCGATCAAGGAACCCGAGGTAGTCACAGAGGAACTTGTTCATGTTCCTCACGTAAAAGGCGTCTACGACACG CGGCACCTAAGTGCGCTGGTATCACCGTTCTAGATGTGCTGTATATGTATCTAAACATCAGCTTCCGTTTGCTCAGTCACGCAGCTGCTACGGTTAACCTTCACCGG TTAATTTCGCGTAGCCGCATTGGAGTGCAATAGGCCACTAGCGCAAACGGTAGTGAAGGGCAGGGAAAATATGCTGTGACTTAGAATGAAGACTCAAAAGTTGGAGG TGAATATGCCTGACTTACGCCCCGAACGATTCCGAATGGATATATCCAAACAATACTGGCAGCACGTCTTATTATAGTAGTTCCATGGAAGTAACGCGGACGGTATA TTGGGGGCAGATCCCGAGGATCGCACTGAAGTGCAAGTTTAGTGTGTTCGGAGTGGGGGATCGGATTTATAAAGCATTGGTGTTGGGCTTTCATTTAGTCGTTTCCG AAAAACTCCTCCTCTGCGTAGGGAGTGTGGATCTCACCGCTCGCAATAAGAACTTGGTTCCGTCACGGTTAGCATGCAGTACCGTAGCCATTCCTTTTTATGGACTG CTCAAACTACTCGCTGGAAGGAACACTACCAGGAAACCGCTCGCAACAACGGCGAACCCCGCAGGTAGCGATCCAGAAAAACCTATGGTAGTCATCGATCGCCTCGG TAGCTTAGCGGCGGTCGCAGTAGAACAAGATGATGCTATAACACGTGGTCCGGACTCCTCAATGACGTACCCCCCAATGACTTCATGTTATACAGATCTTCCAGCGG TCCCGTCACTCGCAAGGATCCGTCTTGAATGCACCTAATGATGTGGGCAACCTTCCGACCAACTCCGCGGCACGCGGAGACCGACAATTCAAAAACGCCGAACGGGA TGAAAAGCCCTGTAGTTTTGATGTCGTGTTCGCTGGCCTCACCACTTCGCCCCCTCTAGCGGTATATCGTGTGAAAGATTGACAGACATGTAGGAGGTACGGGTCGC AAAACAATTATTTTTAGTGTTATTGAGCAAATACACGGTGGAAATGAAACGTGTGCAGAGCCCATTTTCTATGCCCTACGGATGGCGAAGCTAATTGTAATATTAGA ATTACAACGGAAGTCTTTCTTACCACGTCGCTAGTTCCACCGGGATACTGAGATGCTCCAACCAGGCCCGCTAGGAGGTGTAATTACGATTCAGAAGCGATAGAGAG AGCGTCACCTTTATGTTAGGCGTGTAGGGTTATCGCAACCATGCCCCTTATTTCCGCGATGTACCTCTTCCCAATGCTTCTAGCCGGGTCTCCTGTTGGCGGTGGCA GGTCTTGAAGACATAGCAAACGAATGCGACTCGCAAGCCACCAGACATACAAGAGTTCCGGGGGTCATAGCCCCGCCAATATGGACTTGGGTCTTCGACGGACCATT GGGTTGGAAGGACTGGACGAGGTCTGTCGGAGAAACGCAGATGAGACACTCAAACCCTTAAGGCATTCGGAAGAATCCCACGCTACTCCCCGTGCGACCTTATGAAG CACATAATACGGTGTAACGTGTAACTGACGACTCGGTCGTTACTGGCGGGAGAAACTGCGCGCGCTAAATGAGCCGTGGGCTTGAGGCCAGATACCCTCGCTTCGTT TTGTAAGCGTCGAGACATATCACTTTTCACTAGTGGTGGTCGAGGCCGGCATGCACCTAGTCAGGAGCGCGCATGATATACCCCCTTGGTAACAGCACACTCTGGGT CGATGGCGAATTTCGCTGGCATGCCTATCGGTCTGCTGGCCCGTAGAAGAGCGTAACCCGGATCTCATAAGCATCGAAGCATATACACAGGATCTCCCTTTACCATG GTTGCACAACTATCACTGTTTGATAGAGGTCCTTTCCCGACCAGACGGCCCGGCAGCCCAAAAGCGTCTGATCGCTCGGCAGATCTAACGGCTTCTATATGCTCTTA'''
    inlines=x.split()
    pattern=inlines[0]
    dna=list()
    for i in range(1,len(inlines)):
        dna.append(inlines[i])
    res=distanceBetweenPatternAndStrings(pattern,dna)
    print(res)