using System;
using System.Collections.Generic;

namespace BA1I
{
    class Program
    {
        //A solution to a ROSALIND bioinformatics problem.
        //Problem Title: Find the Most Frequent Words with Mismatches in a String
        //Rosalind ID: BA1I
        //URL: http://rosalind.info/problems/ba1i
        static void Main(string[] args)
        {
            string kmer(string text, int i, int k)
            {
                //substring of text from i-th position for the next k letters
                return text.Substring(i, k);
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

            int ApproximatePatternCount(string text,string pattern,int d)
            {
                int count = 0;
                for (int i = 0; i < text.Length-pattern.Length+1; i++)
                {
                    string pattern2 = kmer(text, i, pattern.Length);
                    if (HammingDistance(pattern,pattern2)<=d)
                    {
                        count++;
                    }
                }
                return count;
            }
            string suffix(string pattern)
            {
                //substring of pattern without first letter
                return pattern.Substring(1, pattern.Length-1);
            }
            HashSet<string> Neighbours(string pattern,int d)
            {
                HashSet<string> nucleotides = new HashSet<string>();
                nucleotides.Add("A");
                nucleotides.Add("C");
                nucleotides.Add("G");
                nucleotides.Add("T");
                HashSet<string> neighborhood = new HashSet<string>();
                if (d==0)
                {
                    neighborhood.Add(pattern);
                    return neighborhood;
                }
                if (pattern.Length==1)
                {
                    return nucleotides;
                }
                HashSet<string> suffixNeighbors = Neighbours(suffix(pattern), d);
                foreach (string x in suffixNeighbors)
                {
                    if (HammingDistance(suffix(pattern),x)<d)
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

            Dictionary<string,int> kmerswithapproxcount(string text,int k,int d)
            {
                Dictionary<string, int> D = new Dictionary<string, int>();
                foreach (string window in Lwindows(text,k))
                {
                    foreach (string pattern in Neighbours(window,d))
                    {
                        D[pattern] = ApproximatePatternCount(text, pattern, d);
                    }
                }
                return D;

            }
            List<string> mostfrequentapproxkmers(string text, int k,int d)
            {
                Dictionary<string, int> D = kmerswithapproxcount(text, k,d);
                int maxcount = -1;
                foreach (string key in D.Keys)
                {
                    if (D[key] > maxcount)
                    {
                        maxcount = D[key];
                    }
                }
                List<string> keys = new List<string>();
                foreach (string key in D.Keys)
                {
                    if (D[key] == maxcount)
                    {
                        keys.Add(key);
                    }
                }
                return keys;
            }
            string x = "ACGTTGCATGTCGCATGATGCATGAGAGCT\n4 1";
            string[] inlines = x.Split();
            string text = inlines[0];
            int k = int.Parse(inlines[1]);
            int d = int.Parse(inlines[2]);
            List<string> res = mostfrequentapproxkmers(text, k, d);
            foreach (string s in res)
            {
                Console.WriteLine(s);
            }
       
        }
        }
}
