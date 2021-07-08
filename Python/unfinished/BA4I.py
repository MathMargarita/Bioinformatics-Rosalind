"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement ConvolutionCyclopeptideSequencing
Rosalind ID: BA4I
URL: http://rosalind.info/problems/ba4i/
"""
def get_amino_acid_mass():
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }
    return mass

def Mass(peptide):
    aa_masses=get_amino_acid_mass()
    sumMass=0
    for a in peptide:
        if a in aa_masses.keys():
            sumMass=sumMass+aa_masses[a]
    return sumMass

def Expand(peptides):
    newPeptides=[]
    for peptide in peptides:
        for a in get_amino_acid_mass().keys():
            newPeptides.append(peptide+a)
    return newPeptides

def LinearspectrumList(peptide):
    subPeptides=['',peptide]
    for i in range (1,len(peptide)):
        for j in range(0,len(peptide)-i+1):
            subPeptides.append(peptide[j:j+i])
    spectrum=[]
    for pep in subPeptides:
        spectrum.append(Mass(pep))
    spectrum.sort()
    return spectrum

def LinearScore(peptide,Spectrum):
    spectrum = Spectrum.split()
    for i in range(len(spectrum)):
        spectrum[i] = int(spectrum[i])
    counter=0
    spec=spectrum.copy()
    for value in LinearspectrumList(peptide):
        if value in spec:
            counter=counter+1
            spec.remove(value)
    return counter

def Trim(Leaderboard,Spectrum,N):
    spectrum = Spectrum.split()
    for i in range(len(spectrum)):
        spectrum[i] = int(spectrum[i])
    LinearScores=[]
    for j in range (len(Leaderboard)):
        Peptide=Leaderboard[j]
        LinearScores.append(LinearScore(Peptide,Spectrum))
    #sorting two list according to one
    LinearScores, Leaderboard = (list(t) for t in zip(*sorted(zip(LinearScores, Leaderboard),reverse=True)))
    for j in range(N, len(Leaderboard)):
        if LinearScores[j]<LinearScores[N-1]:
            for i in range(len(Leaderboard)-j):
                Leaderboard.pop()
            break
    return Leaderboard

def LeaderboardCyclopeptideSequencing(Spectrum,N):
    spectrum=Spectrum.split()
    for i in range (len(spectrum)):
        spectrum[i]=int(spectrum[i])
    Leaderboard=['']
    LeaderPeptide=''
    while len(Leaderboard)>0:
        removeList=[]
        Leaderboard=Expand(Leaderboard)
        for peptide in Leaderboard:
            if Mass(peptide)==spectrum[-1]:
                if LinearScore(peptide,Spectrum)>LinearScore(LeaderPeptide,Spectrum):
                    LeaderPeptide=peptide
            else:
                if Mass(peptide)>spectrum[-1]:
                    removeList.append(peptide)
        for x in removeList:
            Leaderboard.remove(x)
        if (len(Leaderboard)<=0):
            break
        Leaderboard=Trim(Leaderboard,Spectrum,N)
    return "-".join([str(get_amino_acid_mass()[a]) for a in LeaderPeptide])

if __name__ == '__main__':
    x='''10
0 71 113 129 147 200 218 260 313 331 347 389 460'''
    inlines=x.split("\n")
    N=int(inlines[0])
    Spectrum=inlines[1]
    res=LeaderboardCyclopeptideSequencing(Spectrum,N)
    print (res)
    print(res=="113-147-71-129")

    x = '''20
60
57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493'''
    inlines = x.split("\n")
    M = int(inlines[0])
    N = int(inlines[1])
    Spectrum = inlines[2]
    res = LeaderboardCyclopeptideSequencing(Spectrum, N)
    print(res)
    print(res == "97-129-97-147-99-71-186-71-113-163-115-71-113-128-103-87-128-101-137-163-114")

