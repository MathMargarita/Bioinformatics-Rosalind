"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Shortest Transformation of One Genome into Another by 2-Breaks
Rosalind ID: BA6D
URL: http://rosalind.info/problems/ba6d/
"""

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
     Edges=[]
     for Chromosome in P:
          Nodes=ChromosomeToCycle(Chromosome)
          for j in range(len(Chromosome)):
               Edges.append((Nodes[2*j+1], Nodes[(2*j+2)%len(Nodes)]))
     return Edges

def BreakOnGenome(P,i,I,j,J):###################################################
    GenomeGraph=ColoredEdges(P)
    GenomeGraph=BreakOnGenomeGraph(GenomeGraph,i,I,j,J)
    P=GraphToGenome(PairsToGraph(GenomeGraph))
    return P

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
    P = []
    for Nodes in GenomeGraph:
        Chromosome = CycleToChromosome(Nodes)
        P.append(Chromosome)
    return P


def PairsToGraph(p):
    graph = []
    start = 0
    P = p.copy()
    while len(P) > 0:
        cycle = [P[start]]
        P.remove(P[start])
        while True:
            if cycle[-1][1] % 2 == 0:
                for pair in P:
                    if cycle[-1][1] - 1 in pair:
                        if cycle[-1][1] - 1 == pair[0]:
                            cycle.append((pair[0], pair[1]))
                        else:
                            cycle.append((pair[1], pair[0]))
                        P.remove(pair)
                        break
            else:
                for pair in P:
                    if cycle[-1][1] + 1 in pair:
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
        Cycle = [cycle[0][1]]
        for i in range(1, len(cycle)):
            Cycle.append(cycle[i][0])
            Cycle.append(cycle[i][1])
        Cycle.append(cycle[0][0])
        graph.append(Cycle)
    return graph

def ShortestRearrangementScenario(P, Q):
    l=[P]
    RedEdges=ColoredEdges(P)
    BlueEdges=ColoredEdges(Q)
    numberOfTrivialCycles=0
    for red in RedEdges:
        if red in BlueEdges or (red[1],red[0]) in BlueEdges:
            numberOfTrivialCycles=+1
    BLUE=BlueEdges.copy()
    while numberOfTrivialCycles<len(BlueEdges):
        for blue in BLUE:
            if blue not in RedEdges and (blue[1],blue[0]) not in RedEdges:
                j=blue[0]
                I=blue[1]
                BLUE.remove(blue)
                break
        for red in RedEdges:
            if j in red:
                if red[0]==j:
                    i=red[1]
                    RedEdges.remove((j, i))
                else:
                    i=red[0]
                    RedEdges.remove((i, j))
                break
        for red in RedEdges:
            if I in red:
                if I==red[0]:
                    J=red[1]
                    RedEdges.remove((I, J))
                else:
                    J=red[0]
                    RedEdges.remove((J, I))
                break
        RedEdges.append((j,I))
        RedEdges.append((J, i))
        numberOfTrivialCycles = 0
        for red in RedEdges:
            if red in BlueEdges or (red[1],red[0]) in BlueEdges:
                numberOfTrivialCycles = numberOfTrivialCycles+ 1
        P=GraphToGenome(PairsToGraph(RedEdges))
        l.append(P)
    return l


if __name__ == '__main__':
    x = '''(+1 -2 -3 +4)
(+1 +2 -4 -3)'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    edges = inlines[1]
    edges = edges[1:-1]
    q = edges.split(" ")
    for i in range(len(q)):
        q[i] = int(q[i])

    res = ShortestRearrangementScenario([p], [q])
    RES = []
    for r in res:
        for i in range(len(r)):
            for j in range(len(r[i])):
                if r[i][j] > 0:
                    r[i][j] = "+" + str(r[i][j])
                else:
                    r[i][j] = str(r[i][j])
            r[i] = " ".join(r[i])
            r[i] = "(" + r[i] + ")"
        r = " ".join(r)
        RES.append(r)
    print("\n".join(RES))

    x = '''(+9 -8 +12 +7 +1 -14 +13 +3 -5 -11 +6 -2 +10 -4)
(-11 +8 -10 -2 +3 +4 +13 +6 +12 +9 +5 +7 -14 -1)'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    edges = inlines[1]
    edges = edges[1:-1]
    q = edges.split(" ")
    for i in range(len(q)):
        q[i] = int(q[i])

    res = ShortestRearrangementScenario([p], [q])
    RES = []
    for r in res:
        for i in range(len(r)):
            for j in range(len(r[i])):
                if r[i][j] > 0:
                    r[i][j] = "+" + str(r[i][j])
                else:
                    r[i][j] = str(r[i][j])
            r[i] = " ".join(r[i])
            r[i] = "(" + r[i] + ")"
        r = " ".join(r)
        RES.append(r)
    print("\n".join(RES))

    x = '''(-7 -10 +4 -6 +8 +12 +13 +9 +14 +2 -11 -3 +5 -1 +15)
(+7 +4 -1 +10 -8 -2 +11 -6 +13 -9 +14 +3 -12 +5 -15)'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    edges = inlines[1]
    edges = edges[1:-1]
    q = edges.split(" ")
    for i in range(len(q)):
        q[i] = int(q[i])

    res = ShortestRearrangementScenario([p],[q])
    RES=[]
    for r in res:
        for i in range(len(r)):
            for j in range(len(r[i])):
                if r[i][j] > 0:
                    r[i][j] = "+" + str(r[i][j])
                else:
                    r[i][j] = str(r[i][j])
            r[i] = " ".join(r[i])
            r[i] = "(" + r[i] + ")"
        r = " ".join(r)
        RES.append(r)
    print("\n".join(RES))
