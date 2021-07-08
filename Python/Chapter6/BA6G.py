"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement CycleToChromosome
Rosalind ID: BA6G
URL: http://rosalind.info/problems/ba6g/
"""

def CycleToChromosome(Nodes):
    Chromosome=[]
    k=int(len(Nodes)/2)
    for j in range(0,k):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome.append(int(Nodes[2*j+1]/2))
        else:
            Chromosome.append(int(-Nodes[2*j]/2))
    return Chromosome

if __name__ == '__main__':
    x = '''(1 2 4 3 6 5 7 8)'''
    x = x[1:-1]
    p = x.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    res = CycleToChromosome(p)
    for i in range(len(res)):
        if res[i] > 0:
            res[i] = "+" + str(res[i])
        else:
            res[i] = str(res[i])
    res = " ".join(res)
    res = "(" + res + ")"
    print(res)
    print(res == '''(+1 -2 -3 +4)''')

    x = '''(1 2 3 4 5 6 8 7 9 10 11 12 14 13 15 16 17 18 19 20 21 22 23 24 26 25 27 28 29 30 31 32 33 34 36 35 37 38 39 40 41 42 43 44 45 46 48 47 49 50 52 51 54 53 56 55 57 58 60 59 61 62 63 64 65 66 68 67 70 69 72 71 73 74 76 75 77 78 79 80 81 82 83 84 85 86 87 88 89 90 92 91 93 94 96 95 97 98 100 99 102 101 103 104 106 105 108 107 109 110 111 112 113 114 115 116 118 117 120 119 122 121 123 124 125 126 128 127 130 129 132 131 133 134 136 135 137 138 140 139)'''
    x = x[1:-1]
    p = x.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    res = CycleToChromosome(p)
    for i in range(len(res)):
        if res[i] > 0:
            res[i] = "+" + str(res[i])
        else:
            res[i] = str(res[i])
    res = " ".join(res)
    res = "(" + res + ")"
    print(res)
    print(res == '''(+1 +2 +3 -4 +5 +6 -7 +8 +9 +10 +11 +12 -13 +14 +15 +16 +17 -18 +19 +20 +21 +22 +23 -24 +25 -26 -27 -28 +29 -30 +31 +32 +33 -34 -35 -36 +37 -38 +39 +40 +41 +42 +43 +44 +45 -46 +47 -48 +49 -50 -51 +52 -53 -54 +55 +56 +57 +58 -59 -60 -61 +62 +63 -64 -65 -66 +67 -68 +69 -70)''')

    x = '''(2 1 3 4 5 6 8 7 9 10 12 11 14 13 15 16 17 18 19 20 21 22 24 23 26 25 27 28 29 30 31 32 33 34 36 35 37 38 40 39 42 41 43 44 46 45 48 47 49 50 51 52 53 54 55 56 58 57 60 59 61 62 64 63 66 65 67 68 70 69 72 71 74 73 75 76 77 78 79 80 81 82 83 84 85 86 88 87 89 90 92 91 94 93 95 96 98 97 100 99 101 102 103 104 106 105 108 107 110 109 112 111 114 113 116 115 118 117 119 120 122 121 124 123 126 125 127 128 130 129 132 131 134 133 136 135)'''
    x = x[1:-1]
    p = x.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    res = CycleToChromosome(p)
    for i in range(len(res)):
        if res[i]>0:
            res[i] = "+"+str(res[i])
        else:
            res[i]=str(res[i])
    res = " ".join(res)
    res = "(" + res + ")"
    print(res)
