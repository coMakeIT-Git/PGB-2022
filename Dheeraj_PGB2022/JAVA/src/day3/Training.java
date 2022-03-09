package day3;
import java.util.*;

class CompareName implements Comparator<Employee> {
    public int compare(Employee a, Employee b)
    {
    	return a.name.compareTo(b.name);
    }
}

class CompareID implements Comparator<Employee>
{
    public int compare(Employee a, Employee b)
    {
    	return a.id-b.id;
    }
}

public class Training{
	public static ArrayList<Employee> Employeelist = new ArrayList<>();
    protected static Set<Employee> Employeeset = new HashSet<>();
    public static Map<String, ArrayList<Employee>> Groups = Collections.synchronizedMap(new HashMap<String, ArrayList<Employee>>());

    
   public static int add_Employee_to_list(int id, String name) { 
		Employee new_Employee = new Employee(id, name);
        Employeelist.add(new_Employee);
		//        System.out.println("New Employee Added To EmployeeList:\n\tName : "+name+"\n\tID : "+id);
		return (Employeelist.size() - 1);
	}
	
	public static void add_Employee_to_set(int id, String name) { 
		Employee new_Employee = new Employee(id, name);
        Employeeset.add(new_Employee);
//        System.out.println("New Employee Added To EmployeeSet:\n\tName : "+name+"\n\tID : "+id);
	}
	
	synchronized private static void assign_to_group(String to_group, Employee s) {
	    if (Groups.containsKey(to_group)) {
	    	Groups.get(to_group).add(s);
	    } else {
	    	Groups.put(to_group, new ArrayList<Employee>());
	    	Groups.get(to_group).add(s);
	    }
//	    System.out.println("Employee Assigned To to_group "+to_group+":\tName : "+s.name+", ID : "+s.id);
	}
	
	public static void assign_to_group(String to_group, ArrayList<Employee> s) {
        if (Groups.containsKey(to_group)) {
    	    Groups.get(to_group).addAll(s);
    	} else {
    	    Groups.put(to_group, new ArrayList<Employee>());
    	    Groups.get(to_group).addAll(s);
    	}
//        System.out.println("Employee Assigned To to_group "+to_group+" : ");
//        for (Employee stu : s) {
//        	System.out.println("Name : "+stu.name+", ID : "+stu.id);
//        }
	}
	
	public static void assign_to_group(String to_group, int id, String name) {
		Employee new_Employee = new Employee(id, name);
        Employeeset.add(new_Employee);
	    if (Groups.containsKey(to_group)) {
	    	Groups.get(to_group).add(new_Employee);
	    } else {
	    	Groups.put(to_group, new ArrayList<Employee>());
	    	Groups.get(to_group).add(new_Employee);
	    }
//	    System.out.println("Employee Assigned To to_group "+to_group+":\tName : "+new_Employee.name+", ID : "+new_Employee.id);
	}
	
	public static void print_Employeelist() {
    	System.out.println("Printing Employees List (ID, Name):");
        for (Employee s : Employeelist) {
            System.out.println(s.id+", "+s.name);
        }
	}
	
	public static void print_Employeeset() {
    	System.out.println("Printing Employees Set :");
        for (Employee s : Employeeset) {
            System.out.println(s.id);
        }
	}
	
	public static void print_group_data() {
        System.out.println("Printing Employee Groups Data :");
        for (Map.Entry <String, ArrayList<Employee>>m : Groups.entrySet()) {
        	System.out.println("Group : "+m.getKey());
        	ArrayList<Employee> stu_list = sortbyid(m.getValue());
        	for (int i = 0; i < stu_list.size();i++) {
        		Employee stu = stu_list.get(i);
        		System.out.println("Name : "+stu.name+", ID : "+stu.id);
        	}
        }
	}
	
	public static ArrayList<Employee> sortbyname(ArrayList<Employee> list) {
		ArrayList<Employee> s_list = list;
		CompareName nameCompare = new CompareName();
        Collections.sort(s_list, nameCompare);
		return s_list;
	}
	
	public static ArrayList<Employee> sortbyid(ArrayList<Employee> list) {
		ArrayList<Employee> s_list = list;
		CompareID idCompare = new CompareID();
        Collections.sort(s_list, idCompare);
		return s_list;
	}
	
    
    public static void main(String[] args){
     	// Create objects of concrete class
        Employee emp = new Employee(1002, "Employee2");
        
        emp.giveMarks("Java", 29);
        emp.giveMarks("Python", 30);
        emp.giveMarks("JavaScript", 28);
        emp.giveMarks("ReactJS", 27);
        emp.giveMarks("AngularJS", 26);
        
        emp.displayMarks();
        
        System.out.println("Average Marks for "+emp.name+" : "+emp.averageMarks());
        
        emp.assigntask("Task_1");
        emp.assigntask("Task_2");
        emp.assigntask("Task_3");
        
        emp.listTasks();
        
        // Initialize a Collections List
        add_Employee_to_list(1002, "Employee2");
        add_Employee_to_list(1003, "Employee3");
        add_Employee_to_list(1004, "Employee4");
        add_Employee_to_list(1005, "Employee5");

		
        // Initialize a Collections HashSet
        add_Employee_to_set(1003, "Employee3");
        add_Employee_to_set(1004, "Employee4");
        add_Employee_to_set(1005, "Employee5");
		
		// Initialize a Collections Map
        assign_to_group("A", Employeelist);
        assign_to_group("B", emp);
        assign_to_group("B", new Employee(1007, "Employee7"));
        assign_to_group("B", new Employee(1008, "Employee8"));
        assign_to_group("C", 1009, "Employee9");
        assign_to_group("C", 1010, "Employee10");
        assign_to_group("C", 1011, "Employee11");
		
		
        // Iterate and Print List
        print_Employeelist();
        
        // Iterate and Print HashSet
        print_Employeeset();
        
        // Iterate and Print Map
        print_group_data();
        
        // Sort the Collections of list
        sortbyid(Employeelist);
        
        // Java Stream to iterate the list
        System.out.println("Printing Employee List using Java Stream");
        Employeelist.stream().forEach((a)->System.out.println("Name : "+a.name+", ID : "+a.id));
        
    }
}




