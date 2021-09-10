"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Highest-Scoring Overlap Alignment of Two Strings
Rosalind ID: BA5I
URL: http://rosalind.info/problems/ba5i/
"""
def allSuffixPrefix(first, second):
    l=[]
    for start in range (0,len(first)):
        for end in range(0,len(second)):
            l.append([first[start:],second[0:end]])
    return l

def alignRecontructionMoves(backtrack):
    n = len(backtrack) - 1
    m = len(backtrack[0]) - 1
    moves = []
    while n > 0 or m > 0:
        moves.append(backtrack[n][m])
        if backtrack[n][m] == "D":
            n = n - 1
        elif backtrack[n][m] == "R":
            m = m - 1
        else:
            m = m - 1
            n = n - 1

    return moves[::-1]


def moves_to_strings(first_word, second_word, moves):
    pointer_w1 = 0
    pointer_w2 = 0

    w1 = []
    w2 = []

    for move in moves:
        if move == "D":
            w1.append(first_word[pointer_w1])
            pointer_w1 += 1
            w2.append("-")
        if move == "R":
            w1.append("-")
            w2.append(second_word[pointer_w2])
            pointer_w2 += 1
        if move == "Diag":
            w1.append(first_word[pointer_w1])
            pointer_w1 += 1
            w2.append(second_word[pointer_w2])
            pointer_w2 += 1

    return "".join(w1), "".join(w2)

def overlapalignment(f, sec):
    maximal=[0,'','',[]]
    for [first,second] in allSuffixPrefix(f,sec):
        s=[]
        for i in range (len(first)+1):
            s.append([])
        s[0].append(0)
        #first column
        for i in range(1,len(first)+1):
            s[i].append(s[i-1][0]-2)
        #first row
        for j in range(1,len(second)+1):
            s[0].append(s[0][j-1]-2)
        for i in range(1, len(first) + 1):
            for j in range(1, len(second) + 1):
                if first[i - 1] == second[j - 1]:
                    s[i].append(max(s[i - 1][j] - 2, s[i][j - 1] - 2, s[i - 1][j - 1] + 1))
                else:
                    s[i].append(max(s[i - 1][j] - 2, s[i][j - 1] - 2, s[i - 1][j - 1] - 2))
        if s[len(first)][len(second)]>=maximal[0]:
            maximal=[s[len(first)][len(second)],first,second,s]

    first=maximal[1]
    second=maximal[2]
    s=maximal[3]
    newFirst=""
    newSecond=""

    Backtrack=[]
    for i in range (len(first)+1):
        Backtrack.append([])
    Backtrack[0].append('')
    # first column
    for i in range(1, len(first) + 1):
        Backtrack[i].append("D")
    # first row
    for j in range(1, len(second) + 1):
        Backtrack[0].append("R")

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if s[i][j]==s[i-1][j-1] -2 or s[i][j]==s[i-1][j-1] +1:
                Backtrack[i].append("Diag")
            else:
                if s[i][j]==s[i-1][j]-2:
                    Backtrack[i].append("D")
                else:
                    if s[i][j]==s[i][j-1]-2:
                        Backtrack[i].append("R")


    newFirst,newSecond= moves_to_strings(first,second,alignRecontructionMoves(Backtrack))
    return str(s[len(first)][len(second)])+"\n"+ newFirst+"\n"+newSecond
if __name__ == '__main__':

    x = '''PAWHEAE
HEAGAWGHEE'''
    inlines = x.split('\n')
    first = inlines[0]
    second = inlines[1]
    res = overlapalignment(first, second)
    print(res)

    x = '''GCTATAAGAATAAACCACTAGATCACCTCCGGCTCGCTCACTCCTGATCATGGTTCGTGCTAACATCGCGCCGCGCTGACGCCGAATCGTTCGTAGGAGACAAGTCGACGACCTCATCTACAGGCAAAAGTTAAATTAGCTCTCGGCTAGATGTGACAATCGGAACCCTGCACCCTGCGTAATAGGGTAAATAGTCGGGAGTTGATGCACACACCTAGATATTGGCTGAATGACAGACTGCCATTCCTGCACTGGAAAGTAGAGTGCATATGTTTCGTGAGATTATGCAGGCTCTACGGTTATACTGGGCTCCACGGATTCGACCGGTACTGTTGATTGAAGACTCTTCTATAGAGGCTCTAACCGCGGAGGCCGCAACCAATCGACAATGAAGCACCCGTCGTCGGTATCGTTGGGAAGGACGACACCGTAAGGGCAGACTTTATCGTGACCCGTCTGCTTGCTAGAAAAGCCCTGGCGTTTGTACAACGTCCGTGCAGAATTAGCGTTTTTCTCAGGAAAGATGAGGGGGTTGATCATCATCTCGTTTCGCACGGGTCAAGCGCATTTTCCTACTGTTTTGGACACAGTACGTCTTCCACTGATCTCATACGGACATTACCAGCACCCTTTTGTACCTGTCGTAACTTGTGCCATTCTAGGCCCGTTTTCACTTGCGCTTATGATCATGGTTCCGCTGATCTATATGGGCCGGGTAGGGCACTCCCAGATGAAGGGGAGTAATGGTAGCCGGATCCAAGTGACGCGCCCTAGCGGCTCCGGAGTTTGATAGACGTCGTGCTATGGAGCGTTGGAGCGACAACGCGCTCGTGCTCTGGAAGGTCGCTGCTGATCCGTAA
TACTGGTCCTGACCCACCTCACTTTGATGTCCCCTTTTCTCGTTTGCGCATCAAGATCTGGCCCGCAACTATTGGCCGTGAAAGGCACTCATCAATAAAGACAGTACTCACGCGGTCGGATCCAAATGCGCGCACCGAGCGGCCCAGGAGTTGATAGCGTCGAGTAACCTATTAGGACTCGAGGCAACTCGCGCTCTCTCAGGAGGCTCGCCTGCTAGTCCGTGAACGACGGATCTTTGGTGCTGCCTTCCTATCATGACATTGCCTAATAACGAGCGGCACCTACTCCCAGGTCTTTGAAGGGATGGCTTGTTTACCCCGATTCCGAGAAATAGAGATGACTCCTAAGGAAGTAATGAAGGAAGTTCAGTGGTATGGGTATCGTTTAGTTTGCCAGGGAGATTGCCCATAACCTAAGTCCCTAATACAGCAGTAGATCTCACCATAGATGTAGGAAAGCACAGTGATTTAGACGCTTAGCCAAATACAAAGGAATGTACCCCCTCCTAACACTGAGCACCGCTTATTTACTAGTATACTCAGAGTGTGGAGCGCTGAACGTTGTGTCAACAAGAACATAAGCCGCCGTGAATGAATTTGTGAAGGGGAGTGATCATGGTTTTACTCGTGGTAGATTTGGGCAGAACCTGATTCCTCACGTGTGAATGTAATTGAAGCTGACTCCCACACATACAGGCACGATTCTTTTAGATGATGTTTTAGGAAGCGCATTTCGTATTAACACTGCCTTGCATTTGATAACCATCACTTGTTCATTACATGATCCCATAGGGCCGTGTTGTTACTTTCGTGTTAGTCGAGCAGTATGACCACCTTTTCGGCGCTTGATATGCCTCAAGACGTGCGATTCAAGGAATCAAACAAATGAACGCCGCACTGGATGACTGGG'''
    inlines = x.split('\n')
    first = inlines[0]
    second = inlines[1]
    res = overlapalignment(first, second)
    print(res)
