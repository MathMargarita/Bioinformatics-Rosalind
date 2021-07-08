"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement 2-BreakOnGenomeGraph
Rosalind ID: BA6J
URL: http://rosalind.info/problems/ba6j/
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

if __name__ == '__main__':
    x = '''(2, 4), (3, 8), (7, 5), (6, 1)
1, 6, 3, 8'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split("), (")
    for i in range(len(p)):
        a = p[i].split(", ")
        p[i] = (int(a[0]), int(a[1]))
    indices = inlines[1].split(", ")
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    #print(p)
    res = BreakOnGenomeGraph(p, indices[0], indices[1], indices[2], indices[3])
    for i in range(len(res)):
        res[i] = str(res[i])
    res = ", ".join(res)
    print(res)

    x = '''(2, 4), (3, 5), (6, 8), (7, 10), (9, 12), (11, 13), (14, 15), (16, 17), (18, 19), (20, 21), (22, 24), (23, 25), (26, 28), (27, 30), (29, 32), (31, 33), (34, 35), (36, 37), (38, 40), (39, 42), (41, 44), (43, 45), (46, 47), (48, 49), (50, 51), (52, 53), (54, 56), (55, 58), (57, 59), (60, 61), (62, 64), (63, 66), (65, 68), (67, 69), (70, 72), (71, 73), (74, 75), (76, 77), (78, 80), (79, 81), (82, 83), (84, 86), (85, 88), (87, 90), (89, 92), (91, 94), (93, 96), (95, 98), (97, 99), (100, 102), (101, 104), (103, 106), (105, 107), (108, 109), (110, 111), (112, 113), (114, 116), (115, 117), (118, 120), (119, 121), (122, 124), (123, 126), (125, 128), (127, 129), (130, 132), (131, 134), (133, 136), (135, 1)
87, 90, 74, 75'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split("), (")
    for i in range(len(p)):
        a = p[i].split(", ")
        p[i] = (int(a[0]), int(a[1]))
    indices = inlines[1].split(", ")
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    res = BreakOnGenomeGraph(p, indices[0], indices[1], indices[2], indices[3])
    for i in range(len(res)):
        res[i] = str(res[i])
    res = ", ".join(res)
    print(res)

    x = '''(2, 3), (4, 6), (5, 8), (7, 10), (9, 12), (11, 14), (13, 15), (16, 18), (17, 20), (19, 21), (22, 23), (24, 26), (25, 28), (27, 29), (30, 31), (32, 33), (34, 35), (36, 38), (37, 39), (40, 41), (42, 43), (44, 45), (46, 48), (47, 50), (49, 52), (51, 54), (53, 55), (56, 57), (58, 59), (60, 62), (61, 64), (63, 66), (65, 68), (67, 69), (70, 71), (72, 73), (74, 75), (76, 77), (78, 79), (80, 82), (81, 83), (84, 85), (86, 87), (88, 90), (89, 92), (91, 93), (94, 95), (96, 97), (98, 100), (99, 101), (102, 104), (103, 105), (106, 107), (108, 110), (109, 111), (112, 114), (113, 116), (115, 117), (118, 120), (119, 122), (121, 123), (124, 125), (126, 127), (128, 130), (129, 131), (132, 133), (134, 136), (135, 138), (137, 139), (140, 1)
119, 122, 30, 31'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split("), (")
    for i in range(len(p)):
        a = p[i].split(", ")
        p[i] = (int(a[0]), int(a[1]))
    indices = inlines[1].split(", ")
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    res = BreakOnGenomeGraph(p, indices[0], indices[1], indices[2], indices[3])
    for i in range(len(res)):
        res[i] = str(res[i])
    res = ", ".join(res)
    print(res)