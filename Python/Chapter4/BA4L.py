"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Trim a Peptide Leaderboard
Rosalind ID: BA4L
URL: http://rosalind.info/problems/ba4l/
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

if __name__ == '__main__':
    x = '''LAST ALST TLLT TQAS
0 71 87 101 113 158 184 188 259 271 372
2'''
    inlines = x.split("\n")
    Leaderboard = inlines[0].split(" ")
    res = " ".join(Trim(Leaderboard, inlines[1], int(inlines[2])))
    print(res)
    print(res == '''LAST ALST''')

    x = '''GFAQHVMEGIGLDVKFTNIISCFFDHEWSTCHCKHHNSINHTMSMVF LIGDDDEADNCMMMVQSIKWKTLLRYGAFFTFPFYSYAILHVFYVLW KPMWWAFIFGFCDMKNCFDAPFWMHNSVQWEQHYRCNDVKMMSQLCW MAPRDIRMYFDKYHETAALDSQWIIQQIYHLMNVRKLNRTNRFTSVG FEKYHQQQILIDAQRVRLVHTVARAGPGWVQTGGWQQTCPRYKPYAW NVNPCERSSPPNFSWFMSFWADNSDYGDVIFCCPSVLRTMEMQSKKG WDTDTFFQKAMLKKDETADQIFNLRPYSLTCHNENILGNDNQEKQAG TLGSGENDKGHTVGAGHKGHPEREFEAPIERHEHPRVMMTKVGCYWI VCGHHHEQTVIMKAFDAWKVGFLGPIVAWVIFPAVYLWGKSLCPWTN YDSPTTYLSTHCHRLTNRMVHENPVICPPQDFAKYLIQSGWEFPLVA KDPINQTGDTNVRNFNVGCFCGCYFQWERHDGTPMHFWFSQKLSLTW HMKKLFWGIMKHHILFDFVNQPAFTNKAKGPTPHKAEELIRNLGQEK FNDRQRLVCHTNQCCAYKNKVVCSGGGSEISTNAHTYHFLALGHQVG MYYSAWTEPYYPPTLQIWWWYWKYGCTACQTGPHTMVFVQPTCKCVH YYGYRQCSWCQRWTVRRMLCWIDVLHKALHWHVCLLFHQALYGFSHE WASIGAIMRSAKDMYESLEFHKTHCTYFVYMVCKEARPGWTFFIEWV
0 71 87 97 97 99 101 101 101 101 101 103 103 113 113 113 113 113 113 113 113 114 114 115 115 128 128 129 129 129 129 129 129 131 131 131 137 137 147 147 156 156 156 163 163 163 186 186 198 200 200 202 202 204 214 214 216 216 216 226 228 230 234 242 242 242 242 242 242 244 245 253 257 257 257 259 260 266 266 268 269 271 276 276 276 276 278 283 284 285 287 293 294 299 301 303 313 317 317 317 327 329 331 343 343 347 354 355 355 356 359 363 363 370 370 371 371 372 379 382 384 388 389 397 397 400 405 407 408 408 413 413 415 415 416 418 418 420 422 428 430 430 432 434 439 444 455 456 458 459 473 476 484 484 485 485 487 499 500 501 506 507 510 510 511 513 515 518 522 526 527 528 529 529 531 533 533 537 540 541 544 544 545 547 558 559 562 568 569 571 572 574 585 586 588 597 598 607 610 612 616 619 620 624 624 625 626 631 636 641 644 646 650 657 657 660 662 663 669 669 670 671 672 674 675 678 681 684 685 689 691 692 696 698 699 700 700 701 711 733 733 735 738 738 739 741 753 771 772 772 773 775 775 775 778 779 782 783 783 786 788 789 794 794 797 798 798 800 801 802 804 805 806 808 810 813 815 828 837 840 846 854 862 864 864 866 869 882 884 885 886 888 889 899 901 902 902 903 904 907 908 911 911 914 914 924 925 926 928 935 935 937 937 941 941 945 952 955 961 961 975 975 977 984 987 988 992 995 999 1002 1013 1015 1016 1017 1017 1017 1022 1025 1032 1032 1038 1039 1039 1040 1044 1051 1055 1058 1058 1059 1062 1065 1066 1070 1070 1072 1074 1084 1088 1097 1099 1100 1101 1103 1104 1105 1106 1118 1118 1121 1130 1133 1135 1142 1150 1151 1153 1153 1154 1154 1156 1165 1171 1172 1186 1187 1194 1196 1198 1200 1201 1201 1202 1207 1212 1213 1214 1215 1216 1217 1217 1218 1218 1219 1231 1233 1234 1234 1236 1248 1255 1259 1264 1267 1272 1279 1281 1285 1298 1300 1301 1309 1311 1315 1315 1315 1316 1318 1319 1319 1321 1325 1330 1331 1334 1335 1338 1341 1343 1344 1346 1347 1348 1352 1363 1363 1372 1379 1395 1396 1398 1402 1410 1414 1414 1422 1422 1428 1429 1429 1430 1431 1432 1433 1434 1435 1435 1438 1447 1448 1450 1452 1460 1461 1471 1472 1472 1476 1476 1478 1481 1494 1499 1509 1515 1517 1521 1525 1532 1534 1535 1535 1535 1543 1546 1548 1551 1557 1557 1561 1561 1561 1562 1566 1566 1573 1577 1581 1585 1585 1589 1603 1605 1606 1608 1609 1609 1612 1618 1628 1634 1635 1636 1638 1647 1663 1664 1664 1664 1672 1672 1674 1674 1677 1680 1682 1686 1690 1694 1699 1702 1708 1713 1715 1716 1718 1718 1722 1723 1724 1740 1741 1743 1748 1749 1756 1763 1777 1777 1778 1781 1785 1792 1801 1803 1803 1805 1810 1811 1811 1815 1819 1819 1822 1823 1827 1830 1837 1837 1842 1844 1849 1850 1853 1869 1872 1876 1878 1878 1879 1887 1905 1906 1906 1912 1916 1916 1916 1924 1925 1929 1934 1936 1939 1940 1940 1940 1948 1948 1950 1965 1972 1979 1979 1991 1993 1996 2000 2000 2005 2007 2007 2009 2017 2019 2019 2026 2031 2034 2035 2039 2042 2053 2053 2058 2061 2064 2076 2079 2079 2087 2087 2094 2096 2097 2103 2113 2118 2120 2120 2123 2125 2132 2132 2135 2135 2136 2138 2140 2147 2150 2167 2171 2171 2192 2193 2200 2200 2200 2205 2209 2216 2216 2219 2224 2226 2226 2232 2233 2233 2233 2235 2237 2250 2252 2262 2266 2266 2268 2276 2284 2287 2296 2300 2303 2313 2318 2334 2334 2334 2336 2336 2337 2339 2347 2349 2355 2355 2356 2363 2363 2365 2366 2379 2380 2389 2397 2397 2413 2413 2416 2418 2434 2435 2437 2446 2447 2449 2449 2452 2466 2468 2468 2473 2476 2490 2492 2493 2494 2494 2494 2502 2510 2511 2519 2526 2533 2536 2542 2547 2549 2550 2553 2560 2578 2579 2579 2586 2597 2605 2605 2615 2620 2622 2623 2624 2624 2625 2627 2631 2632 2634 2648 2650 2650 2650 2651 2655 2689 2691 2706 2710 2711 2715 2733 2733 2733 2735 2738 2742 2742 2744 2747 2751 2753 2756 2761 2763 2768 2771 2779 2802 2807 2813 2820 2824 2825 2828 2836 2836 2836 2843 2846 2862 2862 2866 2871 2873 2876 2876 2881 2882 2900 2903 2907 2924 2933 2933 2937 2938 2944 2944 2949 2953 2957 2965 2972 2975 2975 2975 2987 2995 2999 3004 3018 3034 3034 3037 3037 3038 3039 3058 3062 3066 3066 3070 3073 3078 3078 3082 3088 3101 3104 3112 3119 3130 3135 3138 3149 3151 3152 3163 3163 3171 3172 3179 3190 3191 3193 3195 3217 3217 3220 3229 3238 3241 3241 3243 3244 3248 3250 3251 3276 3286 3291 3292 3300 3308 3318 3320 3321 3330 3335 3342 3351 3351 3354 3354 3357 3358 3358 3372 3387 3405 3407 3420 3422 3429 3431 3433 3433 3434 3439 3448 3455 3471 3483 3485 3486 3486 3488 3510 3514 3521 3533 3534 3534 3535 3546 3551 3552 3568 3585 3596 3599 3599 3600 3611 3611 3614 3615 3622 3634 3635 3647 3649 3664 3664 3681 3682 3696 3697 3708 3713 3727 3728 3728 3728 3735 3748 3750 3751 3771 3777 3797 3809 3812 3827 3828 3837 3841 3841 3842 3851 3857 3864 3864 3868 3868 3884 3898 3913 3940 3940 3942 3943 3955 3965 3969 3970 3970 3977 3981 4013 4014 4027 4027 4044 4053 4054 4056 4057 4083 4096 4098 4099 4110 4126 4140 4140 4140 4145 4155 4158 4167 4171 4184 4209 4211 4212 4223 4253 4255 4259 4268 4272 4284 4296 4296 4299 4303 4313 4352 4368 4373 4374 4397 4397 4397 4400 4409 4409 4416 4428 4465 4469 4487 4501 4510 4510 4526 4529 4538 4560 4566 4572 4584 4630 4639 4639 4639 4643 4651 4673 4673 4681 4685 4752 4752 4752 4768 4782 4786 4786 4802 4829 4853 4867 4881 4881 4883 4915 4915 4942 4968 4968 4982 4994 5028 5044 5069 5069 5071 5095 5097 5157 5157 5170 5184 5198 5210 5258 5270 5299 5311 5313 5371 5373 5412 5426 5474 5486 5527 5575 5587 5642 5688 5743 5844
5'''
    inlines = x.split("\n")
    Leaderboard = inlines[0].split(" ")
    res = " ".join(Trim(Leaderboard, inlines[1], int(inlines[2])))
    print(res)
    print(
        res == '''WASIGAIMRSAKDMYESLEFHKTHCTYFVYMVCKEARPGWTFFIEWV YYGYRQCSWCQRWTVRRMLCWIDVLHKALHWHVCLLFHQALYGFSHE WDTDTFFQKAMLKKDETADQIFNLRPYSLTCHNENILGNDNQEKQAG YDSPTTYLSTHCHRLTNRMVHENPVICPPQDFAKYLIQSGWEFPLVA MAPRDIRMYFDKYHETAALDSQWIIQQIYHLMNVRKLNRTNRFTSVG FEKYHQQQILIDAQRVRLVHTVARAGPGWVQTGGWQQTCPRYKPYAW''')

    x = '''RESDVFAADCVKKEWAIIASPEMRQELAHKLALNMKEQLAFQTYIKYAP NCSIMECDRQWESDTMTEWYGTFQFIIYTRPKEWKPTWTLRTPAQQSFD PTCKKYTTSQSNCYKIRYQWEARYHMIMLLDFQYKTIHNRYFWDLVLLW DIVHSKHDTKEFAKFGHANFGMKCAGTVNVNWIEWMWLEMFKTKLGATR TQQEMRDNNITPWIWHCEQAFEFAFFHCRLFGYLYIIEFVQSSCDPHEG NAWMGKWCNCLMNGKQSKIDCMYFRTYWYFARRYECFDEYCIAFDLQTD CYCMKEPSCPEFGWTHGVFATYSWDHEAESKGCCWDKVSYQFQNIYVTI ILNGHFMWAKALICYRYHNEQKGCGIRGKMIVFFCGQYHDKCQCTVFHH CNTDFEGWAQGAQPLGRTFTYSQMPFNCGMDHSPMWDKFLYLKLTSLVV SSKYSKQVKKAIAYQSCINGKLNNYGKWGDNLIRTFAREKETQCQNYAH FAWQHHTWQYWLHASYVQLWNSPFPKPHQCIDKVKCGCDSMQKRRAPVW FLHIYMVGVDNCPRGWTPCSHWYWWDKEPFCRMAFNSGEVDYSNHKMSF IAHQENSSDEGAKQLSRMPHHSQPEEAYYKHAGMRYRIFKADNNIQGTQ TLIMGEYDGDCRLLPVAIPIVASVWCKMRSMSIRFEGATYPTYGQQKLT AYYASRFDSRHPKRTIGKAFHTVMIQGNWKIQNSINEKSPMWLWEVQEM WFHCCFFWLHTTVRNNRKRAGYKGMNNNHIPKMTMQFWFTAKKFMVCHM
0 57 57 57 57 71 71 71 71 87 97 97 99 99 99 99 99 101 101 113 113 113 115 115 115 115 128 128 128 128 128 129 131 131 137 137 137 137 137 137 147 147 147 156 156 156 158 158 163 163 168 168 170 172 172 186 186 186 186 186 188 198 198 199 200 208 213 218 225 227 227 228 228 243 243 243 244 246 250 250 252 252 257 259 265 268 268 269 269 271 275 278 283 284 284 284 285 285 287 289 297 299 300 300 301 303 305 314 315 315 323 325 326 326 328 330 333 336 342 343 354 355 356 358 364 365 367 371 372 374 380 381 381 384 386 390 391 398 399 400 406 408 411 412 413 413 414 414 415 415 416 421 425 426 432 433 435 441 451 452 455 455 458 461 461 463 465 468 469 470 471 471 471 472 473 479 483 485 486 489 495 496 496 511 513 523 526 527 528 528 531 532 536 539 540 540 550 551 552 552 554 560 560 566 567 569 570 570 572 573 576 578 580 580 583 583 584 584 589 592 592 597 598 602 607 608 609 621 623 626 626 627 628 633 640 641 651 651 654 658 659 659 667 669 671 679 679 682 688 691 691 691 696 697 698 699 704 708 710 711 712 717 718 721 722 726 729 732 736 738 738 739 739 740 746 748 753 755 755 758 763 768 768 770 773 774 778 779 779 795 795 796 797 804 811 814 817 819 822 823 825 825 826 828 835 836 839 839 841 841 847 849 850 854 865 865 867 868 871 876 876 876 880 885 886 892 894 894 895 896 896 898 905 909 910 918 918 934 938 941 942 943 947 948 948 951 951 951 953 954 954 956 959 960 964 964 969 978 980 981 981 989 993 995 995 1002 1005 1007 1012 1013 1021 1022 1022 1023 1033 1038 1039 1042 1042 1046 1048 1052 1055 1062 1063 1063 1064 1066 1068 1069 1072 1073 1079 1080 1081 1091 1093 1096 1097 1106 1109 1111 1112 1117 1117 1119 1120 1123 1133 1134 1137 1139 1140 1144 1146 1150 1151 1152 1159 1167 1168 1169 1170 1176 1179 1189 1191 1201 1202 1205 1206 1206 1206 1207 1209 1210 1210 1218 1221 1228 1230 1232 1234 1239 1240 1248 1249 1249 1249 1250 1252 1262 1266 1266 1279 1280 1281 1283 1283 1286 1289 1296 1304 1305 1306 1306 1307 1315 1317 1319 1320 1321 1326 1331 1337 1338 1339 1347 1349 1357 1362 1363 1364 1365 1365 1365 1369 1377 1386 1387 1392 1394 1395 1396 1402 1403 1409 1414 1417 1419 1419 1420 1420 1420 1422 1423 1430 1434 1435 1437 1448 1454 1470 1474 1475 1477 1478 1484 1487 1490 1491 1492 1494 1494 1501 1502 1512 1518 1519 1521 1521 1521 1523 1524 1527 1530 1531 1532 1532 1534 1535 1547 1550 1551 1558 1567 1567 1572 1574 1578 1582 1585 1587 1592 1605 1609 1615 1618 1620 1622 1623 1631 1634 1638 1639 1640 1642 1645 1646 1646 1647 1652 1660 1665 1668 1669 1672 1673 1679 1680 1686 1691 1697 1698 1698 1702 1704 1709 1709 1710 1713 1717 1719 1721 1744 1755 1759 1760 1765 1767 1768 1770 1771 1773 1774 1778 1778 1781 1782 1784 1785 1789 1790 1801 1803 1810 1810 1817 1818 1828 1828 1835 1835 1835 1836 1845 1846 1856 1858 1860 1865 1872 1877 1878 1881 1888 1889 1892 1897 1898 1902 1907 1907 1909 1918 1922 1931 1934 1938 1940 1941 1941 1943 1945 1946 1947 1949 1957 1959 1966 1973 1976 1987 1993 1997 1998 2008 2009 2015 2017 2017 2023 2028 2028 2035 2044 2044 2046 2051 2053 2053 2053 2054 2056 2056 2060 2068 2074 2078 2081 2086 2086 2094 2097 2101 2104 2107 2110 2110 2113 2124 2124 2124 2145 2156 2159 2165 2165 2169 2175 2178 2180 2181 2181 2182 2191 2193 2200 2209 2209 2212 2214 2214 2223 2225 2226 2230 2235 2237 2239 2244 2244 2249 2258 2261 2266 2271 2274 2278 2282 2293 2296 2296 2306 2313 2319 2324 2325 2337 2338 2341 2343 2351 2351 2353 2357 2359 2363 2367 2372 2373 2376 2377 2386 2386 2395 2400 2408 2408 2411 2412 2424 2434 2437 2437 2450 2452 2456 2462 2464 2468 2472 2472 2480 2481 2482 2485 2494 2499 2501 2505 2514 2523 2523 2524 2527 2532 2533 2536 2537 2539 2539 2545 2549 2569 2581 2583 2589 2593 2593 2595 2596 2600 2600 2609 2613 2620 2620 2635 2636 2638 2640 2646 2650 2652 2654 2660 2660 2661 2664 2667 2676 2677 2679 2680 2696 2699 2706 2733 2736 2737 2740 2749 2751 2751 2753 2757 2763 2767 2774 2776 2777 2777 2782 2782 2783 2791 2792 2798 2799 2806 2806 2807 2816 2824 2827 2836 2837 2848 2850 2852 2873 2891 2895 2897 2898 2904 2905 2907 2908 2911 2914 2919 2923 2924 2926 2935 2935 2943 2944 2946 2947 2949 2952 2962 2992 2995 2995 2999 3004 3004 3004 3006 3010 3034 3034 3041 3042 3045 3048 3051 3061 3063 3066 3067 3070 3072 3074 3075 3077 3090 3093 3096 3105 3109 3129 3132 3132 3141 3147 3149 3166 3167 3167 3172 3173 3176 3190 3190 3192 3198 3203 3204 3204 3219 3224 3227 3229 3230 3237 3238 3247 3260 3262 3272 3276 3291 3295 3303 3304 3305 3313 3318 3319 3327 3329 3331 3332 3337 3352 3356 3358 3359 3362 3366 3375 3377 3390 3410 3413 3415 3415 3418 3418 3428 3430 3432 3433 3450 3458 3465 3474 3475 3475 3476 3481 3487 3503 3503 3514 3518 3527 3530 3531 3532 3544 3544 3545 3546 3547 3565 3574 3575 3601 3601 3602 3602 3603 3605 3613 3616 3618 3618 3631 3631 3643 3645 3655 3662 3674 3692 3700 3702 3702 3712 3716 3717 3721 3730 3730 3733 3733 3744 3746 3755 3763 3778 3787 3788 3799 3801 3802 3811 3818 3820 3829 3843 3845 3845 3849 3864 3870 3875 3883 3886 3888 3889 3891 3900 3902 3916 3935 3939 3942 3946 3946 3946 3958 3982 3985 3987 3992 3998 3999 4003 4015 4015 4017 4026 4031 4043 4063 4063 4070 4072 4083 4086 4097 4102 4114 4114 4116 4127 4132 4154 4154 4168 4171 4173 4178 4185 4191 4201 4211 4215 4229 4251 4253 4261 4272 4272 4282 4283 4300 4300 4306 4310 4313 4314 4315 4318 4358 4371 4371 4379 4381 4413 4415 4419 4428 4429 4430 4437 4439 4443 4470 4470 4478 4486 4496 4516 4518 4541 4558 4565 4566 4567 4569 4586 4587 4598 4615 4617 4623 4643 4664 4664 4686 4694 4697 4714 4714 4714 4716 4724 4751 4771 4785 4793 4811 4813 4823 4842 4844 4850 4850 4852 4884 4922 4939 4941 4951 4951 4979 4997 5012 5021 5036 5050 5050 5125 5126 5137 5149 5149 5149 5183 5236 5248 5254 5277 5284 5311 5335 5376 5383 5412 5434 5482 5511 5562 5581 5610 5709 5709 5837
5'''
    inlines = x.split("\n")
    Leaderboard = inlines[0].split(" ")
    res = " ".join(Trim(Leaderboard, inlines[1], int(inlines[2])))
    print(res)