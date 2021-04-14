using System;
using System.Collections.Generic;

namespace BA3E
{
    class BA3E
    {
        //A solution to a ROSALIND bioinformatics problem.
        //Problem Title: Construct the De Bruijn Graph of a String
        //Rosalind ID: BA3E
        //URL: http://rosalind.info/problems/ba3e/
        static void Main(string[] args)
        {

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

            Dictionary<string, List<string>> DeBruijnRec(string[] Patterns)
            {
                Dictionary<string, List<string>> adjacency = new Dictionary<string, List<string>>();
                string[] sortedPatterns=Patterns;
                Array.Sort(sortedPatterns);
                foreach (string pattern in sortedPatterns)
                {
                    adjacency[prefix(pattern)] = new List<string>();
                }
                foreach (string pattern in sortedPatterns)
                {
                    adjacency[prefix(pattern)].Add(suffix(pattern));
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


            string x = "GAGG\nCAGG\nGGGG\nGGGA\nCAGG\nAGGG\nGGAG";
            string[] inlines = x.Split();
            Dictionary<string, List<string>> res = DeBruijnRec(inlines);
            multipleGraphPrint(res);
        }
    }
}
