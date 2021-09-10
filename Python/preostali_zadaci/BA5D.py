"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find the Longest Path in a DAG
Rosalind ID: BA5D
URL: http://rosalind.info/problems/ba5d/
"""

def Paths(Graph, i, j,path,L):
    if i==j:
        L.append(path)
        return
    if i not in Graph.keys():
        return

    for node in Graph[i]:
        Path=path.copy()
        Path.append([i,node[0],int(node[1])])
        Paths(Graph,node[0],j,Path,L)

    return L

def LongestPath(L):
    sums=[]
    for l in L:
        s=0
        for edge in l:
            s+=edge[2]
        sums.append(s)
    maxval=max(sums)
    i=sums.index(maxval)

    ret=[L[i][0][0]]
    for e in L[i]:
        ret.append(e[1])

    return maxval,"->".join(ret)

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
    paths=Paths(graph,i,j,[],[])
    res=LongestPath(paths)
    print(res[0])
    print(res[1])

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
    paths = Paths(graph, i, j, [], [])
    res = LongestPath(paths)
    print(res[0])
    print(res[1])

    x = '''3
33
11->12:33
9->27:9
20->25:17
32->33:0
28->31:34
11->18:36
14->23:27
12->19:20
15->31:37
15->32:26
4->22:32
10->12:10
1->29:20
12->14:13
4->28:17
2->33:32
5->11:37
0->17:32
18->19:35
0->15:16
23->30:3
17->25:25
2->6:30
3->25:32
22->34:35
2->18:20
22->33:34
9->34:16
23->24:14
19->31:24
16->22:11
18->25:39
24->34:8
16->28:9
21->22:15
25->33:33
20->31:6
15->21:29
20->33:38
0->4:15
22->29:4
27->31:39
5->14:9
0->20:25
13->25:12
22->24:8
13->32:13
13->31:26
17->31:4
18->22:21'''
    inlines = x.split("\n")
    i = inlines[0]
    j = inlines[1]
    graph = dict()
    for k in inlines[2:]:
        pair = k.split("->")
        if pair[0] not in graph.keys():
            graph[pair[0]]=[]
        graph[pair[0]].append(pair[1].split(":"))
    paths=Paths(graph,i,j,[],[])
    res=LongestPath(paths)
    print(res[0])
    print(res[1])


