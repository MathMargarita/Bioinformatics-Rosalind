using System;
using System.Collections.Generic;

namespace BA3C
{
    class BA3C
    {
        //A solution to a ROSALIND bioinformatics problem.
        //Problem Title: Construct the Overlap Graph of a Collection of k-mers
        //Rosalind ID: BA3C
        //URL: http://rosalind.info/problems/ba3c/
        static void Main(string[] args)
        {
            string prefix(string pattern)
            {
                //substring of pattern without  the last letter
                return pattern.Substring(0, pattern.Length-1);
            }
            string suffix(string pattern)
            {
                //substring of pattern without first letter
                return pattern.Substring(1, pattern.Length - 1);
            }
            
            Dictionary<string,List<string>> overlapGraph(string[]seq)
            {
                Dictionary<string, List<string>> adjacency = new Dictionary<string, List<string>>();
                Array.Sort(seq);
                foreach (string pattern in seq)
                {
                    adjacency[pattern] = new List<string>();
                    foreach (string pattern2 in seq)
                    {
                        if (suffix(pattern) == prefix(pattern2))
                        {
                            adjacency[pattern].Add(pattern2);
                        }
                    }
                }
                return adjacency;
            }
            void graphPrint(Dictionary<string, List<string>> adj)
            {
                foreach (string key in adj.Keys)
                {
                    if (adj[key].Count>0)
                    {
                        Console.WriteLine(key + " -> " + adj[key][0]);
                    }
                }
            }


            string x = "ATGCG\nGCATG\nCATGC\nAGGCA\nGGCAT";
            string[] inlines = x.Split();
            Dictionary<string, List<string>> res = overlapGraph(inlines);
            graphPrint(res);
        }
    }
}
