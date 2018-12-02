using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;

namespace advent
{
    class Ap_part_1
    {
        private static void Main(string[] args)
        {
            List<int> delay = new List<int>();
            List<string> lines = File.ReadAllLines("D:\\AdventOfCode\\advent\\advent\\input.txt").ToList();
            StreamWriter sw = new StreamWriter("D:\\AdventOfCode\\advent\\advent\\output-1.txt");

            int doubles = 0;
            int triples = 0;

            foreach (string line in lines) {
                var counts = line.GroupBy(c => c)
                                 .OrderBy(c => c.Key)
                                 .ToDictionary(grp => grp.Key, grp => grp.Count());
                if (counts.ContainsValue(2))
                    doubles++;
                if (counts.ContainsValue(3))
                    triples++;
            }

            sw.WriteLine((doubles * triples).ToString());
            sw.Close();
        }
    }
}
