using System;

namespace BA1L
{
    class Program
    {
        //A solution to a Rosalind bioinformatics problem
        //Problem Title: Implement PatternToNumber
        //URL: http://rosalind.info/problems/ba1l/
        static void Main(string[] args)
        {
            long PatternToNumber(string pattern)
            {
                long res = 0;
                for (int k = 0; k < pattern.Length; k++)
                {
                    if (pattern[pattern.Length-k-1] == 'C')
                    {
                        res = res + 1 * (long)(Math.Pow(4, k));
                    }
                    if (pattern[pattern.Length - k - 1] == 'G')
                    {
                        res = res + 2 * (long)(Math.Pow(4, k));
                    }
                    if (pattern[pattern.Length - k - 1] == 'T')
                    {
                        res = res + 3 * (long)(Math.Pow(4, k));
                    }
                }
                return res;
            }

            string x = "CTTCTCACGTACAACAAAATC";
            string[] inlines = x.Split();
            string text = inlines[0];
            Console.WriteLine(PatternToNumber(text));
        }
    }
}
