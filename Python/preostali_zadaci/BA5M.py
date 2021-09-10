"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Highest-Scoring Multiple Sequence Alignment
Rosalind ID: BA5M
URL: http://rosalind.info/problems/ba5m/
"""
def multiplealignment(first, second, third):
    s=[]
    for i in range (len(first)+1):
        s.append([])
        for j in range (len(second)+1):
            s[i].append([])
            for k in range (len(third)+1):
                s[i][j].append(0)

    backtrack=[]
    for i in range (len(first)+1):
        backtrack.append([])
        for j in range (len(second)+1):
            backtrack[i].append([])
            for k in range (len(third)+1):
                backtrack[i][j].append(0)

    for i in range(1, len(first)+1):
        for j in range(1, len(second)+1):
            for k in range(1, len(third)+1):
                if first[i-1] == second[j-1] == third[k-1]:
                    s[i][j][k]=max(s[i - 1][j - 1][k - 1] + 1, s[i - 1][j][k], s[i][j - 1][k], s[i][j][k - 1], s[i - 1][j - 1][k], s[i - 1][j][k - 1], s[i][j - 1][k - 1])
                    if s[i][j][k]==s[i - 1][j][k]:
                        backtrack[i][j][k] = 1
                    elif s[i][j][k]==s[i][j - 1][k]:
                        backtrack[i][j][k] = 2
                    elif s[i][j][k]==s[i][j][k - 1]:
                        backtrack[i][j][k] = 3
                    elif s[i][j][k]==s[i - 1][j-1][k]:
                        backtrack[i][j][k] = 4
                    elif s[i][j][k]==s[i-1][j][k - 1]:
                        backtrack[i][j][k] = 5
                    elif s[i][j][k]==s[i][j - 1][k - 1]:
                        backtrack[i][j][k] = 6
                else:
                    s[i][j][k] = max(s[i - 1][j - 1][k - 1], s[i - 1][j][k], s[i][j - 1][k], s[i][j][k - 1], s[i - 1][j - 1][k], s[i - 1][j][k - 1], s[i][j - 1][k - 1])
                    if s[i][j][k]==s[i - 1][j][k]:
                        backtrack[i][j][k] = 1
                    elif s[i][j][k]==s[i][j - 1][k]:
                        backtrack[i][j][k] = 2
                    elif s[i][j][k]==s[i][j][k - 1]:
                        backtrack[i][j][k] = 3
                    elif s[i][j][k]==s[i - 1][j-1][k]:
                        backtrack[i][j][k] = 4
                    elif s[i][j][k]==s[i-1][j][k - 1]:
                        backtrack[i][j][k] = 5
                    elif s[i][j][k]==s[i][j - 1][k - 1]:
                        backtrack[i][j][k] = 6
    newFirst, newSecond, newThird = first, second, third
    newFirst, newSecond, newThird=multipleAlignRecontructionMoves(backtrack,newFirst, newSecond, newThird)
    return str(s[len(first)][len(second)][len(third)])+"\n"+newFirst+"\n"+newSecond+"\n"+newThird

def multipleAlignRecontructionMoves(backtrack,newFirst, newSecond, newThird):
    i, j, k = len(backtrack)-1, len(backtrack[0])-1, len(backtrack[0][0])-1

    while i > 0 and j > 0 and k > 0:
        if backtrack[i][j][k] == 1:
            i = i - 1
            newSecond = newSecond[:j] + '-' + newSecond[j:]
            newThird = newThird[:k] + '-' + newThird[k:]
        elif backtrack[i][j][k] == 2:
            j = j - 1
            newFirst = newFirst[:i] + '-' + newFirst[i:]
            newThird = newThird[:k] + '-' + newThird[k:]
        elif backtrack[i][j][k] == 3:
            k = k - 1
            newFirst = newFirst[:i] + '-' + newFirst[i:]
            newSecond = newSecond[:j] + '-' + newSecond[j:]
        elif backtrack[i][j][k] == 4:
            i = i - 1
            j = j - 1
            newThird = newThird[:k] + '-' + newThird[k:]
        elif backtrack[i][j][k] == 5:
            i = i - 1
            k = k - 1
            newSecond = newSecond[:j] + '-' + newSecond[j:]
        elif backtrack[i][j][k] == 6:
            j = j - 1
            k = k - 1
            newFirst = newFirst[:i] + '-' + newFirst[i:]
        else:
            i = i - 1
            j = j - 1
            k = k - 1

    while len(newFirst) != max(len(newFirst), len(newSecond), len(newThird)):
        newFirst = '-' + newFirst
    while len(newSecond) != max(len(newFirst), len(newSecond), len(newThird)):
        newSecond = '-' + newSecond
    while len(newThird) != max(len(newFirst), len(newSecond), len(newThird)):
        newThird = '-' + newThird

    return newFirst, newSecond, newThird

if __name__ == '__main__':

    x = '''ATATCCG
TCCGA
ATGTACTG'''
    inlines = x.split('\n')
    first = inlines[0]
    second = inlines[1]
    third = inlines[2]
    res = multiplealignment(first, second,third)
    print(res)

    x = '''TGTTTAAAAATGTCCGCAACCATTTC
GATATAAAACAGGGATAACTGCAATGG
CCTGCTACTTTATGCCGTCTCCATATGCG'''
    inlines = x.split('\n')
    first = inlines[0]
    second = inlines[1]
    third = inlines[2]
    res = multiplealignment(first, second,third)
    print(res)

    x = '''GTGTTGATAGCATCAGCCGAGTTGGCT
AGAAGTCTGACTGCTTCCCCATGTTGC
TCTGCTCAAGAAGAACGTATGATATGG'''
    inlines = x.split('\n')
    first = inlines[0]
    second = inlines[1]
    third = inlines[2]
    res = multiplealignment(first, second,third)
    print(res)
