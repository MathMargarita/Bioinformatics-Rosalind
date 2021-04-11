using System;
using System.Collections.Generic;

namespace BA2F
{
    class BA2F
    {
        //A solution to a ROSALIND bioinformatics problem.
        //Problem Title: Implement RandomizedMotifSearch
        //Rosalind ID: BA2F
        //URL: http://rosalind.info/problems/ba2f/
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

            string mostProbkmerinText(string text, int k, double[][] profile)
            {
                Dictionary<string, double> d = new Dictionary<string, double>();
                foreach (string window in Lwindows(text, k))
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

            int count(List<string> motifs, int nucl, int i)
            {
                //compute count for each nucleotide of i-th column
                char[] col = new char[motifs.Count];
                for (int j = 0; j < motifs.Count; j++)
                {
                    col[j] = motifs[j][i];
                }
                int num = 0;
                if (nucl == 0)
                {
                    foreach (char n in col)
                    {
                        if (n == 'A')
                            num = num + 1;
                    }
                }
                if (nucl == 1)
                {
                    foreach (char n in col)
                    {
                        if (n == 'C')
                            num = num + 1;
                    }
                }
                if (nucl == 2)
                {
                    foreach (char n in col)
                    {
                        if (n == 'G')
                            num = num + 1;
                    }
                }
                if (nucl == 3)
                {
                    foreach (char n in col)
                    {
                        if (n == 'T')
                            num = num + 1;
                    }
                }
                return num;


            }

            int capitalLetter(List<string> motifs, int i)
            {
                //find a capital letter of i-th column
                int[] counts = new int[4];
                for (int nucl = 0; nucl < 4; nucl++)
                {
                    counts[nucl] = count(motifs, nucl, i);
                }
                int max = 0;
                for (int nucl = 0; nucl < 4; nucl++)
                {
                    if (counts[nucl] > max)
                        max = counts[nucl];
                }
                return Array.IndexOf(counts, max);
            }

            int score(List<string> motifs)
            {
                int sc = 0;
                for (int i = 0; i < motifs[0].Length; i++)
                {
                    sc = sc + (motifs.Count - count(motifs, capitalLetter(motifs, i), i));
                }
                return sc;
            }

            double[][] profileMatrixWithPseudocounts(List<string> motifs, int k)
            {
                double[][] matrix = new double[4][];
                for (int nucl = 0; nucl < 4; nucl++)
                {
                    matrix[nucl] = new double[k];
                }
                for (int i = 0; i < k; i++)
                {
                    for (int nucl = 0; nucl < 4; nucl++)
                    {
                        matrix[nucl][i] = (double)(count(motifs, nucl, i) + 1) / (double)(motifs.Count + 4);
                    }
                }
                return matrix;
            }

            List<string> Motifs(string[] dna, double[][] profile)
            {
                int t = dna.Length;
                int k = profile[0].Length;
                List<string> motifs = new List<string>();
                for (int i = 0; i < t; i++)
                {
                    motifs.Add(mostProbkmerinText(dna[i], k, profile));
                }
                return motifs;
            }

            List<string> RandomizedMotifSearchAtom(string[] dna, int k)
            {
                int n = dna[0].Length;
                System.Random random = new System.Random();
                int[] randpos = new int[dna.Length];
                for (int i = 0; i < dna.Length; i++)
                {
                    randpos[i] = random.Next(0, n - k+1);
                }
                List<string> BestMotifs = new List<string>();
                for (int i = 0; i < dna.Length; i++)
                {
                    BestMotifs.Add(kmer(dna[i], randpos[i], k));
                }
                List<string> motifs = BestMotifs;
                while (true)
                {
                    double[][] profile = profileMatrixWithPseudocounts(motifs, k);
                    motifs = Motifs(dna, profile);
                    if (score(motifs) < score(BestMotifs))
                    {
                        BestMotifs = motifs;
                    }
                    else
                    {
                        return BestMotifs;
                    }
                }

            }

            List<string> RandomizedMotifSearch(string[] dna, int k, int N)
            {
                List<string> BestMotifs = RandomizedMotifSearchAtom(dna,k);
                for (int i=0; i<N; i++)
                {
                    List<string> motifs = RandomizedMotifSearchAtom(dna, k);
                    if (score(motifs) < score(BestMotifs))
                    {
                        BestMotifs = motifs;
                    }
                }
                return BestMotifs;
            }

            string x = "8 5\nCGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA\nGGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG\nTAGTACCGAGACCGAAAGAAGTATACAGGCGT\nTAGATCAAGTTTCAGGTGCACGTCGGTGAACC\nAATCCACCAGCTCCACGTGCAATGTTGGCCTA";
            string[] inlines = x.Split();
            int k = int.Parse(inlines[0]);
            //int t = int.Parse(inlines[1]);
            string[] dna = new string[inlines.Length - 2];
            for (int i = 2; i < inlines.Length; i++)
            {
                dna[i - 2] = inlines[i];
            }
            List<string> res = RandomizedMotifSearch(dna, k, 1000);
            foreach (string s in res)
            {
                Console.WriteLine(s + " ");
            }
        }
    }
}
