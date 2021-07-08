"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Generate the k-mer Composition of a String
Rosalind ID: BA3A
URL: http://rosalind.info/problems/ba3a/
"""

def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def kmercomposition(text,k):
    #lexicographic order
    return sorted(Lwindows(text,k))

if __name__ == '__main__':

    x='''5
CAATCCAAC'''
    inlines=x.split()
    text=inlines[1]
    k=int(inlines[0])
    res=kmercomposition(text,k)
    print("\n".join(res))

    x='''100
ATTGGTGACACAGAGATCACTGGCCTGGTGCGCTTTCTGGTGATCACATTCATAATTGAGGATTACTTGTCCTCTCTTGAGAGTCGCAGCACACCACTTTTAGCCATGGGTCGTCTATAGTTCTTAGAGGCGGTTCTCCGCTTGACTAGTTGGATGCTAGAGCTTAAACACCGCGACGCTGTATTACAAGGGCGAAGACTTCCCCATTGTCTGATTGACCAGCTCTCGGAATTCCACGGGAAGGCCACCGATTGTTTGAGGAGGCGGGGAGGAGCAGTCAGATGGGGCCTCAATCGAAGGGGACCACGCAACCCCCGTCGTGTAGAGGTCCTCTAGATGCCGCCCGCAGGCGACGTAGCGATTCTCGAAATGCGACTCAAAGTAGAGAATAACTGCCGAAATCTCACAACGAATGGGGTGGCACCTGCTGCCTTCCGTTGGAGTGCGTTCACCAACTATTGTAAATAATGCTGCCGTAACATGTAGAGGAACAGCAGCCCTAGGGGCAAACGTTACGCAGTACATTTCTTCTCCGGTGCAAACCGCTCGAGGAATCGCACTTATTACTTTGCGTAATCCAACTTTGCGCAGAAACGCCTGTCAATTCCCACTGAATAGATCTAATGTACCCGGTGAGTACTAGAGGTCAGCGTTTCAAAAAGGGAGGCTCAGAAGTCGGGGTATTCACGCGCATTTTTTCGACGGTGCGTGATTGATCATGTCCTATGACTCATAGTAATAAACCTTTCCAACTTCAGTGTTGTCCACAAGGCGGACTTTTATCGAAGTGAGGAGCAAAATAATATCTACGTTAATCTTTAGGACTGCCCTGAAGTGTAGGCGCCCATATGAAAACGCCGCGGGGCGTTAAGAGGAGTGATGGTATGATTCTTCCCCCGCGTAACTCCAACACCAAGATTGTCCGGATCGTTGACCGGAAACGACCCCGTGCATCGCGACCGGGTTATCACGACACGACCCCGCAAATAGACTATGCCCGGCACCTACGAGTATGTATCTTTCCAGTCATATCAATATGACACGTGTAGGCGTGGAAGTAAAGAAGGATGTACAACCGATCTGTCCTCTAGATATAGCCAAGTGCGCGTCCGGGGCGGTCGTTAATCAAAAGCTCGTCCTGAACTTTCACGAACACGCATTATCTCCTGGCGCGAGCACCCCCGCGGGTGCGGCTCCGGGATCAATCGATCATATCCTTAGAATCGAACGCATTGGATTTCATGTGACAAGGAGTTAGGTTCTGGGAAGAGCTACATCCTTCACGTCCTTTCCTCTAAACCTAGTGCACGCTGTTAACGAACTGGAATGAACGCCTCAGTTTTTTAGCATAGGTAGCATCTTACAGGTTACCACGTCATTCCGTTGCCTCACCGGCACCCGCCTGCTCCGTATGTTGCCTACTCGATTGCACGCCGTGGTTCTTAAAAGACTTCGCAGGCCAGACCTCGGGCCCGTAATATACAAGGTCCTCGTGACTAGACAAACTCCCTGATCAAGAGTCATCTTGCGCATGAGTACGACGTTTCTTTAGTACTAATTACTTGGCTCCCGCCACCGGCTTCTCGTTTCACTTTGAGGACGGTGCAGAGGGAATATCCGTGCTCACAGTGTTCCTGGTAGCCCTCATGAGTTGCTTGCAAGCGACGTATTCAAGCTTTTAGACGTCCAACATTGGGATCCTCCATGACCATAAATGCTCCGGAATTTTAGAAGCCCGAACAACGGGGAGGTACAGACGATTTATAGCAACTCGTTAAGGAGTTGACGAACTATCTACGGTGCCGGCTGAGCTTGTTTCACTAGACTTCTTGAGGGCGTGCGTACGAGTCTAGAGATCCCGCTAGAACTAATCGCTACTCTTGCTCCCCTTTCCTCTTGTACGTCGTTGTGGTAATCTACAACGCCTGGTATCTGTCGTGGTGGTACCTGAGTGCACAAGCCACAGAGGAAACGCATGGGCCTGGAGCGCCGATGTGTGATCAGGTTGACCAACTCCAAGACCATAGTACCTCAAGAGCGATATAATTTTTTAGAACTCCGACCCTCCGTACAAGGGCACAAGTCGCGATCTCAGTCCGACCATCGACATATAACAATACTATTTCTTTCTTGTGGAACACCTACTGCCCACTTGGAAACTAGCCATAAGATGTGCCGGGATGTCTTTCGTCTACAACAGAAAACCGTCCCTAGTCATTAGCTTATCGCCATCGCAGGGCTACCAAGTCTATTCGGAGGGGATTTGGGAGAGGCGCGTCGGATTTCAATAGAGTGTACATTTGGGAACCCCAGCGTGGGTGGACGTCCGACCGCACGGTCTTGCTGATTTGCTCCGGCAACTGGTATGTTGATCCCAGTCGGGCAAGGCAGAGACGTATTTCCCGTCTGGATTGCAATTTAGGGTTTACTCCGCGACGCACATCTTGCCTCTTACCTCTCGTTCGTATGTGGATACACCTCCAGAGTATCCGCAAGCTTTCGCACGTCACCGCTATTAGAGTGCGCCTGATACACGGCAACGTGACATTTGTGGCCACCGTATTGCCTGAGAAGCTCCGGACCAGATGGCGCGGAAGCACGCGTGTATCGTCGTATCACTCGTACTAATGATTAGCCGCGGCATATTGATATTCCATATTGGTATGGCATTTATTACTCGCTACGAGACTACGACTGTCAAGATCCGAAACCACTAGGCGACTCCACGATAACGGGCCTAACCGTGAATGAGATAGTCTTCACGCAGTCAGTGAGATAGGAAGAAACGAGCGTTATACAAGTAAGTGCACCGGGCGCACGCACTCCTGTGCACGCCGCACATTGGGGTAATAAATAGCATCACGTTCTCGTTTACAGTGTCGTAGAGTAAGGCACACCAATGCAGACCCATATAAATCAACTGTAGGTCCGCTTTCTGGGTGCTCAACCAATGCGCGTACTTTCATGCCACCGCATTCGGTACAGTCCGTACTGCGCCCTATACGGAATGGTAAGCGTGCTCGGATTCTATGTAATTTGAGGAGTCGCTAACCAACAGTGTGGGGTATGTCTTCGGGCGCACACATTATCGCTGGTATCTGTTGGCAGCGAGGGTGAGTCACTGGCTTAGTTCGGACTGGGGCCTACGTACAGTTCGTCATCTAATTTTGACTAAGCAACTTAGATTACTTTCGTGCTCTAAACGTCCTGAGCTACTAAGGTGCCCAATACATCCATTCTCTTTGGACTCACACTTCGCACTGCCTTGGTTGTTAGCCCTTAATAAATTGGACGTGCGATATTGGACCCCCATGGACAGTATAAAAGGTGCGCTGGGTTGCTCGGCAAACAATATTGGGAATTCCCCCCAGCAGGGCATAGACACGCGCAGTTCGCCGAGGATGTCCCACGGTCGCCGTTACTATTCAACACCCCCTAGACGTCACAGTAGCTAGAGGATACCATCGGCTCAAACCGGTGTGACGGTAAGGCCTCATGCTTCCAGGTTAGTGCCATCCCGCACTCGGTAGCGAGCTTCGGATCTATCGTGTGCATATGACTACACACGTCGATAACACTGGTAACCGAAATAGTAAGCGCGTAATTAGGGGGACGTTTGAATTGCATTAGAAGGGGGCTAAAGGTTCTCAGCAGGACAAATCGTGGTTGAGAGATTGTTAGGTAAACAGCAAACGTCGGGTTACAAAAAAGAGCTAAGAGCGACGATCGCGCCGGACGTTAAGTTCAGTCACTCCCGGACCCCTGCGGTGTACAGACCATACGAAGCCGTCACCGCTTTGGTCGTGTATTTGGTCGGTCTCCGAAAGTTGCTGCTCGCAGCTAAATAAAGCATCTCAGCACTGGTCGGGGAAGCCAGTTGAACTCAGTAAGCTGCCGGACTTTCTCGTAACTGTCAGCCAATTGACCATTGGATTTCGCCTCCTAAAAGCGTGACAGGCTCCGAGATTTACCGCGCGTCACGCCCGTCTTTGAGCTACTACAATCTATAATAGACTATGGTGCTTTCCCTGGTTAAAAACGAAACTCGAGCGTGCTTCCCTAATGTAGTGCTCCACTCCTAAGAGCTTAGGCACCAGATTCCAATTGACAGGTCCTAAGTAAGCGGTAACCCACGACCCGCGCCGACGATCGTCTAGTGTCATCGTACCGAGAACTCATTCTCGTGGCGGCTAACCAATCATTATAACAGTTTAATGAATATTCCAAACGATATGCCATTCGCTATCGTTGGGGCACGCCGGCTCTTTTGTCGGCCACGAAGAACCCCGACTAACTGCAAGACGGTGCTCCTGGAGTTCCCCACCCGCTCGCCTTATTTTGCGAATTAAAGTTCAGTAAGCGCTTTTCACGTGTAGCGCTGACCAGGACGTTATTTCCACGAGCTCCGCCAGTGCACTTAACGGAGTCATTTCTCCCAATACATATTAAGAGCCGCCTCAAGAATTAGTAACAACCTCAACGTCCGTATCCTACGGTAAATACGCTACGTTAACGGAAACCCGTTTTGCCTTATGGGATGAATGGAATCCTGTGCCGGGAGGCCAGATCTGGAGCTCGGGACTGTGTCAGAAATTCTTGCCCAGGTTAACCTGTTTTAAACAGGTCGCTAGAGGAGTAAATCGCAGCAATGTACTTGTCTTATTTATATTATATTGCCAATACCGTAATGCGAATCTAGAACGGGTGACACTTTGAGGTTAAACCTCGTCCAGTATCCGCGTCCGTTTGCTCTGCGCTTTTCTCCCTGGACCAAAAACGGTACGTGGAGTAGCTTTGGTACCCTGATCACGTTGGTAGTCTTAGAGCACAAGCTGGAGGGTAGAGCAGATGGAAAGTAGGCGATGTTTGATGACGACACTCGTCGCATTCGGCCATCTTCGTAGGGCGATAGGAAACCACCTATCTCGTTTGTAAAGCGCCCGCTGTTGCTGAGTTATACGTCGTCCTCGAGTGCCTGTAATCATTGAGACCATAATGCGAGAACACAGTTTTAGTGTAAGTTTATCAGGTGGGTGCATAAGAACCCTCAATCGCTTGTAAGCTCGATCACGTATTTCACGTGCGGAGTCAGGAAGTTGTCTTAGTGCGATCCCGGACGAGCTGGCCTATCAGGCACCGCCCCGATACGGGATCTGCGGGGAATACGAGTCGAAGGGGGTACATCTAGGAGGGGGGAATCCCGCAGCATCGGCAATCTCGTTGCTCTTACTCCTTTTATGGATCCGCTAGTGCGGTCTGCTAGAGGACACTCCCGCCAATTGTTTCGGCCCGAATCACAACGCATATGGCGAGCCCCAGTTATGGAATTATCGTCTGTACATTCACCGTGGCTGATTGGCCACAACGCCGCTTACTAATCGTGAAGCGATCGCTCTGTGGGCAACGGGTGCGATTTCCTTCTCTATCAACAATTGATGTTGCTCCTATTCATCAGCAGTAAGTTCGCAGCTTAGAAGGAGAGAGGTGCTAAGGCTGCCAGGTTAGATTTAACACGCAAGCGAGTACCAGTACAATTTACCGAGAGTAGCCTAGTCTAACTCTCATGGCGTGCTGTACTTCACTTGAATCTAGCTAACGAAGAAGGGGATAACGTAGCGCATTGGTCAAAGAGCACCTCAGTGCTGAATCGTCTCTCCCGAGGCTCTGCAAGGCCGTACCGCAGAGACTCATCTGGACGGTCTTTTACTTCTCCTGGGAACAGCGATAATGCCCAAATGTCCGAGATCTGTAAAAGGACAGCGCTGCTATGCGATAGACCGGGGGCGAGTACACCCCTTACAACCCCCGAGATCGCAAGATCGAGTATCAAGTCCTAGGCTTGAAACGGCGTAACCGTGGTGGTGGAGGTGCGAGCACTAGTCAATACTCAATATGCCCTCAGTGTTAAGTCACGACAGGCGCCTGGCGGGAAGCTGAATCAGACACGGAGCCTTTTTCGATTGCCTTGGGATGTGTTCCTCACGTTATTGCTTATGCCCGTCGGAACATCTTTTCGCGGTATTACAACCAACGTGAGATTAGAAGCATGATCCCAAAGACGCCAGGTACAGTGGCAAGTTTGATGGAAGTAAGTAGATCGAGATATGAAGCTTGCTAGTTTCTCGATCCTGCTCCCAGCGGGAGATGCTTACGTGAGGGGGCAATTGTCTTACGGAGGTGCCTCTGGATTCCGCTAGGTCTTTGGGGTCGCACGGGAAAGGTCCCCAGCAGAGCACGGGTACCCCTGGATCATGTGCATTAGTCCAAATTCCGTACCGTTAGGTACGTAACTGCTTGCAATCATGCGGAAAAAGTCGAGCCTTTTTTCCGTTTTACCGAGGTAGAGTACGGTTGCGTTTTGAACCGCAGAGTGGGTCTTTTCCAAGGTCGTCCGTGCTACGTATTATGAACTGTAACAGAACTGCAGGTCGTTCCGTGCCACTTGCGCCCCCTCGTAGCAACGACGCCTATACGCGCCATAGACGAAAAAAAGTGGTGCATACCACACCCCTTAGCACCACACTGTAGAGCGTAGCGTAATTGGGCTCTACTGCGCTTCTGCTTGTAGCGTTGAAGACCATTCAGTTGGAGGGTATCGCATGATTACACCGCAGATGCTGCATAAGATGGGCACAAGACGCAGGGATTAGAGGCACCACGCATAGCGTATCCCGGTGCTAACATCGACATCATATCGCCGTACGCGTGATATTGTAGACAACCCAGATAGCCAGCCTAATAGCGCATGTCTCGCTAAAGTATTGACTTCGAGCGAGACGGGTAAGGATCGGCAGTCAGTTGATACCTGTGTTCTTCAGGGTTTGCCAAAGTTACGAGGATTAGAGAAACTTCATATGCCACGCTACTCACCAGGTCGTATTGGTGAATATCGTGTACATTCCAAGCGTCCCAATCCACCCACGCGTGAGTAATGATTGAAGACTGGACATAGAGCACCTGGGTAGCGCAGGGAAATCACACCGGGCCTGTGACCCTTATACCCCCGTCAACATCGAGCGCCGCACACTCAGAGCGGGTCGGGAGATATTTATACTGAACACGTCTAAAAGCGATGAGCATGGATTTTAGCGGGGTATAGATGTTAAAATTGGCTATCACGGGGTGTCCTATGCGACCGTGTACATCTGTACTGATAGTCGGTCTGGTGTAGCCGGCGCGCAGAAAGGCCTCTGAGATTAGCACTACGACGGTAGGTTTGTTAGGGAACGTTTTTCCCAGGGAGTGTAATTGCAAGTCGATATTAGCCAGTAGTCCTTGTTCTGTGAAGATAGTCGTTTTGTCATGTCTGGAATTAATTTGATGCGGTCACCATGGGAAGTTATACCACGGCGTGCTGGTTTTCAGAGTCGTTAAACCACACAGAACTATATCCCTGTCGTGGTGAAAGTTATGCACTGGTCCGGGTATGTAGTCTATTGTTCTCAGGGAAACTGTCGCAGGCACAACGTGACAGATTACATTTTAGCCGTCTAACAAATCAGCTCTGGCTTTCAGCAATTCAATCCATGCTCCGAGAGACTAGGACCCCAGCTCTGACAGAACTACAAGAGGTTTAAAGGAGTTTATGGGAGTTAGAGGAACACGGGGCGGCGATAGCTTACCTACAACTGCTTTAGCTAACTATGAAAGTACTCGAGTTCCGATCGCTTCCCAACCATGCACTCTTTCTAAAGAGGCCTACCGGCGACCCACGGATGAACTCCACTTAAGGGACGTTGAAACTCTCTCGCATCCTCGGGTACGCCACTAGAATACGTCCGCACCCTCCTAAGGTCGTCACTCATTGTGCAGGAAACGCAGATTGACGGGATTTGTACCACATCAATGAGCTTCATATTCGTGACGATTGCACGTGAAGTCACGGCTTGATAACATAGTTCGTACAGTAGGAGACCGGTTCCGGCTGGATTCATCCAGGGTCACGGGTCGACAGTGACGCTGTCAAAGCCTCGTAATATGTTAAAGTGTTCCGGAGTCAAACCAATCCGTACACCCGCAAGGTCGTCGTAGCATAATAATTAAGTCCGCCTAAGCAAGTCGAGTCTAGTAGTTGGGTACCTCTAGAACTCAAGCGATGATAATGCATCGTCTCGATCCCATAAACCCGCGAAGAACGCCTGGTAGGCCATTCGAGGGCAGATTGAATTCCCGTACTTGGGGTATGAGCTGAAAACGATGTGATCACACCGATTCACGCACCTTTGTAACTAAAGCGCAGCCGCTGAGTGTGGCTCCTCCTTAAGCCGGGATTGAGGAACATCTCTCCCAAAGATTAGTCCGTCCTAAGCCCCGGCTACGGGAGTCAATACGAAGCTAAGGCTCCCAATAGATAATAGCCGTCTTTACTCATTTACTCCTAAAATATCTCATTCGTATGGGCATAGAAAGTATATTGCTCCCGATGCCTTCCACATCCTGTACGTCAATCAATTAGCGTAACAACGACAACCTTCCGCGAATACTCCCACAAAGCATTCATCAATGCCTCATACATTGGGGCGCCACAAGGCTGCTTCTCCAAGGTTTTAAGTATCCCCCTCCGAGTCAACGAATAGAGACCTCTAACCGAACCAATAGGCACCAAGGCAGCATTCGAGATACTTGACTCAGACATTTTCAGAAAGGCCAACGACGATCGCGCTTTGCTGGGGCAGATGACTTACGACACGCTCACGAATTCCTGTCTCGGCATCATACACGTCAATAGCAGTTGAACCACTAAAGTTTAGGCAGGGGCGCTTACTATTGTATAGGATGGCCCGTTAAACCAAGACAGAAACATGCATCGAGGGCTGGACCAATTCGGCGGCTATAAACCTGGAAGGACGGCGAAGAGTTCAGGTGTTTCTCCGTTTCCGAAATTTCGTTTAAGGCTACTAGAACTGTATGGAACCATGGTGAATAGTGATGTATGAGTGGACCTCATCTATACGGCGCGGGGATTCCGCCGACCCAGAATCCGATCTAGGCAGCAAGCTCTTTACATTCTCGTGGATCGCGCTATCGACGGTGGGCCGGTGGGGTTAGCTATTACACGTAACATGTAACTCGTCACAGGGTAAATAGCTCCAGGCTATAGTGCGCCTGCTCTTTGCCTGCAGAGACGTTGATTAATGTGCTTTGGGGAATATTTGGTGTCACCAACACGAGCCTATAGCTGCAGTACCCGGCACCGGCGAACCAACCGAAATCTCTATCGGTCTGGAGAGAGGACGGGTCACGAGTAGGTGCAATCTACTGAAAACGTGTTTGGACTCGCAAGTAGGGCCCCTGACCTTCCTGAAACGTTGTAGTTTAGACTCACCCACATGCTTGAAAGACCGCCCGATGTTAGAGTCAACCACCTACATGTTGCCTTGGTGGTGAGCTCAGGTGCCCTCACCAGTGAAGGGGGAACCTATATCACTGTGCGCGTGGTCGTCCCTACATGCTTTAACCTAACGTGATGGCAGAATCGCGTAAGATAACCACTTCAGGGTCGCGAGATTCAACATTCGTAATAGCAATTAAGCCTTAGATCAGAACTCGCATTCTAATGTTTTCTTGCGCGGAGGAATATCTGTAGTTAGCCCGGGTTGGATGAGGAATAGA'''
    inlines=x.split()
    text=inlines[1]
    k=int(inlines[0])
    res=kmercomposition(text,k)
    print("\n".join(res))

    x='''50
GGCGCTTCTAACGATCAGGGACGAACGAAAGTAGAGACATTTCTTGTGTAGAGGATAAGCACAGATTAGCGGAGTTATTATCGAGGCGCCTCCCTAGAGGCGGGGCCGCCTGACGTCGGCGCGACGGTGGTCTCTTGCCGGCGGGGAGCTATCAGATCCGCTGCGAGACTGCGGGTCAATATTGACACCCCCGAACAATACTATGTCTACGCGGCGGCAGAGTTCCCTGGGCGTTAAAGCGTCTGTTTACACTACTCTGGTAATGTCAATTTAGTATGAGGTTGACCCTGCGCGCCACAAATCAAAGTGAACGCGTACGGCAACTTCTATCTCATCACTAGAGCGACGCTGTGGGCGATTCCAAACTTCGTCCAAAACTAAAGCAGCTGTAACTTCGAAACTCTACTGTTAACTACCATCTGAGTCGTTCGAGCGGGCGGGTTTTGCGTTGGGTCCTCCACATCAACAAACGGGCGGTGGCAGAAAGCAGCTTATGACCTCGGCGCCAGATTAATGTAGTAGCATTATGAGGGTGGTGGCTCGTCGAACATTGAGTAGGCGCTAGCAGTACAACACGAATGATAGTGCGCAAGCTTTGGAACTAGATCTGTTTCAAACAAGGACAGTCACAAGCATCTGGTAACGGGGAATTTCAATTTTCAAGCCTTGTTACTAATAGTCTAGCACTCCTTTTTACTCAGCCGAGTAACAAGAGTACGTCGCCACCGCTGGGGTTGACTACACCTGACTCGGTAGTTGCGAATTCGCTTAGCCGCGTACATACGTGGTTGGAAAGTCTTCATAGGTTTACTCGGTCAGTCTAGTCGCTCACGAATTGACTACGAGATCCCTTTTCCGAGGAATCGGCGGAAGGTAATACGTGGCCTCAGATACCGCAGCACTCTCGTTAACGGCTGCCTGACACACTGCTAATTTCTTAATTTGACGCATGCTGTTGCGAACCAACTACAATCTACCGTAATGCCGGGTATCAGTCCGG'''
    inlines=x.split()
    text=inlines[1]
    k=int(inlines[0])
    res=kmercomposition(text,k)
    print("\n".join(res))