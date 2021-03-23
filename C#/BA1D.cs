using System;
using System.Collections.Generic;

namespace BA1D
{
    class Program
    {
    //A solution to a ROSALIND bioinformatics problem.
    //Problem Title: Find All Occurrences of a Pattern in a String
    //Rosalind ID: BA1D
    //URL: http://rosalind.info/problems/ba1d/
        static void Main(string[] args)
        {
            string kmer(string text, int i, int k)
            {
                //substring of text from i-th position for the next k letters
                return text.Substring(i, k);
            }
            List<int> patternposition(string text, string pattern)
            {
                //Find a starting position of pattern is within a text
                List<int> p = new List<int>();
                int np = pattern.Length;
                for (int i = 0; i < text.Length - np + 1; i++)
                {
                    if (kmer(text, i, np) == pattern)
                    {
                        p.Add(i);
                    }
                }
                return p;
            }

            string x = "ATAT\nGATATATGCATATACTT";
            string[] inlines = x.Split("\n");
            string text = inlines[1];
            string pattern = inlines[0];

            List<int> res = patternposition(text, pattern);
            foreach (int i in res)
            {
                Console.Write(i+" ");
            }
        }
    }
}
