"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Topological Ordering of a DAG
Rosalind ID: BA5N
URL: http://rosalind.info/problems/ba5n/
"""
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


if __name__ == '__main__':
    x = '''1 -> 2
2 -> 3
4 -> 2
5 -> 3'''
    inlines = x.split("\n")
    graph = dict()
    for i in inlines:
        pair = i.split(" -> ")
        graph[pair[0]] = pair[1].split(",")
    res = TopologicalOrdering(graph)
    print(res)
    print(res == '''1, 4, 5, 2, 3''')

    x = '''0 -> 13,16,20,22,4,5
1 -> 12,13,16,17,19,22,23,24,25,3,4
10 -> 13,14,17,20,23,24
11 -> 12,19,20,22,23
12 -> 15,20,24
13 -> 20,21,22
15 -> 23
17 -> 25
19 -> 20,25
2 -> 16,19,3,7
20 -> 22,23
21 -> 22,23,24
22 -> 25
24 -> 25
3 -> 15,21,4
4 -> 10,12,14,15,16,17,18,19,21,23,5
5 -> 11,16,17,20,23,8,9
6 -> 12,14,18,22
7 -> 14,17,22
8 -> 21,24
9 -> 12,14'''
    inlines = x.split("\n")
    graph = dict()
    for i in inlines:
        pair = i.split(" -> ")
        graph[pair[0]] = pair[1].split(",")
    res = TopologicalOrdering(graph)
    print(res)

    x = '''1 -> 16,17,2,9
10 -> 34
11 -> 30,39
12 -> 39
13 -> 15,30,33
14 -> 38
15 -> 37
16 -> 38
18 -> 37,39
2 -> 22,35,38
21 -> 37,39,40
22 -> 27,31,37
23 -> 37
25 -> 34
26 -> 27,33,34,35,41
28 -> 39
3 -> 20,27,5
31 -> 39
33 -> 35,38
38 -> 39
4 -> 30,7
5 -> 36
6 -> 22
7 -> 10,18
8 -> 19,20,22,38
9 -> 24'''
    inlines = x.split("\n")
    graph = dict()
    for i in inlines:
        pair = i.split(" -> ")
        graph[pair[0]] = pair[1].split(",")
    res = TopologicalOrdering(graph)
    print(res)
