package Task1;

import java.util.Scanner;


interface client { //Creating interface
	
	// 2 methods in interface
	void input();
	void output();
	
}

abstract class tprice{   // abstract class
	
	abstract void price();   //abstract method
}
public class Table extends tprice implements client {
	int material;
	int type;
	public void input()
	{
	    Scanner myObj = new Scanner(System.in);
		System.out.println("Select type of material for Table : 1. wood 2. Metal 3.Plastic ");
		material=myObj.nextInt();
		System.out.println("Select 1. foldable 2.non- foldable ");
		type=myObj.nextInt();
	}
	public void output()
	{
		switch(material)
		{
		case 1: System.out.println("wood"); break;
		case 2: System.out.println("metal"); break;
		case 3: System.out.println("plastic"); break;
		default: break;
		}
		switch(type)
		{
		case 1: System.out.println("foldable"); break;
		case 2: System.out.println("non-foldable"); break;
		default: break;
		}			
	}
	public void price() // override the method of abstract class
	{
		System.out.println("$800"); 		
	}
	
	
	public static void main(String args[])
	{
		client c =new Table(); // Create objects of concrete class
		c.input();
		c.output();
	    tprice n= new Table();
		n.price();
		
	}
}