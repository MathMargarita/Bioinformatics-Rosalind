using System;
using System.Collections.Generic;

namespace BA1F
{
    class Program
    {
    //A solution to a ROSALIND bioinformatics problem.
    //Problem Title: Find a Position in a Genome Minimizing the Skew
    //Rosalind ID: BA1F
    //URL: http://rosalind.info/problems/ba1e/


        static void Main(string[] args)
        {
            string kmer(string text, int i, int k)
            {
                //substring of text from i-th position for the next k letters
                return text.Substring(i, k);
            }
            int[] skew(string text)
            {
                int[] sk = new int[text.Length + 1];
                for (int  k= 1; k < text.Length+1; k++)
                {
                    if (kmer(text,0,k)[kmer(text,0,k).Length-1]=='C')
                    {
                        sk[k] = sk[k - 1] - 1;
                    }
                    else if(kmer(text, 0, k)[kmer(text, 0, k).Length - 1] == 'G')
                    {
                        sk[k] = sk[k - 1] + 1;
                    }
                    else
                    {
                        sk[k] = sk[k - 1];
                    }
                }
                return sk;
            }
           
            List<int> indexofminskew(int[]skew)
            {
                List<int> ind = new List<int>();
                int minval = skew.Length;
                foreach (int num in skew)
                {
                    if (num<minval)
                    {
                        minval = num;
                    }
                }
                for (int i = 0; i < skew.Length; i++)
                {
                    if (skew[i]==minval)
                    {
                        ind.Add(i);
                    }
                }
                return ind;
            }



            string x = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG";
            List<int> res = indexofminskew(skew(x));
            foreach (int i in res)
            {
                Console.WriteLine(i);
            }
        }
    }
}
