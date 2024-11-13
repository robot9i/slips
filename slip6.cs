using System; 
 
internal class Program 
    { 
        static void Main(string[] args) 
    { 
        int num1; 
        int num2, ch; 
        Console.WriteLine("enter numner1:"); 
        num1 = Convert.ToInt32(Console.ReadLine()); 
 
        Console.WriteLine("enter numner2:"); 
        num2 = Convert.ToInt32(Console.ReadLine()); 
 
        Console.WriteLine("1.addition"); 
        Console.WriteLine("2.subtraction"); 
        Console.WriteLine("3.multiplication"); 
        Console.WriteLine("4.division"); 
        Console.WriteLine("enter your choice:"); 
        ch = Convert.ToInt32(Console.ReadLine()); 
            switch (ch) 
            { 
                case 1: 
                Console.WriteLine("addition="+(num1+num2)); 
                break; 
            case 2: Console.WriteLine("subtarction="+(num1 - num2)); 
                break; 
            case 3: Console.WriteLine("multiplication="+num1 * num2); 
                break; 
            case 4: Console.WriteLine("division="+num1 / num2); 
                break; 
        }   
    } 
}

Q2


namespace assig6q2 
{ 
    public partial class Form1 : Form 
    { 
        public Form1() 
        { 
            InitializeComponent(); 
        } 
 
        private void radioButtonrose_CheckedChanged(object sender, EventArgs e) 
        { 
            if(radioButtonrose.Checked==true) 
            { 
                label1.Image = Image.FromFile("E:\\sujata\\windows application\\rose.jfif"); 
            } 
 
        } 
 
        private void radioButtonmarigold_CheckedChanged(object sender, EventArgs e) 
        { 
            if (radioButtonmarigold.Checked == true) 
            { 
                
                 
                label1.Image= Image.FromFile("E:\\sujata\\windows 
application\\marigold.jpg"); 
            } 
        } 
 
        private void Form1_Load(object sender, EventArgs e) 
        { 
 
        } 
 
        private void radioButtonhabiscus_CheckedChanged(object sender, EventArgs e) 
        { 
            label1.Image = Image.FromFile("E:\\sujata\\windows application\\hibiscus.jfif"); 
        } 
 
        private void radioButtonsunflower_CheckedChanged(object sender, EventArgs e) 
        { 
            label1.Image = Image.FromFile("E:\\sujata\\windows application\\sunflower.jfif"); 
        } 
 
        private void radioButtonlily_CheckedChanged(object sender, EventArgs e) 
        { 
            label1.Image = Image.FromFile("E:\\sujata\\windows application\\lily.jfif"); 
        } 
 
        private void radioButtonjasmine_CheckedChanged(object sender, EventArgs e) 
        { 
            label1.Image = Image.FromFile("E:\\sujata\\windows application\\jasmine.jfif"); 
        } 
    } 
} 
 
 
