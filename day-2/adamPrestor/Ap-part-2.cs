using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;

namespace advent
{
    class Ap_part_2
    {
        private static void Main(string[] args)
        {
            List<string> lines = File.ReadAllLines("D:\\AdventOfCode\\advent\\advent\\input.txt").ToList();
            StreamWriter sw = new StreamWriter("D:\\AdventOfCode\\advent\\advent\\output-2.txt");

            int length = lines.Count;

            for (int i = 0; i<length; i++)
            {
                for (int j = i+1; j<length; j++)
                {
                    if (Compute(lines[i], lines[j]) == 1)
                        sw.WriteLine(GetCommon(lines[i], lines[j]));
                }
            }
            sw.Close();
        }

        public static string GetCommon(string s, string t)
        {
            string result = "";
            for (int i = 0; i<s.Length; i++)
            {
                if (s[i] == t[i])
                    result += s[i];
            }
            return result;
        }

        public static int Compute(string s, string t)
        {
            int n = s.Length;
            int m = t.Length;
            int[,] d = new int[n + 1, m + 1];

            if (n == 0)
                return m;

            if (m == 0)
                return n;

            for (int i = 0; i <= n; d[i, 0] = i++)
            {
            }

            for (int j = 0; j <= m; d[0, j] = j++)
            {
            }

            for (int i = 1; i <= n; i++)
            {
                for (int j = 1; j <= m; j++)
                {
                    int cost = (t[j - 1] == s[i - 1]) ? 0 : 1;

                    d[i, j] = Math.Min(
                        Math.Min(d[i - 1, j] + 1, d[i, j - 1] + 1),
                        d[i - 1, j - 1] + cost);
                }
            }
            return d[n, m];
        }
    }
}
