package Day3Assignment;

import java.util.*;

interface Human{
    public void read(); //abstract method-1
    public void write();  //abstract method-2
}


abstract class Person{
	
		public void eat()
		{
			System.out.println("Person is doing lunch...");
		}
		public static String play()
		{
			return "Person is playing Cricket...";
		}
		
	}
class sort implements Comparator<Student>{
	public int compare(Student s1,Student s2)
	{
		return s1.student_name.charAt(0)-s2.student_name.charAt(0);
	}
}

public class Student extends Person implements Human {
		String student_name;
		int stuId;
		Student(int stuId,String student_name)
		{
			this.stuId=stuId;
			this.student_name=student_name;
		}
		//implementing abstract method in interface Vehicle
		public void read()
		{
			System.out.println("Student is reading...");
		}
		//implementing abstract method in interface Vehicle
		public void write()
		{
			System.out.println("Student is writing...");
		}
		@Override
		//overriding abstract method from abstract Automobile
		public void eat()
		{
			System.out.println("Person had completed the lunch...");
		}
		public static void main(String args[])
		{
		   //Creating Object for Concrete Class
		   Student obj=new Student(01,"RAM");
		   System.out.println("Calling Overriding Methods");
		   obj.read(); //Calling method read
		   obj.write();  //Calling method write
		   obj.eat();  //Calling method eat
		   //Accessing abstract class Method
		   System.out.println(Person.play());
		   System.out.println();
		   List<Student> l=new LinkedList<>();
		   l.add(new Student(02,"Akhil"));
		   l.add(new Student(01,"Nithish"));
		   l.add(new Student(03,"Balaji"));
		   System.out.println("Printing the elements using List");
		   for(int i=0;i<l.size();i++) System.out.println(l.get(i).stuId+" "+l.get(i).student_name);
		   System.out.println();
		   Map<Student,String>m=new HashMap<>();
		   System.out.println("Printing the elements using Map");
		   m.put(new Student(02,"Akhil"),"Jiyaguda");
		   m.put(new Student(01,"Nithish"),"HayathNagar");
		   m.put(new Student(02,"Balaji"),"Karmanghat");
		  
		   //for(int i=0;i<m.size();i++) System.out.println(m.get(i).stuId+" "+m.get(i).student_name);
		   for(Map.Entry<Student,String> f:m.entrySet())
		   {
			   System.out.println(f.getKey().stuId+" "+f.getKey().student_name+" "+f.getValue());
		   }
		   System.out.println();
		   Set<Student> set=new HashSet<>();
		   for(int i=0;i<l.size();i++)
		   {
			   set.add(l.get(i));
		   }
		   System.out.println("Printing the elements using Set");
		   for(Student st:set)
		   {
			   System.out.println(st.stuId+" "+st.student_name);
		   }
		   System.out.println();
		   //sorting the list
		   System.out.println("Printing elements after sorting");
		   Collections.sort(l,new sort());
		   for(int i=0;i<l.size();i++)
		   {
			   System.out.println(l.get(i).student_name);
		   }
		   //iterating using streams
		   System.out.println("Printing Elements By Java Streams");
		   l.stream().forEach((c) -> System.out.println(c.student_name));
         	
	}
}
		

