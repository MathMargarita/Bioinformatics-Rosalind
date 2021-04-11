using System;
using System.Collections.Generic;

namespace BA2B
{
    class Program
    {
        //A solution to a ROSALIND bioinformatics problem.
        //Problem Title: Find a Median String
        //Rosalind ID: BA2B
        //URL: http://rosalind.info/problems/ba2b/
        static void Main(string[] args)
        {
            string kmer(string text, int i, int k)
            {
                //substring of text from i-th position for the next k letters
                return text.Substring(i, k);
            }
            Dictionary<string, int> kmersfrequency(string text, int k)
            {
                Dictionary<string, int> D = new Dictionary<string, int>();
                for (int i = 0; i < text.Length - k + 1; i++)
                {
                    string tmp = kmer(text, i, k);
                    try
                    {
                        D[tmp] = D[tmp] + 1;
                    }
                    catch (KeyNotFoundException) //ne postoji taj kljuc, tj. prvi put se pojavljuje ta rijec u tekstu
                    {

                        D[tmp] = 1;
                    }
                }
                return D;
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

            string suffix(string pattern)
            {
                //substring of pattern without first letter
                return pattern.Substring(1, pattern.Length - 1);
            }
            HashSet<string> Neighbours(string pattern, int d)
            {
                HashSet<string> nucleotides = new HashSet<string>();
                nucleotides.Add("A");
                nucleotides.Add("C");
                nucleotides.Add("G");
                nucleotides.Add("T");
                HashSet<string> neighborhood = new HashSet<string>();
                if (d == 0)
                {
                    neighborhood.Add(pattern);
                    return neighborhood;
                }
                if (pattern.Length == 1)
                {
                    return nucleotides;
                }
                HashSet<string> suffixNeighbors = Neighbours(suffix(pattern), d);
                foreach (string x in suffixNeighbors)
                {
                    if (HammingDistance(suffix(pattern), x) < d)
                    {
                        foreach (string n in nucleotides)
                        {
                            neighborhood.Add(n + x);
                        }
                    }
                    else
                    {
                        neighborhood.Add(pattern[0] + x);
                    }
                }
                return neighborhood;
            }
            int minHamm(string text, string pattern)
            {
                //Find the minimum Hamming distance bethween Pattern and any k-mer in text
                Dictionary<string, int> D = kmersfrequency(text, pattern.Length);
                int min = pattern.Length;
                foreach (string x in D.Keys)
                {
                    if (HammingDistance(pattern,x)<min)
                    {
                        min = HammingDistance(pattern, x);
                    }
                }
                return min;

            }
            Dictionary<string,int> kmerNeighbours(string text,int k)
            {
                //Find all k-mers (words) and their Neighbours in a string text together with a minimal hamming distance between neighbours and the set of original k-mers
                HashSet<string> L = new HashSet<string>();
                for (int i = 0; i < text.Length-k+1; i++)
                {
                    for (int d = 0; d < k+1; d++)
                    {
                        L.UnionWith(Neighbours(kmer(text, i, k), d));
                    }
                }
                Dictionary<string, int> D = new Dictionary<string, int>();
                foreach (string l in L)
                {
                    D[l] = minHamm(text, l);
                }
                return D;
            }

            string MedianString(List<string>dnalist, int k)
            {
                //Find the k-mer Pattern that minimizes d(Pattern,Dnalist)=sum(d(Pattern,Dna)) over all k-mers Pattern and Dnalist where d=minhamm
                List<Dictionary<string, int>> L = new List<Dictionary<string, int>>();
                foreach (string dna in dnalist)
                {
                    L.Add(kmerNeighbours(dna, k));
                }
                HashSet<string> s = new HashSet<string>();
                foreach (Dictionary<string,int> x in L)
                {
                    s.UnionWith(x.Keys);
                }
                Dictionary<string, int> RES = new Dictionary<string, int>();
                foreach (string key in s)
                {
                    RES[key] = 0;
                }
                foreach (Dictionary<string,int> D in L)
                {
                    foreach (string key in D.Keys)
                    {
                        RES[key] = RES[key] + D[key];
                    }
                }
                int mincount = 1000;
                foreach (int value in RES.Values)
                {
                    mincount = value;
                    break;
                }
                foreach (int value in RES.Values)
                {
                    if (value<mincount)
                    {
                        mincount = value;
                    }
                }
                List<string> tmp = new List<string>();
                foreach (string key in RES.Keys)
                {
                    if (mincount==RES[key])
                    {
                        tmp.Add(key);
                    }
                }
                return tmp[0];
            }

            string x = "3\nAAATTGACGCAT\nGACGACCACGTT\nCGTCAGCGCCTG\nGCTGAGCACCGG\nAGTACGGGACAG";
            string[] inlines = x.Split();
            int k = int.Parse(inlines[0]);

            List<string> L = new List<string>();
            for (int i = 2; i < inlines.Length; i++)
            {
                L.Add(inlines[i]);
            }
            string res = MedianString(L, k);
            Console.WriteLine(res);

        }
    }
}
