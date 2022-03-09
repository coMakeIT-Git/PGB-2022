package day5;
import day3.*;

import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.function.Function;


class printEmpDetails {
	printEmpDetails(Employee e) {
		System.out.println("Name : "+e.name+", ID : "+e.id);
	}
}



class CompareByName {
    public static int compare(Employee a, Employee b)
    {
    	return a.name.compareTo(b.name);
    }
}

class CompareByID {
    public int compare(Employee a, Employee b)
    {
    	return a.id-b.id;
    }
}

// Implementing the Runnable Interface.
class EmpReg implements Runnable{
	
	int Id;
	String grp;
	List<String> givenList = Arrays.asList("A","B","C","D","E","F");
	// Using Function to get Employee ID
	static Function<Integer, Integer> AssignID = a -> 10000-a;
	
    public EmpReg(int id) {
        this.Id = id;
    } 
	
    // Defining Run for Runnable Interface
	public void run() {
		Random rand = new Random();
		// Use Thread Pool to Register Employees and assign them to Different Groups
		for (int i = Id;i < Id+20;i++ ) {
			grp = givenList.get(rand.nextInt(givenList.size()));
			// Synchronized Method
			
			Training.assign_to_group(grp, AssignID.apply(i),"Employee_"+i);//AssignName.apply(i));
			// System.out.println(Training.Groups.get(grp).size());
		}
	}
	

}

public class BatchEmployeeRegister{
	
	static final int max_threads = 10;
	
	public static void sortEmpByName(Map<String, ArrayList<Employee>> GroupList) {
		for (Map.Entry <String, ArrayList<Employee>> EmpList : GroupList.entrySet()) {
        	System.out.println("Group : "+EmpList.getKey());
        	// Method Reference : Using Static Method
        	Collections.sort(EmpList.getValue(), CompareByName::compare);
        	ArrayList<Employee> stu_list = EmpList.getValue();
        	stu_list.stream().forEach(printEmpDetails::new);
		}
        	
	}

	public static void sortEmpByID(Map<String, ArrayList<Employee>> GroupList) {
		for (Map.Entry <String, ArrayList<Employee>> EmpList : GroupList.entrySet()) {
        	System.out.println("Group : "+EmpList.getKey());
        	CompareByID cmpbyid = new CompareByID();
        	// Method Reference : Using Instance
        	Collections.sort(EmpList.getValue(), cmpbyid::compare);
        	ArrayList<Employee> stu_list = EmpList.getValue();
        	
        	// Method Reference : Using Constructor
        	stu_list.stream().forEach(printEmpDetails::new);
		}
        	
	}
	
	
	public static void main(String[] args) throws InterruptedException {
		
        Runnable r1 = new EmpReg(1001);
        Runnable r2 = new EmpReg(1021);    
        Runnable r3 = new EmpReg(1041);
        Runnable r4 = new EmpReg(1061);
          
        // Add a thread pool in your class. Use Executor framework
        // Create a Thread Pool With max 10 Threads
        ExecutorService pool = Executors.newFixedThreadPool(max_threads);  
         
        // Create Multiple Threads To Register Employees
        pool.execute(r1);
        pool.execute(r2);
        pool.execute(r3);
        pool.execute(r4);
        
        // ThreadPool ShutDown
        pool.shutdown();  
        
        // Sleep to Update the Groups List
        Thread.sleep(10);
        
        // Print The Updated Employees Data after Using ThreadPool
        // Training.print_group_data();
        
        sortEmpByName(Training.Groups);
        
        sortEmpByID(Training.Groups);
        
	}
}
