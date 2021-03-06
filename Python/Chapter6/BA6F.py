"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement ChromosomeToCycle
Rosalind ID: BA6F
URL: http://rosalind.info/problems/ba6f/
"""

def ChromosomeToCycle(Chromosome):
    Nodes=[]
    for j in range(0,len(Chromosome)):
        i=Chromosome[j]
        if i > 0:
            Nodes.append(2*i-1)
            Nodes.append(2*i)
        else:
            Nodes.append(-2*i) #minus because i is negative
            Nodes.append(-2*i-1)
    return Nodes

if __name__ == '__main__':
    x = '''(+1 -2 -3 +4)'''
    x = x[1:-1]
    p = x.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    res = ChromosomeToCycle(p)
    for i in range(len(res)):
        res[i] = str(res[i])
    res = " ".join(res)
    res = "(" + res + ")"
    print(res)
    print(res == '''(1 2 4 3 6 5 7 8)''')

    x = '''(+1 +2 -3 -4 +5 -6 +7 +8 -9 +10 -11 -12 +13 -14 +15 -16 +17 +18 +19 -20 +21 -22 -23 -24 +25 +26 +27 -28 +29 -30 -31 +32 +33 +34 -35 +36 +37 +38 -39 +40 -41 -42 +43 -44 -45 -46 -47 +48 +49 -50 +51 -52 -53 -54 +55 +56 +57 -58 -59 -60 +61 +62 +63 -64 +65 +66 +67 -68 -69)'''
    x = x[1:-1]
    p = x.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    res = ChromosomeToCycle(p)
    for i in range(len(res)):
        res[i] = str(res[i])
    res = " ".join(res)
    res = "(" + res + ")"
    print(res)
    print(
        res == '''(1 2 3 4 6 5 8 7 9 10 12 11 13 14 15 16 18 17 19 20 22 21 24 23 25 26 28 27 29 30 32 31 33 34 35 36 37 38 40 39 41 42 44 43 46 45 48 47 49 50 51 52 53 54 56 55 57 58 60 59 62 61 63 64 65 66 67 68 70 69 71 72 73 74 75 76 78 77 79 80 82 81 84 83 85 86 88 87 90 89 92 91 94 93 95 96 97 98 100 99 101 102 104 103 106 105 108 107 109 110 111 112 113 114 116 115 118 117 120 119 121 122 123 124 125 126 128 127 129 130 131 132 133 134 136 135 138 137)''')

    x = '''(-1 -2 +3 +4 +5 +6 +7 +8 -9 -10 +11 -12 -13 +14 -15 +16 -17 -18 -19 -20 -21 -22 +23 -24 +25 +26 -27 -28 +29 -30 -31 -32 -33 +34 +35 -36 +37 +38 -39 +40 -41 +42 +43 -44 +45 -46 -47 -48 -49 -50 +51 -52 +53 +54 +55 -56 +57 -58 -59 +60 +61)'''
    x=x[1:-1]
    p=x.split(" ")
    for i in range (len(p)):
        p[i]=int(p[i])
    res=ChromosomeToCycle(p)
    for i in range (len(res)):
        res[i]=str(res[i])
    res=" ".join(res)
    res="("+res+")"
    print(res)
