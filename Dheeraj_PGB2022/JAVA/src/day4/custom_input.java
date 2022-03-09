package day4;
import day3.*;

import java.util.Map;
import java.util.Scanner;

// Custom Exception
final class InvalidNameException extends Exception {
	public InvalidNameException(String str) {
		 System.out.println(str); 
	}
};

// Custom Functional Interface
interface Average {
	abstract double calculate(Employee e);
}

public class custom_input extends Training{
	static Scanner input = new Scanner(System.in); 
	static String Topicnames[] = {"Java", "Python", "Javascript"};
	static int empid = 1;
	static String empName = "Admin";
	static Integer sum = 0;
	
	static void validate(String name) throws InvalidNameException{    
		if(name.length() <= 2){  
			throw new InvalidNameException("Custom Exception : name '"+name+"' is too small");
	    }
	}    

	static String TakeEmpName(String empName) throws NullPointerException, InvalidNameException{
		// Take input from console
		System.out.print("Enter Name : ");
	    String name = input.nextLine();
	    if (!empName.equals(name)){
	    	validate(name);
	    } else {
	    	throw new NullPointerException("Name Is Empty!!");
	    }
	    return name;
	}
	    
	
	static int TakeEmpID(int empid, String empName) throws InvalidNameException {
		String name = TakeEmpName(empName);
	    System.out.print("Enter ID : ");
	    int id = Integer.parseInt(input.nextLine());
	    int sno = Training.add_Employee_to_list(id/empid, name);
	    System.out.println("Added");
	    return sno;
	}

	// Custom Functional Interface Using Lambda Expressions
	public static double averageMarks(Employee emp) {
		Average a = (Employee e) -> {
			if(!e.marksSheet.isEmpty()) {
				for (Map.Entry <String, Integer>topic : e.marksSheet.entrySet()) {
			        // Addition of integers
					sum += topic.getValue();
			    }
				// Calculate the average
			    return (sum.doubleValue() / e.marksSheet.size());
			}
			return sum;
		};
		return a.calculate(emp);
	}
	
	static void Employee_data(int empid, String empName) throws InvalidNameException {
		
		int sno = TakeEmpID(empid, empName);
		
	    Training.print_Employeelist();
			for(int i = 0;i < Topicnames.length;i++) {
				System.out.print("Enter Marks for "+Topicnames[i]+" : ");
			    int marks = input.nextInt();
			    Training.Employeelist.get(sno).giveMarks(Topicnames[i], marks);
			}
		System.out.println("Total Marks : "+averageMarks(Training.Employeelist.get(sno)));
		input.nextLine();
		System.out.println();
	}
	
	public static void main(String[] args) {
	    for(int i = 0;i<30;i++) {
	    	try {
		    	if(i == 2) {
		    		// Code to generate ArithmeticException Exception
		    		System.out.println("ArithmeticException Exception : ");
		    		Employee_data(0, empName);
		    	} else if (i == 1) {
		    		// Code to generate NullPointer Exception
		    		System.out.println("NullPointer Exception : ");
		    		Employee_data(empid, null);
		    	} else if (i == 3){
		    		System.out.println("Enter characters in ID To get NumberFormat Exception");
		    		Employee_data(empid, empName);
		    	} else {
		    		Employee_data(empid, empName);
		    	}
	    	} 
	    	catch (NumberFormatException e) {
	    		System.out.println("Enter a valid ID!! (NumberFormat Exception Occured)");
	    	}
	    	catch (NullPointerException e) {
	    		System.out.println("Forced NullPointerException Occured\n");
	    	}
	    	catch (ArithmeticException e) {
	    		System.out.println("Forced ArithmeticException Occured\n");
	    	}
	    	catch (InvalidNameException e) {
	    		continue;
	    	}
	    }
	}
}
