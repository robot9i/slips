using System; 
namespace assign5q1 
{ 
    internal class Program 
    { 
        static void Main(string[] args) 
        { 
            int[] arr = {4,5,8,9,10}; 
            int max = 0; 
            for(int i=0;i<arr.Length;i++) 
            { 
                if (arr[i]>max) 
                { 
                    max = arr[i]; 
                } 
            } 
            Console.WriteLine("maximum number in array =" + max); 
        } 
    } 
}


Q2

namespace assign5q2 
{ 
    public partial class Form1 : Form 
    { 
        public Form1() 
        { 
            InitializeComponent(); 
        } 
        private void buttonclickme_Click(object sender, EventArgs e) 
        { 
             
            this.BackColor = System.Drawing.Color.FromName(comboBoxcolor.Text); 
        } 
 
    } 
} 
 
 
 
 