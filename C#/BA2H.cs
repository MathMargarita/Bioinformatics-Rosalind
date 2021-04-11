using System;
using System.Collections.Generic;

namespace BA2H
{
    class BA2H
    {
        //A solution to a ROSALIND bioinformatics problem.
        //Problem Title: Implement DistanceBetweenPatternAndStrings
        //Rosalind ID: BA2H
        //URL: http://rosalind.info/problems/ba2h/
        static void Main(string[] args)
        {
            string kmer(string text, int i, int k)
            {
                //substring of text from i-th position for the next k letters
                return text.Substring(i, k);
            }
            List<string> Lwindows(string text, int L)
            {
                //list of all L-windows in text
                List<string> windows = new List<string>();
                for (int i = 0; i < text.Length - L + 1; i++)
                {
                    windows.Add(kmer(text, i, L));
                }
                return windows;

            }
            int HammingDistance(string p, string q)
            {
                //Computes the hamming distance between strings p and q
                if (p.Length != q.Length)
                {
                    return -1;
                }
                int dist = 0;
                (char first, char second)[] zippq = new (char first, char second)[p.Length];
                for (int i = 0; i < p.Length; i++)
                {
                    zippq[i] = (p[i], q[i]);
                }
                foreach ((char first, char second) x in zippq)
                {
                    if (x.first != x.second)
                    {
                        dist = dist + 1;
                    }
                }
                return dist;

            }
            int distanceBetweenPatternAndStrings(string Pattern, string []Dna)
            {
                int k = Pattern.Length;
                int distance = 0;
                foreach (string Text in Dna)
                {
                    int hammingDistance = Pattern.Length;
                    foreach(string Pattern1 in Lwindows(Text, k))
                    {
                        if (hammingDistance > HammingDistance(Pattern, Pattern1))
                            hammingDistance = HammingDistance(Pattern, Pattern1);
                    }
                    distance = distance + hammingDistance;
                }

                return distance;
            }

            string x = "AAA\nTTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT";
            string[] inlines = x.Split();
            string pattern=inlines[0];
            string[] dna = new string[inlines.Length - 1];
            for (int i = 1; i < inlines.Length; i++)
            {
                dna[i-1] = inlines[i];
            }
            int res = distanceBetweenPatternAndStrings(pattern, dna); 
            Console.WriteLine(res);

        }
    }
}
