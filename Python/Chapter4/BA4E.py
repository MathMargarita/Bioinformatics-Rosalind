"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Compute the Number of Peptides of Given Total Mass
Rosalind ID: BA4E
URL: http://rosalind.info/problems/ba4e/
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

def CyclospectrumList(peptide):
    subPeptides=['',peptide]
    peptide1=peptide+peptide
    for i in range (1,len(peptide)):
        for j in range(0,len(peptide)):
            subPeptides.append(peptide1[j:j+i])
    spectrum=[]
    for pep in subPeptides:
        spectrum.append(Mass(pep))
    spectrum.sort()
    return spectrum

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

def Expand(peptides):
    newPeptides=[]
    for peptide in peptides:
        for a in get_amino_acid_mass().keys():
            newPeptides.append(peptide+a)
    return newPeptides

def CyclopeptideSequencing(Spectrum):
    spectrum=Spectrum.split()
    for i in range (len(spectrum)):
        spectrum[i]=int(spectrum[i])
    peptides=['']
    output=[]
    while len(peptides)>0:
        removeList=[]
        peptides=Expand(peptides)
        for peptide in peptides:
            if Mass(peptide)==spectrum[-1]:
                if CyclospectrumList(peptide)==spectrum:
                    output.append([str(get_amino_acid_mass()[a]) for a in peptide])
                removeList.append(peptide)
            else:
                spec=spectrum.copy()
                for s in LinearspectrumList(peptide):
                    if s not in spec:
                        removeList.append(peptide)
                        break
                    else:
                        spec.remove(s)
        for x in removeList:
            peptides.remove(x)
    outputList=['-'.join(output[i]) for i in range (len(output))]
    return ' '.join(list(set(outputList)))

if __name__ == '__main__':
    x='''0 113 128 186 241 299 314 427'''
    res=CyclopeptideSequencing(x)
    print (res)
    print(set(res.split()) == set('''186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186'''.split()))

    x = '''0 71 97 99 103 113 113 114 115 131 137 196 200 202 208 214 226 227 228 240 245 299 311 311 316 327 337 339 340 341 358 408 414 424 429 436 440 442 453 455 471 507 527 537 539 542 551 554 556 566 586 622 638 640 651 653 657 664 669 679 685 735 752 753 754 756 766 777 782 782 794 848 853 865 866 867 879 885 891 893 897 956 962 978 979 980 980 990 994 996 1022 1093'''
    res = CyclopeptideSequencing(x)
    print(res)
    print(set(res.split()) == set(
        '''103-137-71-131-114-113-113-115-99-97 103-97-99-115-113-113-114-131-71-137 113-113-114-131-71-137-103-97-99-115 113-113-115-99-97-103-137-71-131-114 113-114-131-71-137-103-97-99-115-113 113-115-99-97-103-137-71-131-114-113 114-113-113-115-99-97-103-137-71-131 114-131-71-137-103-97-99-115-113-113 115-113-113-114-131-71-137-103-97-99 115-99-97-103-137-71-131-114-113-113 131-114-113-113-115-99-97-103-137-71 131-71-137-103-97-99-115-113-113-114 137-103-97-99-115-113-113-114-131-71 137-71-131-114-113-113-115-99-97-103 71-131-114-113-113-115-99-97-103-137 71-137-103-97-99-115-113-113-114-131 97-103-137-71-131-114-113-113-115-99 97-99-115-113-113-114-131-71-137-103 99-115-113-113-114-131-71-137-103-97 99-97-103-137-71-131-114-113-113-115'''.split()))

