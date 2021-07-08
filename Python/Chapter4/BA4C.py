"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Generating Theoretical Spectrum Problem:
Rosalind ID: BA4C
URL: http://rosalind.info/problems/ba4c/
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
        "W": 186
    }

    return mass

def Cyclospectrum(peptide):
    subPeptides=['',peptide]
    peptide1=peptide+peptide
    for i in range (1,len(peptide)):
        for j in range(0,len(peptide)):
            subPeptides.append(peptide1[j:j+i])
    spectrum=[]
    for pep in subPeptides:
        mass=0
        for a in pep:
            mass=mass+get_amino_acid_mass()[a]
        spectrum.append(mass)
    spectrum.sort()
    for i in range (0,len(spectrum)):
        spectrum[i]=str(spectrum[i])
    return ' '.join(spectrum)

if __name__ == '__main__':
    x='''LEQN'''
    res=Cyclospectrum(x)
    print (res)
    print(res=='0 113 114 128 129 227 242 242 257 355 356 370 371 484')

    x = '''IAQMLFYCKVATN'''
    res = Cyclospectrum(x)
    print(res)
    print(res=='0 71 71 99 101 103 113 113 114 128 128 131 147 163 170 172 184 199 215 227 227 231 244 259 260 266 271 286 298 298 310 312 328 330 330 372 385 391 394 399 399 399 401 413 423 426 443 443 470 493 498 502 513 519 526 527 541 554 556 557 564 569 590 598 616 626 640 654 657 658 665 670 682 697 697 703 711 729 729 753 753 771 779 785 785 800 812 817 824 825 828 842 856 866 884 892 913 918 925 926 928 941 955 956 963 969 980 984 989 1012 1039 1039 1056 1059 1069 1081 1083 1083 1083 1088 1091 1097 1110 1152 1152 1154 1170 1172 1184 1184 1196 1211 1216 1222 1223 1238 1251 1255 1255 1267 1283 1298 1310 1312 1319 1335 1351 1354 1354 1368 1369 1369 1379 1381 1383 1411 1411 1482')



