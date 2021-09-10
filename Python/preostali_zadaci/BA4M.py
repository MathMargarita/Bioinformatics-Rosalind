"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Solve the Turnpike Problem
Rosalind ID: BA4M
URL: http://rosalind.info/problems/ba4m/
"""
import itertools
def turnpike(L,n):
    maxval=L[-1]
    #itertools.combinations(L,n) gives n-tuples of elements from L
    sets=list(itertools.combinations(L,n-2))
    for set_ in sets:
        L_new = []
        setconstr = []

        setconstr.append(maxval)
        setconstr.append(0)
        for e in set_:
            setconstr.append(e)
        setconstr.sort()

        for i in range(n):
            for j in range(i+1,n):
                L_new.append(setconstr[j]-setconstr[i])
        L_new.sort()

        #checking solution
        if L==L_new:
            for i in range (0,len(setconstr)):
                setconstr[i]=str(setconstr[i])
            return " ".join(setconstr)

    return None

if __name__ == '__main__':
    x = '''-10 -8 -7 -6 -5 -4 -3 -3 -2 -2 0 0 0 0 0 2 2 3 3 4 5 6 7 8 10'''
    x = x.split(" ")
    input=[]
    n=0
    for num in x:
        if int(num)==0:
            n+=1
        elif int(num)>0:
            input.append(int(num))
    res=turnpike(input,n)
    print(res)
    print(res == '''0 2 4 7 10''')
