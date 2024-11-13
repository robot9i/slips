namespace assign9q1 
{ 
    internal class Program 
    { 
        static void Main(string[] args) 
        { 
            string name; 
            int count = 0; 
            Console.WriteLine("enter the string:"); 
            name = Console.ReadLine(); 
            char ch; 
            Console.WriteLine("enter a character:"); 
            ch = Convert.ToChar( Console.ReadLine()); 
            for(int i=0;i<name.Length;i++) 
            { 
                if (name[i]==ch) 
                { 
                    count++; 
                } 
            } 
            Console.WriteLine(ch + " is occured in "+ name +"\t"+count+ "\tTimes"); 
        } 
    } 
} 


Q2


  internal class Program 
    { 
        static void Main(string[] args) 
        { 
        person p1 = new person(); 
        student p2 =new student(); 
        instructor p3 = new instructor(); 
        p1.print(); 
        p2.print(); 
        p3.print(); 
        } 
    } 
 
    public class person 
    { 
        public string name; 
    DateTime date = new DateTime(); 
    public person() 
        { 
        Console.WriteLine("Enter the person's name"); 
        name = Console.ReadLine(); 
        Console.WriteLine("Enter the person's birth date"); 
        date = DateTime.Parse(Console.ReadLine()); 
 
        } 
    public void print() 
        { 
        Console.WriteLine("person name="+name); 
        Console.WriteLine("person date of birth ="+date); 
        } 
        
        } 
    public class student : person 
    { 
        public string course; 
        public student() 
        { 
        Console.WriteLine("Enter the student's course"); 
        course = Console.ReadLine(); 
    } 
        public void print() 
        { 
        Console.WriteLine("student course=" + course); 
    } 
    } 
    class instructor : person 
    { 
        public double salary; 
        public instructor() 
        { 
        Console.WriteLine("Enter the instructor's salary"); 
        salary = Convert.ToDouble( Console.ReadLine()); 
    } 
        public void print() 
        { 
        Console.WriteLine("instructor salary=" + salary); 
    } 
    }