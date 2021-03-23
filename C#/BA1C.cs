using System;

namespace BA1C
{
    class Program
    {

    //A solution to a ROSALIND bioinformatics problem.
    //Problem Title: Find the reverse complement of a DNA string
    //Rosalind ID: BA1C
    //URL: http://rosalind.info/problems/ba1c/

        static void Main(string[] args)
        {
            string x = "AAAACCCGGT";
            Console.WriteLine(reverse(complement(x)));

            string complement(string text)
            {
                string compl = "";
                int nt = text.Length;
                for (int i = 0; i < nt; i++)
                {
                    if (text[i] == 'G')
                    {
                        compl += "C";
                    }
                    if (text[i] == 'C')
                    {
                        compl += "G";
                    }
                    if (text[i] == 'A')
                    {
                        compl += "T";
                    }
                    if (text[i] == 'T')
                    {
                        compl += "A";
                    }
                }
                return compl;
            }
            string reverse(string text)
            {
                string rev = "";
                int nt = text.Length;
                for (int i = nt - 1; i > -1; i--)
                {
                    rev = rev + text[i];
                }
                return rev;
            }

        }
    }
}
