"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a k-Universal Circular String
Rosalind ID: BA3I
URL: http://rosalind.info/problems/ba3i/
"""
def binaryString(k):
    def generateAllBinaryStrings(n, arr, i):
        if i == n:
            binstr.append("".join(arr))
            return

        arr[i] = '0'
        generateAllBinaryStrings(n, arr, i + 1)

        arr[i] = '1'
        generateAllBinaryStrings(n, arr, i + 1)
    binstr=[]
    generateAllBinaryStrings(k,[None]*k,0)
    return binstr

def graph(adj):
    adjDict=dict()
    for x in adj:
        x=x.split()
        adjDict[x[0]]=x[2].split(",")
    return adjDict


def cycles(adjDict):
    edgesDict=dict()
    for key in adjDict.keys():
        edgesDict[key]=[(key,value) for value in adjDict[key]]
    cycles=[]
    import random
    index=random.randint(0,len(adjDict.keys())-1)
    v0=[key for key in adjDict.keys()][index]
    def oneCycle():
        cyclev0 = []
        for node in adjDict[v0]:
            if (v0, node) not in cyclev0:
                if (v0, node) in edgesDict[v0]:
                    cyclev0.append((v0, node))
                    edgesDict[v0].remove((v0, node))
                    nodesv0.append(node)
                    startNode = node
                    break
        while (startNode != v0):
            for node in adjDict[startNode]:
                if (startNode, node) not in cyclev0:
                    if (startNode, node) in edgesDict[startNode]:
                        cyclev0.append((startNode, node))
                        edgesDict[startNode].remove((startNode, node))
                        nodesv0.append(node)
                        startNode = node
                        break
        cycles.append(cyclev0)

    nodesv0 = [v0]
    oneCycle()
    flag=0
    for i in range(1, len(nodesv0)):
        if len(edgesDict[nodesv0[i]]) > 0:
            v0 = nodesv0[i]
            flag = 1
            break
    while (flag > 0):
        nodesv0 = [v0]
        oneCycle()
        cycles = [EulerianCycle(cycles)]
        flag=0
        nodesv0=[cycles[0][0][0]]
        for element in cycles[0]:
            nodesv0.append(element[1])
        for i in range(1, len(nodesv0)):
            if len(edgesDict[nodesv0[i]]) > 0:
                v0 = nodesv0[i]
                flag = 1
                break
    return  cycles

def EulerianCycle(cycles):
    EulerianCycle=[]
    remove = []
    for element in cycles[0]:
        EulerianCycle.append(element)
        remove.append(element)
        if element[1] == cycles[1][0][0]:
            break
    for element in remove:
        cycles[0].remove(element)

    for i in range(1,-1,-1):
        remove=[]
        for element in cycles[i]:
            EulerianCycle.append(element)
            remove.append(element)
        for element in remove:
            cycles[i].remove(element)

    return EulerianCycle

def printUniversal(eulerianCycle):
    nodes=[eulerianCycle[0][0][0]]
    for x in eulerianCycle[0]:
        nodes.append(x[1][-1])
    return ("".join(nodes[:-len(eulerianCycle[0][0][0])]))


def prefix(pattern):
    """substring of pattern without  the last letter"""
    return pattern[0:len(pattern)-1]

def suffix(pattern):
    #substring of pattern without first letter
    return pattern[1:]

def graphFromStrings(inlines):
    text=""
    nodes=[]
    adj=dict()
    for x in inlines:
        nodes.append(prefix(x))
        nodes.append(suffix(x))
    nodes=list(set(nodes))
    for node in nodes:
        adj[node]=[]
    for node in nodes:
        for x in inlines:
            if prefix(x)==node:
                adj[node].append(suffix(x))
    for key in adj.keys():
        if len(adj[key])>0:
            text=text+key+" -> "+",".join(adj[key])+"\n"
    return text[:-1]

if __name__ == '__main__':

    x = '4'
    k=int(x)
    nodes = graphFromStrings(binaryString(k)).split("\n")
    res = printUniversal(cycles(graph(nodes)))
    print(res)

    x = '14'
    k=int(x)
    nodes = graphFromStrings(binaryString(k)).split("\n")
    res = printUniversal(cycles(graph(nodes)))
    print(res)

    x = '9'
    k=int(x)
    nodes = graphFromStrings(binaryString(k)).split("\n")
    res = printUniversal(cycles(graph(nodes)))
    print(res)
