namespace assign8q1 
{ 
    internal class Program 
    { 
        static void Main(string[] args) 
        { 
            int[] arr = new int[5]; 
            Console.WriteLine("enetr elements in array:"); 
            for(int i=0;i<5;i++) 
            { 
                arr[i] = Convert.ToInt32(Console.ReadLine()); 
            } 
            Console.WriteLine("maximum number in array="+arr.Max()); 
            Console.WriteLine("maximum number in array=" + arr.Min()); 
        } 
    } 
} 


Q2

using System; 
using System.Collections.Generic; 
using System.ComponentModel.Design; 
using System.Data; 
using System.Data.SqlClient; 
using System.Linq; 
using System.Text; 
using System.Threading.Tasks; 
namespace assign8q2 
{ 
    internal class Program 
    { 
        static void Main(string[] args) 
        { 
            string connetionString; 
            SqlConnection cnn; 
            connetionString = @"Data 
Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=""E:\sujata\windows 
application\assig6q2\Database2.mdf"";Integrated Security=True"; 
            cnn = new SqlConnection(connetionString); 
            cnn.Open(); 
            Console.WriteLine("Connection Open  !"); 
            Console.WriteLine("students who got greter than 90%"); 
            SqlCommand command = new SqlCommand("select * from student where 
percentage>50", cnn); 
            SqlDataReader reader= command.ExecuteReader(); 
            while(reader.Read()) 
            { 
                Console.WriteLine("id=" + reader["id"].ToString()); 
                Console.WriteLine("name=" + reader["name"]); 
                Console.WriteLine("percentage=" + reader["percentage"]); 
            } 
            reader.Close(); 
            Console.WriteLine("students name starting with k letter"); 
            SqlCommand command1 = new SqlCommand("select * from student where 
name like 'k%' ", cnn); 
            SqlDataReader reader1 = command1.ExecuteReader(); 
            while (reader1.Read()) 
            { 
                Console.WriteLine("id=" + reader1["id"].ToString()); 
                Console.WriteLine("name=" + reader1["name"]); 
                Console.WriteLine("percentage=" + reader1["percentage"]); 
            } 
            reader1.Close(); 
            SqlCommand command2 = new SqlCommand("delete from student where 
percentage <50 ", cnn); 
            int result = command2.ExecuteNonQuery(); 
            if(result>0) 
            { 
                Console.WriteLine("student was removed"); 
            } 
            else 
            { 
                Console.WriteLine("cant find student"); 
            } 
            cnn.Close(); 
        } 
    } 
} 
