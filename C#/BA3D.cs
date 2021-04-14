using System;
using System.Collections.Generic;

namespace BA3D
{
    class BA3D
    {
        //A solution to a ROSALIND bioinformatics problem.
        //Problem Title: Construct the De Bruijn Graph of a String
        //Rosalind ID: BA3D
        //URL: http://rosalind.info/problems/ba3d/
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
            string prefix(string pattern)
            {
                //substring of pattern without  the last letter
                return pattern.Substring(0, pattern.Length - 1);
            }
            string suffix(string pattern)
            {
                //substring of pattern without first letter
                return pattern.Substring(1, pattern.Length - 1);
            }

            Dictionary<string, List<string>> DeBruijn(int k, string text)
            {
                Dictionary<string, List<string>> adjacency = new Dictionary<string, List<string>>();
                List<string> sortedWindows= Lwindows(text,k);
                sortedWindows.Sort();
                foreach (string window in sortedWindows)
                {
                    adjacency[prefix(window)] = new List<string>();                  
                }
                foreach (string window in sortedWindows)
                {
                    adjacency[prefix(window)].Add(suffix(window));
                }
                return adjacency;
            }
            void multipleGraphPrint(Dictionary<string, List<string>> adj)
            {
                foreach (string key in adj.Keys)
                {
                    Console.Write(key + " -> ");
                    foreach (string s in adj[key])
                    {
                        Console.Write(s + " ");
                    }
                    Console.WriteLine();
                }
            }


            string x = "4\nAAGATTCTCTAC";
            //string x='12\nCTGAAGACCTCTCCACATTACTACGATATAAATCATTTCAGCCTCTAGATACGCCTTGGTGGGTGGGGTTGGCAATTTACGATATGTCCGAATGATTTGACACCAAATACCTTAGCTAGCCCCAAGGAAAATTCTGGGCTTTACGTTGGCCGAGCCACATTACTACAGTAAGGTTAAGCAACCAGCCAGTCGCTCATAAGGACTCCACGCCTCCCGTTACTGACTTCCAACAACAATGTGACAGTAGACTGGAACCTGGGAGGACATTATTGATTCGCCGCGAATCTTCTAAGGTATTTTACCCCCACTGGTCACCTTAACCATTAAGACCTCGAAGTGACACCTAGCCTCTTAACACCCAACTCCACCGACAATACCTATTCGCTGACAAGCGGGACATCCGATCGCCCCTGACTCGAGGTGTCTACCGTCCATCGATTGCTAAACTTTGTTAGGAGTCTAAGCGAACCATGGGAAGGGGGCGGCAGTCAACGTGCTCCTTTAGTGAGGTACCATATTCTTACAGCATGTGGAGCGCAGCAAACTAGCGACCGGGAGTACTCCCACAACCCTGGGTACGTACTGCACTTTTTTCAAGAGCCAGGGTCATTTAAATAGCATCTTTGCTCTTTCTGATAAGGGGGCGACCATCTCCGAATTGAGCCAAACGCTGGTATAAGACTCGTCTCATGACTCCCTAGCCATTTGTATGTTGTCATTTCTGATTTTAGCAGGTAAAACGTAAGGCCTGCTAAAGAATCACGCGGGGAGGCCTTAAATTTCGTCATGGAGCAATCGTCCTAGATTGCTGTGAAGGTTCGTACCAGTAGAGTCTAATGTGCGTAAATGTTAACTGGCCGTATATTCTCTGGTGAGCTGAAACAGAAAGCTGGCAGAAAGCCACTCTTGCTGTTTCGTGTGTACGGACATCGGGATAGTACCAAAAAGCATGTTCTTCATCTGGCGATGCTTGATGTCTACCGTAGACACCTTCATACGT';
            string[] inlines = x.Split();
            int k = int.Parse(inlines[0]);
            string text = inlines[1];
            Dictionary<string, List<string>> res = DeBruijn(k,text);
            multipleGraphPrint(res);
        }
    }
}
