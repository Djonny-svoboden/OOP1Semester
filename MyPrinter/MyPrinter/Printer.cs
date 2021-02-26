using System;

namespace MyPrinter
{
    class Printer
    {
        public static int inkCounter = 100;
        public string name { get; set; } 
        public int paperCount { get; set; }
        public int droch { get; set; }
        public int maxPapepCount { get; set; }
        public  Printer(string Name, int PaperCount,int Droch, int MaxPapepCount)
        {
            this.name=Name;
            this.paperCount=PaperCount;
            this.droch=Droch;
            this.maxPapepCount=MaxPapepCount;

        }
        public void Print()
        {
            inkCounter = inkCounter - (droch * 10);
            if (droch <= paperCount)
            {
                this.paperCount = this.paperCount - this.droch;
                Console.WriteLine("printed " + droch + " lists " + " inkcounter is " + inkCounter);
            }
            


        }
        public void Cleaning() 
        {
            inkCounter = inkCounter - 50;
            Console.WriteLine("printer now clean");
        }
        public void paperFilling() 
        {   
            if (paperCount < maxPapepCount) 
            {
                paperCount = maxPapepCount;
                Console.WriteLine("printer now clean");
            }
        }
        public static void OMM(string state) 
        {
            if (state == "on") 
            {
                Console.WriteLine("device is on");
            }
            else if (state == "off") {
                Console.WriteLine("device is off");
            }
            else {
                Console.WriteLine("bruj");
            }
        }


    }
    class Program
    {
       
        static void Main(string[] args)
        {
            string state="on";
            Printer printer1 = new Printer("Kanon", 7, 3, 11);
            //Console.WriteLine(printer1.name);
            //Console.WriteLine(printer1.droch);
            //Console.WriteLine(printer1.paperCount);
            //Console.WriteLine(printer1.maxPapepCount);
            printer1.Print();
            printer1.Cleaning();
            Printer.OMM(state);
           
        }
    }
}
