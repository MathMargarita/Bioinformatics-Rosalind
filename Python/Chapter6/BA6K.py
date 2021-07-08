"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement 2-BreakOnGenomeGraph
Rosalind ID: BA6J
URL: http://rosalind.info/problems/ba6j/
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

def ColoredEdges(P):
    Edges = []
    for Chromosome in P:
        Nodes = ChromosomeToCycle(Chromosome)
        for j in range(len(Chromosome)):
            Edges.append((Nodes[2 * j + 1], Nodes[(2 * j + 2) % len(Nodes)]))
    return Edges

def BreakOnGenomeGraph(GenomeGraph, i, I, j, J):
     if (i,I) in GenomeGraph:
         GenomeGraph.remove((i,I))
     else:
         if (I,i) in GenomeGraph:
             GenomeGraph.remove((I, i))
     if (j,J) in GenomeGraph:
         GenomeGraph.remove((j,J))
     else:
         if (J,j) in GenomeGraph:
             GenomeGraph.remove((J, j))
     GenomeGraph.append((i,j))
     GenomeGraph.append((I,J))
     return GenomeGraph

def CycleToChromosome(Nodes):
    Chromosome=[]
    k=int(len(Nodes)/2)
    for j in range(0,k):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome.append(int(Nodes[2*j+1]/2))
        else:
            Chromosome.append(int(-Nodes[2*j]/2))
    return Chromosome

def GraphToGenome(GenomeGraph):
     P=[]
     for Nodes in GenomeGraph:
          Chromosome=CycleToChromosome(Nodes)
          P.append(Chromosome)
     return P

def PairsToGraph(p):
    graph = []
    start = 0
    P=p.copy()
    while len(P)>0:
        cycle=[P[start]]
        P.remove(P[start])
        while True:
            if cycle[-1][1]%2==0:
                for pair in P:
                    if cycle[-1][1]-1 in pair:
                        if cycle[-1][1]-1 == pair[0]:
                            cycle.append((pair[0],pair[1]))
                        else:
                            cycle.append((pair[1],pair[0]))
                        P.remove(pair)
                        break
            else:
                for pair in P:
                    if cycle[-1][1]+1 in pair:
                        if cycle[-1][1] + 1 == pair[0]:
                            cycle.append((pair[0], pair[1]))
                        else:
                            cycle.append((pair[1], pair[0]))
                        P.remove(pair)
                        break
            if cycle[0][0] % 2 == 0:
                if cycle[0][0] - 1 in cycle[-1]:
                    break
            else:
                if cycle[0][0] + 1 in cycle[-1]:
                    break
        Cycle=[cycle[0][1]]
        for i in range (1,len(cycle)):
            Cycle.append(cycle[i][0])
            Cycle.append(cycle[i][1])
        Cycle.append(cycle[0][0])
        graph.append(Cycle)
    return graph

def BreakOnGenome(P,i,I,j,J):
    GenomeGraph=ColoredEdges(P)
    GenomeGraph=BreakOnGenomeGraph(GenomeGraph,i,I,j,J)
    P=GraphToGenome(PairsToGraph(GenomeGraph))
    return P

if __name__ == '__main__':
    x = '''(+1 -2 -4 +3)
1, 6, 3, 8'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    p = [p]
    indices = inlines[1].split(", ")
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    res = BreakOnGenome(p, indices[0], indices[1], indices[2], indices[3])
    for j in range(len(res)):
        for i in range(len(res[j])):
            if res[j][i] > 0:
                res[j][i] = "+" + str(res[j][i])
            else:
                res[j][i] = str(res[j][i])
        res[j] = " ".join(res[j])
        res[j] = "(" + res[j] + ")"
    res = "".join(res)
    print(res)

    x = '''(-1 +2 -3 -4 -5 -6 -7 +8 +9 +10 +11 +12 +13 +14 +15 -16 -17 -18 +19 -20 +21 +22 -23 -24 +25 -26 -27 +28 -29 -30 +31 +32 +33 -34 -35 +36 +37 +38 +39 -40 +41 +42 -43 +44 +45 +46 -47 +48 +49 +50 -51 +52 +53 +54 -55 -56 -57 +58 -59 -60 -61 +62 -63 +64 +65 -66 -67)
116, 118, 73, 72'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    p = [p]
    indices = inlines[1].split(", ")
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    res = BreakOnGenome(p, indices[0], indices[1], indices[2], indices[3])
    for j in range(len(res)):
        for i in range(len(res[j])):
            if res[j][i] > 0:
                res[j][i] = "+" + str(res[j][i])
            else:
                res[j][i] = str(res[j][i])
        res[j] = " ".join(res[j])
        res[j] = "(" + res[j] + ")"
    res = "".join(res)
    print(res)

    x = '''(+1 +2 -3 -4 -5 +6 +7 -8 -9 +10 +11 -12 +13 +14 -15 -16 -17 -18 -19 +20 +21 +22 +23 +24 -25 -26 +27 -28 -29 +30 +31 +32 -33 -34 +35 -36 -37 -38 -39 -40 +41 +42 -43 +44 -45 +46 -47 +48 +49 -50 +51 -52 +53 -54 -55 -56 +57 +58 +59 -60 +61 -62 -63 -64 +65 +66 +67 +68 -69 +70)
21, 20, 43, 42'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    p = [p]
    indices = inlines[1].split(", ")
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    res = BreakOnGenome(p, indices[0], indices[1], indices[2], indices[3])
    for j in range(len(res)):
        for i in range(len(res[j])):
            if res[j][i] > 0:
                res[j][i] = "+" + str(res[j][i])
            else:
                res[j][i] = str(res[j][i])
        res[j] = " ".join(res[j])
        res[j] = "(" + res[j] + ")"
    res = "".join(res)
    print(res)