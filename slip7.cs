namespace assign7q1 
{ 
    internal class Program 
    { 
        static void Main(string[] args) 
        { 
            int[,] m1=new int[3,3]; 
            int[,] m2=new int[3,3]; 
            int[,] add = new int[3, 3]; 
            int[,] trans = new int[3, 3]; 
            Console.WriteLine("enter data in matrix 1:"); 
            for(int i=0;i<3;i++) 
            { 
                for(int j=0;j<3;j++) 
                { 
                    m1[i, j] = Convert.ToInt32(Console.ReadLine()); 
                } 
            } 
            Console.WriteLine("enter data in matrix 2:"); 
            for (int i = 0; i < 3; i++) 
            { 
                for (int j = 0; j < 3; j++) 
                { 
                    m2[i, j] = Convert.ToInt32(Console.ReadLine()); 
                } 
            } 
            Console.WriteLine("1.addition"); 
            Console.WriteLine("2.tranpose"); 
            Console.WriteLine("enter your choice"); 
            int choice = Convert.ToInt32(Console.ReadLine()); 
            switch(choice) 
            { 
                case 1: 
                    for (int i = 0; i < 3; i++) 
                    { 
                        for (int j = 0; j < 3; j++) 
                        { 
                            add[i, j] = m1[i, j] + m2[1, j]; 
                        } 
                    } 
                    Console.WriteLine("addition of matrix="); 
                    for (int i = 0; i < 3; i++) 
                    { 
                        for (int j = 0; j < 3; j++) 
                        { 
                            Console.WriteLine(add[i, j]); 
                        } 
                    } 
                    break; 
                case 2: 
                    Console.WriteLine("transpose of matrix 1="); 
                    for(int i=0;i<3;i++) 
                    { 
                        for(int j=0;j<3;j++) 
                        { 
                            
                                trans[i, j] = m1[j, i]; 
                             
                        } 
                    } 
                    for (int i = 0; i < 3; i++) 
                    { 
                        for (int j = 0; j < 3; j++) 
                        { 
                             
                                Console.WriteLine(trans[i, j]); 
                             
                        } 
                    } 
                    break; 
 
            } 
             
        } 
    } 
} 


Q2


namespace assign7q2 
{ 
    internal class Program 
    { 
        static void Main(string[] args) 
        { 
            Stack stack = new Stack(5); 
            
            Console.WriteLine("\nInput some elements onto the stack:"); 
            stack.Push(10); 
            stack.Push(20); 
            stack.Push(30); 
            stack.Push(40); 
            stack.Push(50); 
            Console.WriteLine("Total elements present in" + 
                     " stack: {0}", stack.Count); 
            stack.Pop(); 
            Console.WriteLine("Total elements present in" + 
                     " stack: {0}", stack.Count); 
            Console.WriteLine("Topmost element of my_stack " + 
                              "is: {0}", stack.Peek()); 
            stack.Clear(); 
            if(stack.Count==0) 
            { 
                Console.WriteLine("stack is empty"); 
            } 
            else 
            { 
                Console.WriteLine("stack is full"); 
            } 
        } 
    } 
} 
 
