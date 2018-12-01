using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace advent
{
    class Ap_part_1
    {
        private static void Main(string[] args)
        {
            int delay = 0;
            StreamReader sr = new StreamReader("i-a.txt");
            StreamWriter sw = new StreamWriter("o-a-1.txt");

            string line = string.Empty;

            while ((line = sr.ReadLine()) != null)
            {
                delay += CalculateDelay(line);
            }

            sw.WriteLine(delay.ToString());

            sr.Close();
            sw.Close();
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
