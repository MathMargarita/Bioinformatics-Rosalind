"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Generate All Maximal Non-Branching Paths in a Graph
Rosalind ID: BA3M
URL: http://rosalind.info/problems/ba3m/
"""

def graph2(adj):
    #Add all nodes as keys (even if they have not output degree > 0)
    adjDict=dict()
    for x in adj:
        x=x.split()
        adjDict[x[0]]=x[2].split(",")
        for node in x[2].split(","):
            if node not in adjDict.keys():
                adjDict[node]=[]
    return adjDict

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

def MaximalNonBranchingPathsPrint(paths):
    output=[]
    for x in paths:
        seq=x[0][0]+' -> '+x[0][1]
        for y in x[1:]:
            seq=seq+' -> '+y[1]
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
        if (inputDeg!=1 or len(graph[key])!=1):
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

    x='''1 -> 2
2 -> 3
3 -> 4,5
6 -> 7
7 -> 6'''
    inlines=x.split('\n')
    res=MaximalNonBranchingPathsPrint(MaximalNonBranchingPaths(graph2(inlines)))
    print(res)