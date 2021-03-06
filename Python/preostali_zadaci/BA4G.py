"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement LeaderboardCyclopeptideSequencing
Rosalind ID: BA4G
URL: http://rosalind.info/problems/ba4g/
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

    x = '''325
0 71 71 71 87 97 97 99 101 103 113 113 114 115 128 128 129 137 147 163 163 170 184 184 186 186 190 211 215 226 226 229 231 238 241 244 246 257 257 276 277 278 299 300 312 316 317 318 318 323 328 340 343 344 347 349 356 366 370 373 374 391 401 414 414 415 419 427 427 431 437 441 446 453 462 462 462 470 472 502 503 503 511 515 529 530 533 533 540 543 547 556 559 569 574 575 584 590 600 600 604 612 616 617 630 640 640 643 646 648 660 671 683 684 687 693 703 703 719 719 719 729 730 731 737 740 741 745 747 754 774 780 784 790 797 800 806 818 826 827 832 833 838 846 846 847 850 868 869 877 884 889 893 897 903 908 913 917 930 940 947 956 960 960 961 964 965 966 983 983 985 1002 1009 1010 1011 1021 1031 1031 1036 1053 1054 1058 1059 1062 1063 1074 1076 1084 1092 1103 1113 1122 1124 1130 1133 1134 1145 1146 1146 1149 1150 1155 1156 1171 1173 1174 1187 1191 1193 1200 1212 1221 1233 1240 1242 1246 1259 1260 1262 1277 1278 1283 1284 1287 1287 1288 1299 1300 1303 1309 1311 1320 1330 1341 1349 1357 1359 1370 1371 1374 1375 1379 1380 1397 1402 1402 1412 1422 1423 1424 1431 1448 1450 1450 1467 1468 1469 1472 1473 1473 1477 1486 1493 1503 1516 1520 1525 1530 1536 1540 1544 1549 1556 1564 1565 1583 1586 1587 1587 1595 1600 1601 1606 1607 1615 1627 1633 1636 1643 1649 1653 1659 1679 1686 1688 1692 1693 1696 1702 1703 1704 1714 1714 1714 1730 1730 1740 1746 1749 1750 1762 1773 1785 1787 1790 1793 1793 1803 1816 1817 1821 1829 1833 1833 1843 1849 1858 1859 1864 1877 1886 1890 1893 1900 1900 1903 1904 1918 1922 1930 1930 1931 1961 1963 1971 1971 1971 1980 1987 1992 1996 2002 2006 2006 2014 2018 2019 2019 2032 2042 2059 2060 2063 2067 2077 2084 2086 2089 2090 2093 2105 2110 2115 2115 2116 2117 2121 2133 2134 2155 2156 2157 2176 2176 2187 2189 2192 2195 2202 2204 2207 2207 2218 2222 2243 2247 2247 2249 2249 2263 2270 2270 2286 2296 2304 2305 2305 2318 2319 2320 2320 2330 2332 2334 2336 2336 2346 2362 2362 2362 2433'''
    inlines = x.split("\n")
    N = int(inlines[0])
    Spectrum = inlines[1]
    res = LeaderboardCyclopeptideSequencing(Spectrum, N)
    print(res)

    x='''393
0 71 99 103 103 113 129 129 131 131 137 147 156 156 200 200 230 234 234 240 240 244 246 269 285 285 303 329 333 343 347 356 356 371 371 377 398 400 402 432 469 470 474 480 484 485 485 503 503 529 531 533 573 587 598 600 602 605 617 632 632 636 640 641 662 703 704 718 720 729 731 733 743 754 765 769 773 788 817 832 836 840 851 862 872 874 876 885 887 901 902 943 964 965 969 973 973 988 1000 1003 1005 1007 1018 1032 1072 1074 1076 1102 1102 1120 1120 1121 1125 1131 1131 1135 1136 1173 1203 1205 1207 1228 1234 1234 1249 1249 1258 1262 1272 1276 1302 1320 1320 1336 1359 1361 1365 1365 1371 1371 1375 1405 1405 1449 1449 1458 1468 1474 1474 1476 1476 1492 1502 1502 1506 1534 1605'''
    inlines=x.split("\n")
    N=int(inlines[0])
    Spectrum=inlines[1]
    res=LeaderboardCyclopeptideSequencing(Spectrum,N)
    print (res)
