"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Highest-Scoring Fitting Alignment of Two Strings
Rosalind ID: BA5H
URL: http://rosalind.info/problems/ba5h/
"""
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

def fittingalignment(f, second):
    maximum = [0, '', []]
    for first in allSubstrings(f,second):
        s=[]
        for i in range (len(first)+1):
            s.append([])
        s[0].append(0)
        #first column
        for i in range(1,len(first)+1):
            s[i].append(s[i-1][0]-1)
        #first row
        for j in range(1,len(second)+1):
            s[0].append(s[0][j-1]-1)

        for i in range(1, len(first) + 1):
            for j in range(1, len(second) + 1):
                if first[i - 1] == second[j - 1]:
                    s[i].append(max(s[i - 1][j]-1, s[i][j - 1]-1, s[i - 1][j - 1] + 1))
                else:
                    s[i].append(max(s[i - 1][j]-1, s[i][j - 1]-1, s[i - 1][j - 1]-1))

        if s[len(first)][len(second)]>maximum[0]:
            maximum=[s[len(first)][len(second)],first,s]

    newFirst = ""
    newSecond = ""

    Backtrack = []
    for i in range(len(maximum[1]) + 1):
        Backtrack.append([])
    Backtrack[0].append('')
    # first column
    for i in range(1, len(maximum[1]) + 1):
        Backtrack[i].append("D")
    # first row
    for j in range(1, len(second) + 1):
        Backtrack[0].append("R")

    for i in range(1, len(maximum[1]) + 1):
        for j in range(1, len(second) + 1):
            if maximum[2][i][j] == maximum[2][i - 1][j] - 1:
                Backtrack[i].append("D")
            else:
                if maximum[2][i][j] == maximum[2][i][j - 1] - 1:
                    Backtrack[i].append("R")
                else:
                    Backtrack[i].append("Diag")

    newFirst, newSecond = moves_to_strings(maximum[1], second, alignRecontructionMoves(Backtrack))

    return str(maximum[0]) + "\n" + newFirst + "\n" + newSecond

def allSubstrings(first,second):
    l=[]
    for d1 in range (len(second),len(first)+1):
        for start1 in range (0,len(first)-d1+1):
            l.append(first[start1:start1+d1])
    return l

if __name__ == '__main__':

    x = '''GTAGGCTTAAGGTTA
TAGATA'''
    inlines = x.split('\n')
    first = inlines[0]
    second = inlines[1]
    res = fittingalignment(first, second)
    print(res)

    x = '''CAATCACCCCAATCCCTCAATCCTGGCCCCACGCATAGGCTAATGCCAATCGCGGCCAGGGTATAACCGCCATAACTGTGGGTCAGAAGGGATAAGTTCCACAATCCTATTTTCCTCGAGGCGCTTCGATGCGTTAACGCGTACACTCTGTCGGCCAACCGTGTGGGAGCCGAATTGGCTGGGCTGTTGAACATTCTATCAGTAGATAAACGAAGGTACATCCGAGGTTGTCGATCGACCGCGGGGTCGTAGCGCGTGCATGTTCCTTTCAGGCCCACATACTCCGGAACGGTTCATATCACGACTATTCTTGCACAATCGGACAACGGTGTACCATGGTGGACACCGTAGGAGACCAATACTGCGTAAATCATAAGCATTGGAGAGTGGACTGCTAGCGAGGCTCACCATGGAGTCTCGGTCGGCATCTCCTGACTGCTGTTCCATCGCGTTTTTCTTTTACTCACGCAATAAATCAATACCCCCTAACACAGGCCTGCTCCAGCCTTATTAAGGCCATAGTAGCTCTACATGTAGACCGAACGGAAGCACAGTTTGGTAGAAATTCTTAATCGACTATGGTCCGTGCAGGCCAAAAAAGGAATAATCTTCGAATTCTCACGCCTTCATTAGGGCGCACATGGTGGGGTAAATCACTGCACTCTGTTCGCAGTTAAGCGTTGCAATCAATATCGGCAGAACTCGGAGTCCGTATAAAGCCGCCTCAGCGTGCACACGCCCGTGCGGCACGTCATTAGACGAGGATTCCGGGGGACTGGCCTGTTCGTAATCCACTAAAACAATGGTCCTACCATCTAAAACGCACCGTGTTCCCCTCTACGGGAACCCCCTAGAT
AGAGCGCAGAGAAGTCATTAGAACATGTAGCACATCGCTTATTAAGGGTCAATACCTAAAGGGCCTAACTATACGCCACACGGAACAGCTC'''
    inlines = x.split('\n')
    first = inlines[0]
    second = inlines[1]
    #print(len(allSubstrings(first,second)))
    #res = fittingalignment(first, second)
    #print(res)
