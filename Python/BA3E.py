"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Construct the De Bruijn Graph of a Collection of k-mers
Rosalind ID: BA3E
URL: http://rosalind.info/problems/ba3e/
"""

def prefix(pattern):
    """substring of pattern without  the last letter"""
    return pattern[0:len(pattern)-1]

def suffix(pattern):
    #substring of pattern without first letter
    return pattern[1:]

def DeBrujinRec(Patterns):
    adjacency = dict()
    sortedPattern = sorted(Patterns)
    for pattern in sortedPattern:
        adjacency[prefix(pattern)] = []
    for pattern in sortedPattern:
        adjacency[prefix(pattern)].append(suffix(pattern))
    return adjacency

def multipleGraphPrint(adj):
    for key in adj.keys():
        print(key,'->',",".join(adj[key]))

if __name__ == '__main__':

    x='GAGG\nCAGG\nGGGG\nGGGA\nCAGG\nAGGG\nGGAG'
    inlines=x.split()
    res=DeBrujinRec(inlines)
    multipleGraphPrint(res)