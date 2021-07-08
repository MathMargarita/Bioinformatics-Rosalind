"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find the Longest Path in a DAG
Rosalind ID: BA5D
URL: http://rosalind.info/problems/ba5d/
"""
def LCSBacktrack(v,w):
    Backtrack=[]
    s = []
    for i in range(len(v)+1):
        s.append([0])
    for j in range(1, len(w)+1):
        s[0].append(0)

    for i in range(0,len(v)):
        Backtrack.append([])

    for i in range (1,len(v)+1):
        for j in range(1, len(w)+1):
            if v[i-1]==w[j-1]:
                s[i].append(max([s[i-1][j],s[i][j-1],s[i-1][j-1]+1]))
            else:
                s[i].append(max([s[i - 1][j], s[i][j - 1],s[i-1][j-1]]))
            if s[i][j]==s[i-1][j]:
                Backtrack[i-1].append("D")
            else:
                if s[i][j] == s[i][j-1]:
                    Backtrack[i-1].append("R")
                else:
                    Backtrack[i-1].append("Diag")
    return Backtrack

def OutputLCS(Backtrack, v, i, j,final):
    if i==-1 or j==-1:
        print(final[::-1])
        return
    if Backtrack[i][j]=="D":
        OutputLCS(Backtrack, v, i -1, j,final)
    else:
        if Backtrack[i][j]=="R":
            OutputLCS(Backtrack, v, i, j -1,final)
        else:
            final = final + v[i]
            OutputLCS(Backtrack, v, i -1, j -1,final)

def TopologicalOrdering(Graph):
    List = []
    Outgoing = []
    for v in Graph.values():
        Outgoing=Outgoing+v
    Outgoing=set(Outgoing)
    Candidates=[]
    for k in Graph.keys():
        if k not in Outgoing:
            Candidates.append(k)
    while len(Candidates)>0:
        a=Candidates[0]
        List.append(a)
        Candidates.remove(a)
        if a in Graph.keys():
            d=len(Graph[a])
            for i in range (d):
                b=Graph[a][0]
                Graph[a].pop(0)
                Outgoing=[]
                for v in Graph.values():
                    Outgoing = Outgoing + v
                Outgoing = set(Outgoing)
                if b not in Outgoing:
                    Candidates.append(b)

    for k in Graph.keys():
        if len(Graph[k])>0:
            return "the input graph is not a DAG"
    return ", ".join(List)

def Paths(Graph, i, j,path):
    if i not in Graph.keys():
        if i==j:
            return
        return

    for node in Graph[i]:
        path.append([i,node[0]])
        Paths(Graph,node[0],j,path)


    return path

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1500)
    x = '''0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3'''
    inlines = x.split("\n")
    i = inlines[0]
    j = inlines[1]
    graph = dict()
    for k in inlines[2:]:
        pair = k.split("->")
        if pair[0] not in graph.keys():
            graph[pair[0]]=[]
        graph[pair[0]].append(pair[1].split(":"))
    print(Paths(graph,i,j,[]))
    #res = OutputLCS(LCSBacktrack(v, w), v, len(v)- 1, len(w) - 1, "")

    x = '''0
44
6->26:32
10->39:30
26->28:24
3->16:19
10->35:35
10->37:19
10->31:36
10->33:32
10->32:4
15->23:0
15->21:0
22->24:0
22->27:31
1->3:36
5->43:37
8->30:23
19->34:11
12->13:38
39->40:35
12->15:29
27->29:13
1->42:31
24->25:2
1->10:4
4->30:11
13->35:17
24->28:2
23->25:37
31->43:7
31->40:17
3->28:2
5->12:39
5->11:37
3->4:4
2->31:23
14->29:13
19->27:21
27->36:20
31->33:23
30->40:27
28->42:29
21->35:33
21->37:5
20->37:24
2->9:38
0->14:19
4->20:0
1->41:8
8->14:28
19->20:13
4->43:3
14->31:25
14->30:22
13->41:19
13->40:32
14->35:10
10->11:5
14->38:23
2->23:9
2->25:1
24->40:37
12->38:38
20->23:34
20->21:29
12->30:10
12->37:12
29->44:30
33->35:15
33->37:22
0->36:8
37->38:17
10->29:13
17->44:11
6->14:5
10->22:8
22->37:19
22->34:3
32->43:4
15->36:28
11->35:20
2->16:27
7->10:22
11->31:19
16->41:24
15->30:25
32->37:29
0->27:9
0->28:7
32->38:0
12->43:5
22->35:37
24->30:7
24->32:19
24->38:38'''
    inlines = x.split("\n")
    i = inlines[0]
    j = inlines[1]
    graph = dict()
    for k in inlines[2:]:
        pair = k.split("->")
        if pair[0] not in graph.keys():
            graph[pair[0]] = []
        graph[pair[0]].append(pair[1].split(":"))
    print(Paths(graph, i, j, []))



