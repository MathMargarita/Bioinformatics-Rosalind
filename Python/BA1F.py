"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Position in a Genome Minimizing the Skew
Rosalind ID: BA1F
URL: http://rosalind.info/problems/ba1e/
"""

def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]
def skew(text):
    sk=[0]*(len(text)+1)
    for k in range (1,len(text)+1):
        if kmer(text,0,k)[-1]=='C':
            sk[k]=sk[k-1]-1
        else:
            if kmer(text,0,k)[-1]=='G':
                sk[k]=sk[k-1]+1
            else:
                sk[k]=sk[k-1]

    return (sk)
def indexofminskew(skew):
    ind=list()
    minval=min(skew)
    for i in range (0,len(skew)):
        if skew[i]==minval:
            ind.append(i)
    return (ind)


if __name__ == '__main__':
    x="CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
    res=indexofminskew(skew(x))
    print(str(res))
