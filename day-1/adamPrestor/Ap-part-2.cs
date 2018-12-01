using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace advent
{
    class Ap_part_2
    {
        private static void Main(string[] args)
        {
            List<int> delay = new List<int>();
            List<string> lines = File.ReadAllLines("i-a.txt").ToList();
            StreamWriter sw = new StreamWriter("o-a-2.txt");

            int newFreq = 0;
            int index = 0;
            int length = lines.Count;

            while (! IsContained(newFreq, delay))
            {
                delay.Add(newFreq);
                newFreq += CalculateDelay(lines[index]);
                index = (index + 1) % length;
            }

            sw.WriteLine(newFreq.ToString());
            sw.Close();
        }

        private static bool IsContained(int freq, List<int> freqList)
        {
            foreach (int oldFreq in freqList)
            {
                if (oldFreq == freq)
                    return true;
            }
            return false;
        }

        private static int CalculateDelay(string line)
        {
            char op = line[0];
            int number = 0;
            int.TryParse(line.Substring(1), out number);
            if (op == '+')
                return number;
            else
                return -number;
        }
    }
}
