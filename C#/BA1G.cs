using System;

namespace BA1G
{
    class Program
    {
    //A solution to a ROSALIND bioinformatics problem.
    //Problem Title: Compute the Hamming Distance Between Two Strings
    //Rosalind ID: BA1G
    //URL: http://rosalind.info/problems/ba1g

        static void Main(string[] args)
        {

            int HammingDistance(string p,string q)
            {
                //Computes the hamming distance between strings p and q
                if (p.Length!=q.Length)
                {
                    return -1;
                }
                int dist = 0;
                (char first, char second)[] zippq = new (char first, char second)[p.Length];
                for (int i = 0; i < p.Length; i++)
                {
                    zippq[i] = (p[i], q[i]);
                }
                foreach ((char first,char second) x in zippq)
                {
                    if (x.first!=x.second)
                    {
                        dist = dist + 1;
                    }
                }
                return dist;
                
            }

            string p = "GGGCCGTTGGT";
            string q = "GGACCGTTGAC";
            Console.WriteLine(HammingDistance(p, q));
        }
    }
}
