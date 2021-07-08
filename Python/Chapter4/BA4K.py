"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Compute the Score of a Linear Peptide
Rosalind ID: BA4K
URL: http://rosalind.info/problems/ba4k/
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

if __name__ == '__main__':
    x = '''NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484'''
    inlines = x.split("\n")
    res = LinearScore(inlines[0], inlines[1])
    print(res)
    print(res == 8)

    x = '''ICWTVCKDKSMGGNAGIWLRYYKQRKPYWTFSDKWFQR
0 57 57 57 71 87 97 99 99 101 103 103 113 113 113 113 114 114 115 128 128 128 128 128 128 128 137 147 147 156 156 156 156 163 163 163 170 171 185 186 186 186 186 194 198 199 212 216 218 224 225 227 228 241 242 243 243 248 250 251 256 260 269 275 281 284 284 284 285 287 289 291 298 299 299 299 299 311 312 314 314 319 326 333 338 340 346 349 351 355 356 356 356 365 365 380 381 384 388 388 402 411 412 412 412 412 413 419 429 431 432 434 437 439 442 446 450 451 452 454 455 461 461 466 468 469 469 482 484 487 493 493 494 497 501 508 509 510 526 532 537 540 544 547 550 555 565 567 568 574 575 576 579 580 582 589 594 595 597 597 598 600 600 608 610 617 618 625 625 636 637 637 652 654 655 663 666 672 675 679 679 679 692 693 694 696 700 703 704 711 712 713 723 728 730 731 736 738 738 745 749 750 753 753 768 780 780 781 788 791 793 797 799 800 800 806 807 807 807 815 822 825 826 831 841 848 849 851 852 858 860 864 866 867 890 894 894 905 906 909 912 912 916 920 924 925 927 935 936 939 943 947 951 954 955 959 962 963 963 963 966 977 978 981 986 992 1004 1007 1019 1022 1022 1030 1037 1040 1040 1042 1048 1049 1055 1068 1076 1079 1079 1081 1087 1087 1092 1105 1105 1106 1110 1113 1118 1118 1119 1126 1129 1133 1135 1144 1147 1149 1150 1155 1163 1168 1179 1190 1193 1193 1196 1204 1205 1205 1207 1207 1209 1211 1218 1226 1232 1234 1236 1241 1246 1250 1250 1276 1276 1281 1282 1291 1292 1293 1303 1304 1306 1307 1312 1317 1321 1321 1324 1324 1335 1337 1349 1354 1361 1363 1368 1373 1378 1395 1397 1397 1404 1404 1404 1406 1407 1413 1416 1418 1432 1432 1434 1435 1444 1449 1452 1452 1468 1489 1491 1491 1500 1501 1501 1503 1506 1510 1517 1520 1524 1531 1531 1535 1560 1560 1560 1563 1569 1572 1580 1581 1581 1588 1592 1595 1602 1602 1605 1615 1616 1619 1629 1638 1648 1657 1657 1659 1662 1663 1673 1682 1687 1694 1700 1705 1705 1715 1716 1716 1719 1723 1733 1743 1751 1758 1766 1767 1772 1778 1785 1785 1785 1787 1788 1790 1815 1818 1819 1829 1830 1836 1847 1856 1868 1871 1879 1880 1886 1886 1887 1891 1901 1906 1913 1913 1929 1932 1934 1935 1937 1941 1943 1943 1944 1981 1984 1993 1999 2004 2004 2014 2014 2015 2034 2038 2041 2047 2050 2057 2062 2065 2069 2071 2076 2081 2092 2098 2099 2107 2117 2118 2127 2128 2142 2160 2166 2168 2170 2175 2179 2185 2197 2197 2204 2220 2226 2227 2231 2233 2236 2239 2244 2248 2255 2273 2280 2288 2293 2298 2298 2313 2323 2324 2325 2331 2337 2346 2354 2360 2361 2361 2367 2383 2394 2395 2395 2403 2411 2416 2426 2427 2430 2436 2453 2474 2484 2486 2487 2508 2510 2511 2517 2523 2523 2523 2530 2531 2531 2531 2539 2541 2547 2558 2587 2599 2609 2614 2618 2636 2636 2638 2639 2644 2645 2659 2660 2673 2678 2679 2686 2694 2702 2717 2727 2735 2737 2742 2744 2759 2765 2773 2774 2781 2792 2795 2799 2807 2822 2830 2834 2845 2845 2855 2864 2868 2872 2887 2896 2898 2898 2921 2923 2935 2959 2973 2978 2983 2985 2992 2992 2992 2997 3011 3016 3020 3024 3024 3026 3073 3084 3086 3091 3095 3106 3111 3120 3120 3123 3139 3139 3148 3163 3183 3183 3185 3210 3210 3220 3223 3233 3234 3236 3267 3276 3284 3286 3291 3297 3332 3336 3338 3338 3348 3357 3369 3390 3399 3431 3435 3444 3447 3451 3453 3466 3470 3472 3485 3504 3524 3534 3550 3572 3573 3579 3585 3600 3617 3641 3649 3652 3671 3678 3686 3720 3720 3728 3728 3765 3777 3799 3799 3823 3833 3835 3864 3884 3912 3927 3936 3938 3955 3963 3963 4011 4040 4051 4066 4083 4110 4139 4149 4179 4196 4238 4252 4295 4296 4365 4394 4399 4424 4512 4527 4580 4640 4683 4796'''
    inlines = x.split("\n")
    res = LinearScore(inlines[0], inlines[1])
    print(res)
    print(res == 274)

    x = '''TINLNNFHITCTEDVNAACDKFCQYHNAYEAMNGINHENRSC
0 57 57 71 71 71 87 99 99 101 101 101 103 103 103 103 113 113 113 114 114 114 114 114 114 114 114 115 115 128 128 128 129 129 131 137 137 137 142 144 147 156 160 163 163 171 174 185 186 194 199 201 202 204 204 214 214 214 218 227 227 227 227 228 230 231 234 243 243 244 245 245 245 247 250 251 251 251 258 260 261 270 270 289 291 292 293 298 300 302 305 308 308 315 317 328 330 330 333 340 342 342 343 345 346 348 349 351 359 360 361 363 365 365 369 371 372 373 374 374 374 388 394 406 406 407 413 416 417 417 418 422 434 439 441 444 445 445 445 448 452 454 458 463 471 472 475 477 477 477 479 484 487 488 488 488 488 493 502 507 509 516 520 530 534 534 537 542 545 547 547 548 549 553 553 554 555 559 559 566 572 573 580 587 587 587 588 591 591 601 608 610 612 613 616 616 619 621 621 623 643 644 648 651 662 662 663 667 667 667 673 673 675 676 679 682 684 690 690 694 697 702 702 703 708 711 714 715 715 716 722 722 724 726 736 746 747 757 760 760 761 765 768 776 777 779 780 781 787 793 796 799 804 804 807 814 817 817 817 818 818 825 825 826 830 831 836 839 840 845 847 858 863 864 871 874 881 889 893 894 894 898 908 910 916 917 918 918 918 920 920 921 922 928 929 931 932 933 940 946 954 954 955 959 959 960 972 981 984 992 995 995 1005 1007 1021 1022 1025 1026 1027 1030 1030 1031 1032 1032 1034 1035 1036 1045 1047 1054 1057 1058 1060 1062 1068 1069 1071 1079 1085 1096 1096 1097 1098 1101 1107 1108 1108 1109 1119 1134 1136 1139 1144 1155 1156 1159 1160 1161 1161 1163 1165 1167 1167 1168 1168 1171 1176 1182 1185 1199 1199 1208 1209 1210 1210 1210 1211 1214 1216 1216 1242 1248 1249 1253 1262 1262 1264 1270 1270 1271 1279 1281 1281 1281 1281 1284 1289 1295 1296 1302 1305 1312 1312 1313 1315 1323 1324 1324 1328 1329 1330 1352 1363 1365 1367 1370 1373 1377 1379 1386 1390 1394 1395 1395 1398 1399 1401 1408 1409 1411 1413 1416 1427 1428 1438 1441 1443 1443 1444 1452 1466 1467 1468 1473 1476 1480 1482 1493 1493 1502 1507 1508 1509 1509 1513 1514 1514 1515 1515 1529 1539 1541 1542 1542 1542 1553 1556 1556 1571 1572 1573 1579 1579 1581 1585 1594 1596 1610 1613 1616 1621 1623 1627 1630 1638 1642 1643 1643 1644 1644 1653 1655 1656 1656 1657 1670 1670 1687 1688 1694 1695 1698 1700 1707 1709 1716 1724 1739 1741 1742 1744 1747 1752 1756 1756 1757 1758 1758 1758 1769 1772 1782 1783 1784 1801 1803 1812 1815 1818 1823 1823 1837 1839 1842 1844 1853 1854 1857 1858 1861 1861 1870 1871 1872 1872 1883 1884 1886 1889 1915 1916 1918 1924 1925 1931 1932 1942 1943 1945 1951 1952 1955 1956 1960 1975 1985 1986 1986 1986 1986 1989 2000 2002 2003 2007 2017 2026 2027 2028 2030 2030 2044 2055 2056 2057 2060 2066 2073 2074 2087 2088 2089 2100 2105 2114 2115 2116 2126 2128 2129 2130 2131 2133 2143 2143 2158 2163 2169 2170 2176 2188 2188 2190 2193 2197 2202 2203 2216 2229 2230 2231 2233 2233 2240 2241 2244 2246 2257 2261 2271 2275 2277 2287 2291 2306 2307 2311 2316 2317 2319 2325 2330 2332 2336 2345 2349 2360 2360 2370 2372 2374 2377 2378 2402 2403 2404 2420 2420 2424 2424 2431 2433 2435 2439 2448 2460 2461 2463 2463 2471 2473 2474 2488 2491 2518 2531 2533 2534 2534 2534 2537 2538 2539 2541 2562 2563 2564 2574 2575 2575 2576 2577 2601 2605 2610 2621 2632 2647 2648 2651 2653 2665 2668 2670 2675 2676 2678 2678 2678 2690 2692 2697 2702 2723 2724 2735 2749 2763 2764 2769 2778 2779 2781 2782 2784 2789 2790 2795 2804 2811 2820 2826 2836 2837 2837 2852 2865 2872 2883 2891 2892 2903 2904 2908 2915 2919 2923 2940 2940 2948 2949 2950 2951 2958 2973 2986 2990 3018 3020 3022 3029 3033 3047 3051 3051 3054 3064 3071 3071 3086 3086 3087 3087 3105 3123 3134 3135 3147 3150 3162 3165 3185 3185 3185 3200 3200 3201 3223 3224 3234 3236 3237 3242 3248 3265 3291 3298 3299 3314 3314 3332 3335 3337 3337 3338 3351 3356 3379 3392 3394 3399 3427 3428 3438 3445 3446 3451 3452 3474 3493 3493 3495 3495 3503 3528 3539 3541 3559 3559 3565 3588 3596 3598 3607 3616 3630 3640 3642 3652 3672 3673 3699 3702 3709 3730 3744 3744 3753 3754 3773 3786 3789 3812 3843 3846 3858 3858 3867 3867 3887 3891 3944 3945 3949 3972 3980 3981 4002 4004 4005 4059 4081 4094 4105 4116 4118 4118 4119 4195 4206 4219 4231 4232 4232 4263 4319 4332 4345 4346 4366 4376 4433 4446 4459 4479 4490 4546 4560 4593 4603 4647 4704 4706 4807'''
    inlines = x.split("\n")
    res = LinearScore(inlines[0], inlines[1])
    print(res)
