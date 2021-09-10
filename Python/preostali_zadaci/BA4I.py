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

def Mass1(peptide):
    aa_masses=get_amino_acid_mass()
    sumMass=0
    for a in peptide:
        if a in aa_masses.keys():
            sumMass=sumMass+aa_masses[a]
    return sumMass

def Mass(peptide):
    sumMass=0
    for a in peptide.split("-"):
        try:
            sumMass=sumMass+int(a)
        except:
            sumMass=sumMass

    return sumMass

def Expand(peptides,new_alphabet):
    newPeptides=[]

    for peptide in peptides:
        for a in new_alphabet:
            if len(peptide) > 0:
                newPeptides.append(peptide + '-' + a)
            else:
                newPeptides.append(peptide + a)

    return newPeptides

def LinearspectrumList(peptide):
    subPeptides=['',peptide]
    for i in range (1,len(peptide.split("-"))):
        for j in range(0,len(peptide.split("-"))-i+1):
            subPeptides.append("-".join(peptide.split("-")[j:j+i]))
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
    if (len(Leaderboard) <= 0):
        return Leaderboard
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

def LeaderboardCyclopeptideSequencing(Spectrum,N,new_alphabet):
    spectrum=Spectrum.split()
    for i in range (len(spectrum)):
        spectrum[i]=int(spectrum[i])
    Leaderboard1=[]
    Leaderboard=['']
    LeaderPeptide=''
    while len(Leaderboard)>0:
        removeList=[]
        Leaderboard=Expand(Leaderboard,new_alphabet)
        for peptide in Leaderboard:
            if Mass(peptide)==spectrum[-1]:
                if LinearScore(peptide,Spectrum)>LinearScore(LeaderPeptide,Spectrum):
                    LeaderPeptide=peptide
            else:
                if Mass(peptide)>spectrum[-1]:
                    removeList.append(peptide)
        for x in removeList:
            Leaderboard.remove(x)
        Leaderboard=Trim(Leaderboard,Spectrum,N)
        if len(Leaderboard)>0:
            Leaderboard1=Leaderboard.copy()

    for peptide in Leaderboard1:
        if Mass(peptide) == spectrum[-1]:
            if Score(peptide, Spectrum) > Score(LeaderPeptide, Spectrum):
                LeaderPeptide = peptide

    return LeaderPeptide

def CyclospectrumList(peptide):
    subPeptides=['',peptide]
    peptide1=peptide+"-"+peptide
    for i in range (1,len(peptide.split("-"))):
        for j in range(0,len(peptide.split("-"))):
            subPeptides.append("-".join(peptide1.split("-")[j:j+i]))
    spectrum=[]
    for pep in subPeptides:
        spectrum.append(Mass(pep))
    spectrum.sort()
    return spectrum

def Score(peptide,Spectrum):
    spectrum = Spectrum.split()
    for i in range(len(spectrum)):
        spectrum[i] = int(spectrum[i])
    counter=0
    for value in CyclospectrumList(peptide):
        if value in spectrum:
            counter=counter+1
            spectrum.remove(value)
    return counter

def Convolution(arr):
    arr = arr.split(" ")
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    l=[]
    for a in arr:
        for b in arr:
            if a-b>0:
                l.append(a-b)
    for i in range (len(l)):
        l[i]=str(l[i])
    l.sort()
    return " ".join(l)

def ConvolutionCyclopeptideSequencing(Spectrum,M,N):
    convolution=Convolution(Spectrum).split(" ")
    frequencies=dict()

    for x in convolution:
        if x in frequencies.keys():
            frequencies[x]+=1
        else:
            frequencies[x]=1

    keys=[]
    values=[]
    for x in frequencies.keys():
        if int(x)>=57 and int(x)<200:
            keys.append(x)
            values.append(frequencies[x])
    values, keys = (list(t) for t in zip(*sorted(zip(values, keys), reverse=True)))
    last=values[M-1]
    new_alphabet=[]
    for i in range (0,M):
        new_alphabet.append(keys[i])
    for i in range (M,len(values)):
        if values[i]==last:
            new_alphabet.append(keys[i])

    return LeaderboardCyclopeptideSequencing(Spectrum, N, new_alphabet)

if __name__ == '__main__':
    x = '''20
60
57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493'''
    inlines = x.split("\n")
    M = int(inlines[0])
    N = int(inlines[1])
    Spectrum = inlines[2]
    res = ConvolutionCyclopeptideSequencing(Spectrum, M, N)
    print(res)
    print(res=="99-71-137-57-72-57")

    x = '''20
373
853 113 585 796 924 502 423 1210 342 186 761 391 593 1412 1152 1396 260 129 1381 229 242 356 990 1047 57 748 1176 730 990 1038 1119 294 339 114 696 1251 1267 617 567 357 471 163 1266 1281 0 536 1395 454 1104 1362 1039 892 1509 1086 129 649 1095 713 258 777 1394 753 299 599 648 876 414 1249 813 242 859 1305 552 1284 861 650 1249 261 520 470 519 957 1233 405 260 861 762 810 1248 891 916 1346 390 981 147 1323 390 732 618 1380 1038 756 989 225 633 910 204 1452 243 1119 860 1395 129 57 503 1267 1153 276 462 228 1215 114 1170 357 973 388 519 699 131 128 1120 648 1452 1055 632 333 1380 528 747 389 656 97 1167 779 1380 1280 942 115 1121 1152 1007 990 1006 1118 519 877 1378 471'''
    inlines = x.split("\n")
    M = int(inlines[0])
    N = int(inlines[1])
    Spectrum = inlines[2]
    #res = ConvolutionCyclopeptideSequencing(Spectrum, M, N)
    #print(res)
    #print(res == "113-115-114-128-97-163-131-129-129-147-57-57-129")

    x='''18
339
0 71 87 87 97 113 115 128 128 129 131 131 147 163 174 184 202 202 215 226 228 244 259 275 276 278 289 291 302 315 315 330 341 346 357 365 373 404 406 412 417 417 433 438 443 446 452 470 493 501 504 504 530 541 543 548 553 567 574 580 580 617 617 619 632 640 661 664 671 672 682 688 708 711 727 732 745 748 758 769 779 782 795 800 816 819 839 845 855 856 863 866 887 895 908 910 910 947 947 953 960 974 979 984 986 997 1023 1023 1026 1034 1057 1075 1081 1084 1089 1094 1110 1110 1115 1121 1123 1154 1162 1170 1181 1186 1197 1212 1212 1225 1236 1238 1249 1251 1252 1268 1283 1299 1301 1312 1325 1325 1343 1353 1364 1380 1396 1396 1398 1399 1399 1412 1414 1430 1440 1440 1456 1527'''
    inlines=x.split("\n")
    M=int(inlines[0])
    N=int(inlines[1])
    Spectrum=inlines[2]
    #res=ConvolutionCyclopeptideSequencing(Spectrum,M,N)
    #print (res)

