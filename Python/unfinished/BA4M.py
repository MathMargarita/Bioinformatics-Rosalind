"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Solve the Turnpike Problem
Rosalind ID: BA4M
URL: http://rosalind.info/problems/ba4m/
"""


def Factor(Delta):
    A=[]

    for i in range (len(A)):
        A[i]=str(A[i])
    return " ".join(A)

if __name__ == '__main__':
    x = '''-10 -8 -7 -6 -5 -4 -3 -3 -2 -2 0 0 0 0 0 2 2 3 3 4 5 6 7 8 10'''
    delta = x.split(" ")
    for i in range (len(delta)):
        delta[i]=int(delta[i])
    res = Factor(delta)
    print(res)
    print(res == '''0 2 4 7 10''')

