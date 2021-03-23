"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find the reverse complement of a DNA string
Rosalind ID: BA1C
URL: http://rosalind.info/problems/ba1c/
"""

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

if __name__ == '__main__':
    x="AAAACCCGGT"
    print (str(reverse(complement(x))))
