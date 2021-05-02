"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Generate Contigs from a Collection of Reads
Rosalind ID: BA3K
URL: http://rosalind.info/problems/ba3k/
"""

def prefix(pattern):
    """substring of pattern without  the last letter"""
    return pattern[0:len(pattern)-1]

def suffix(pattern):
    #substring of pattern without first letter
    return pattern[1:]

def DeBrujinRecAll(Patterns):
    #add all nodes as keys in adj dict (even if they haw output degree=0)
    adjacency = dict()
    for pattern in Patterns:
        adjacency[prefix(pattern)] = []
        adjacency[suffix(pattern)] = []
    for pattern in Patterns:
        adjacency[prefix(pattern)].append(suffix(pattern))
    return adjacency

def contigs(adj):
    def sequence(key,seq):
        if len(adj[key])==1:
            if adj[key][0] not in non1to1(adj):
                seq=seq+suffix(adj[key][0])
                sequence(adj[key][0],seq)
            else:
                contigs.append(seq+suffix(adj[key][0]))
                return
        else:
            if len(adj[key])>1:
                for val in adj[key]:
                    if val not in non1to1(adj):
                        sequence(val,key+suffix(val))
                    else:
                        contigs.append(seq+suffix(val))
                return
            else:
                contigs.append(seq)
                return

    contigs=[]
    for key in non1to1(adj):
        sequence(key,key)
    return contigs

def MaximalNonBranchingPaths(graph):
    Paths=[]
    for  v in non1to1(graph):
        if len(graph[v]) > 0:
            for w in graph[v]:
                NonBranchingPath=[[v,w]]
                while w not in non1to1(graph):
                    NonBranchingPath.append([w,graph[w][0]])
                    w=graph[w][0]
                Paths.append(NonBranchingPath)
    for cycle in isolatedCycles(graph):
        Paths.append(cycle)
    return Paths

def contigsPrint(paths):
    output=[]
    for x in paths:
        seq=x[0][0]+suffix(x[0][1])
        for y in x[1:]:
            seq=seq+suffix(y[1])
        output.append(seq)
    return '\n'.join(output)

def non1to1(graph):
    unbalancedNodes=[]
    for key in graph.keys():
        inputDeg=0
        for key2 in graph.keys():
            if key2!=key:
                for node in graph[key2]:
                    if node==key:
                        inputDeg=inputDeg+1
        if(inputDeg!=1 or len(graph[key])!=1):
            unbalancedNodes.append(key)
    return unbalancedNodes

def isolatedCycles(graph):
    Cycles=[]
    usedNodes=[]
    for key in graph.keys():
        if key not in usedNodes:
            if key not in non1to1(graph):
                if len(graph[key]) > 0:
                    usedNodes.append(key)
                    for w in graph[key]:
                        usedNodes.append(w)
                        path = [[key, w]]
                        while w not in non1to1(graph):
                            usedNodes.append(w)
                            if w==key:
                                Cycles.append(path)
                                break
                            path.append([w, graph[w][0]])
                            w = graph[w][0]
    return Cycles


if __name__ == '__main__':

    x='''ATG
ATG
TGT
TGG
CAT
GGA
GAT
AGA'''
    inlines=x.split()
    res=contigsPrint(MaximalNonBranchingPaths(DeBrujinRecAll(inlines)))
    print(res)
    print(sorted(res.split())==sorted('''AGA ATG ATG CAT GAT TGGA TGT'''.split()))

    x = '''TAA
    AAT
    ATG
    ATG
    ATG
    TGT
    GTT
    TGG
    GGG
    GGA
    GAT
    TGC
    GCC
    CCA
    CAT'''
    inlines = x.split()
    res = contigsPrint(MaximalNonBranchingPaths(DeBrujinRecAll(inlines)))
    #print(res)
    #print(sorted(res.split()) == sorted('''TAAT TGTT TGCCAT ATG ATG ATG TGG GGG GGAT'''.split()))