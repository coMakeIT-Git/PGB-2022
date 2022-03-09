package day3;

import java.util.*;
import day2.Student;

//Interface Class
interface Progress {
	// Declare 2 methods in interface
	public double averageMarks();
	public void displayMarks();
}

//Abstract class
abstract class Intern extends Student{
	static ArrayList<String> taskList = new ArrayList<String>();
	
	public Intern(int id, String name) {
		super(id, name);
	}

	// Add method with definition in abstract class
	abstract void listTasks();

	public void assigntask(String str){
		taskList.add(str);
	}
}

//Concrete class
public class Employee extends Intern implements Progress{
	public static Map<String, Integer> marksSheet = new HashMap<String, Integer>();
	
	public Employee(int id, String name) {
		super(id, name);
	}
    
	@Override
	public double averageMarks() {
		Integer sum = 0;
		if(!marksSheet.isEmpty()) {
			for (Map.Entry <String, Integer>topic : marksSheet.entrySet()) {
		        sum += topic.getValue();
		    }
		    return sum.doubleValue() / marksSheet.size();
		}
		return sum;
	}

	@Override
	public void displayMarks() {
		System.out.println("Printing MarksSheet for "+this.name+" : ");
		if(!marksSheet.isEmpty()) {
			for (Map.Entry <String, Integer>topic : marksSheet.entrySet()) {
		        System.out.println(topic.getKey()+" : "+topic.getValue());
		    }
		}
	}

	@Override
	public void listTasks() {
    	System.out.println("Printing Pending TaskList for "+this.name+" : ");
        for (String s : taskList) {
            System.out.println(s);
        }
	}
	
	// Concrete class method
	public void giveMarks(String Topic, int marks) {
		if (!marksSheet.containsKey(Topic)) {
			marksSheet.put(Topic, marks);
		} else {
			marksSheet.replace(Topic, marks);
		}
	}
}