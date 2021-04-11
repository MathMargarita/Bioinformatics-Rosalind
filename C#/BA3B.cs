using System;

namespace BA3B
{
    class BA3B
    {
        //A solution to a ROSALIND bioinformatics problem.
        //Problem Title: Reconstruct a String from its Genome Path
        //Rosalind ID: BA3B
        //URL: http://rosalind.info/problems/ba3b/
        static void Main(string[] args)
        {
            string reconstr(string[]seq)
            {
                //Find the string spelled by a genome path
                string text = seq[0];
                for (int i = 1; i < seq.Length; i++)
                {
                    text = text + seq[i][seq[i].Length - 1];
                }
                return text;
            }

            string x = "ACCGA\nCCGAA\nCGAAG\nGAAGC\nAAGCT";
            string[] inlines = x.Split();
            string res = reconstr(inlines);
            Console.WriteLine(res);
        }
    }
}
