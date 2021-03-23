using System;
using System.Collections.Generic;

namespace BA1M
{
    class Program
    {
        //A solution to a Rosalind bioinformatics problem
        //Problem Title: Implement NumberToPattern
        //URL: http://rosalind.info/problems/ba1m/
        static void Main(string[] args)
        {
            string NumberToPattern(int number, int k)
            {
                string pattern = "";
                Dictionary<int,string> D = new Dictionary<int,string>();
                D[0] ="A" ;
                D[1] = "C";
                D[2] = "G";
                D[3] = "T";
                int q = number;
                for (int i = 0; i < k; i++)
                {
                    int r = q % 4;
                    q = (int)(q / 4);
                    pattern=pattern + D[r];
                }
                return reverse(pattern);
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

            string x = "45\n4";
            string[] inlines = x.Split();
            int number = int.Parse(inlines[0]);
            int k = int.Parse(inlines[1]);
            Console.WriteLine(NumberToPattern(number,k));
        }
    }
}
