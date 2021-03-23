using System;
using System.Collections.Generic;

namespace BA1N
{
    class Program
    {
    //A solution to a Rosalind bioinformatics problem
    //Problem Title: Generate the d-Neighborhood of a String
    //URL: http://rosalind.info/problems/ba1n/
        static void Main(string[] args)
        {
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

            string x = "ACG\n1";
            string[] inlines = x.Split();
            string pattern = inlines[0];
            int d = int.Parse(inlines[1]);
            HashSet<string> res = Neighbours(pattern, d);
            foreach (string s in res)
            {
                Console.WriteLine(s);
            }


        }
    }
}
