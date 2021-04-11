using System;
using System.Collections.Generic;

namespace BA2C
{
    class BA2C
    {
        //A solution to a ROSALIND bioinformatics problem.
        //Problem Title: Find a Profile - most Probable k-mer in a String
        //Rosalind ID: BA2C
        //URL: http://rosalind.info/problems/ba2c/
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

            double probability(string window, double[][] profile)
            {
                //probability of kmer in string according to profile matrix
                double prob = 1;
                for (int i = 0; i < window.Length; i++)
                {
                    if (window[i] == 'A')
                        prob = prob * profile[0][i];
                    else
                    {
                        if (window[i] == 'C')
                            prob = prob * profile[1][i];
                        else
                        {
                            if (window[i] == 'G')
                                prob = prob * profile[2][i];
                            else if (window[i] == 'T')
                                prob = prob * profile[3][i];
                        }
                    }
                }
                return prob;
            }

            string mostProbkmerinText(string text, int k,double[][]profile)
            {
                Dictionary<string, double> d = new Dictionary<string, double>();
                foreach (string window in Lwindows(text,k))
                {
                    d[window] = probability(window, profile);
                }
                double maxcount = 0;
                foreach (string key in d.Keys)
                {
                    if (d[key] > maxcount)
                    {
                        maxcount = d[key];
                    }
                }
                List<string> keys = new List<string>();
                foreach (string key in d.Keys)
                {
                    if (d[key] == maxcount)
                    {
                        keys.Add(key);
                    }
                }
                return keys[0];
            }

            string x = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT\n5\n0.2 0.2 0.3 0.2 0.3\n0.4 0.3 0.1 0.5 0.1\n0.3 0.3 0.5 0.2 0.4\n0.1 0.2 0.1 0.1 0.2";
            //string x = "TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCCTGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGCGCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCACCCCTA\n6\n0.364 0.333 0.303 0.212 0.121 0.242\n0.182 0.182 0.212 0.303 0.182 0.303\n0.121 0.303 0.182 0.273 0.333 0.303\n0.333 0.182 0.303 0.212 0.364 0.152";
            string[] inlines = x.Split('\n');
            string text = inlines[0];
            int k = int.Parse(inlines[1]);
            string[][] prof = new string[4][];
            for (int i=2; i<6; i++)
            {
                prof[i-2]=inlines[i].Split();
            }
            double[][] profile = new double[4][];
            for (int i = 0; i < 4; i++)
            {
                profile[i] = new double[k];
                for (int j = 0; j < k; j++)
                {
                    profile[i][j] = double.Parse(prof[i][j], System.Globalization.CultureInfo.InvariantCulture);
                }
            }
            string res = mostProbkmerinText(text, k, profile);
            Console.WriteLine(res);
        }
    }
}
