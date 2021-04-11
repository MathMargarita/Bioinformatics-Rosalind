"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Reconstruct a String from its Genome Path
Rosalind ID: BA3B
URL: http://rosalind.info/problems/ba3b/
"""
def reconstr(seq):
    #Find the string spelled by a genome path
    text=seq[0]
    for i in range (1,len(seq)):
        text=text+seq[i][-1]
    return text

if __name__ == '__main__':

    x='ACCGA\nCCGAA\nCGAAG\nGAAGC\nAAGCT'
    #x='AAGCTCGACAAGACGCACCACCGAT\nAGCTCGACAAGACGCACCACCGATT\nGCTCGACAAGACGCACCACCGATTA\nCTCGACAAGACGCACCACCGATTAT\nTCGACAAGACGCACCACCGATTATT\nCGACAAGACGCACCACCGATTATTT\nGACAAGACGCACCACCGATTATTTG\nACAAGACGCACCACCGATTATTTGG\nCAAGACGCACCACCGATTATTTGGT\nAAGACGCACCACCGATTATTTGGTA'
    inlines=x.split()
    res=reconstr(inlines)
    print(res)