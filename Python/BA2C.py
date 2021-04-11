"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Profile-most Probable k-mer in a String
Rosalind ID: BA2C
URL: http://rosalind.info/problems/ba2c/
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

def probability(window,profile):
    # probability of kmer in string according to profile matrix
    prob=1
    for i in range (0,len(window)):
        if window[i]=='A':
            prob=prob*profile[0][i]
        else:
            if window[i]=='C':
                prob = prob * profile[1][i]
            else:
                if window[i] == 'G':
                    prob = prob * profile[2][i]
                else:
                    if window[i] == 'T':
                        prob = prob * profile[3][i]

    return prob

def mostProbkmerinText(text,k,profile):
    d=dict()
    for window in Lwindows(text,k):
        d[window]=probability(window,profile)
    return  [x[0] for x in d.items() if x[1]==max(d.values())][0]

if __name__ == '__main__':

    x = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT\n5\n0.2 0.2 0.3 0.2 0.3\n0.4 0.3 0.1 0.5 0.1\n0.3 0.3 0.5 0.2 0.4\n0.1 0.2 0.1 0.1 0.2"
    #x='TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCCTGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGCGCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCACCCCTA\n6\n0.364 0.333 0.303 0.212 0.121 0.242\n0.182 0.182 0.212 0.303 0.182 0.303\n0.121 0.303 0.182 0.273 0.333 0.303\n0.333 0.182 0.303 0.212 0.364 0.152'
    inlines=x.split('\n')
    text=inlines[0]
    k=int(inlines[1])
    profile=list()
    for i in range(2,6):
        profile.append(inlines[i].split())
        for j in range(0, k):
            profile[i-2][j] = float(profile[i-2][j])
    res=mostProbkmerinText(text,k,profile)
    print(res)