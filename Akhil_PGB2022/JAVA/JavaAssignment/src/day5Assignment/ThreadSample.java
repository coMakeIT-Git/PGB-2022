package day5Assignment;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import day2Assignment.test.Employee;

class ThreadTask implements Runnable{
	List<Employee> emp;
	ThreadTask(List<Employee> e){
		this.emp = e;
	}
	@Override
	synchronized public void run() {
		for(Employee e:emp) {
			System.out.println(" empId:"+e.getEmpId()+" empName:"+e.getEmpName()+" empMail:"+e.getEmail());
		}
	}
	
}
class ThreadSample{
	public static void main(String[] args) {
		List<Employee> empGrp1 = new ArrayList<>();
		for(int i=0;i<100;i++) {
			empGrp1.add(new Employee(101-i,"Name"+i,"Name"+i+"@gmail.com"));
		}
		List<Employee> empGrp2 = new ArrayList<>();
		for(int i=0;i<100;i++) {
			empGrp2.add(new Employee(1001-i,"Name"+(i+1000),"Name"+(1000+i)+"@gmail.com"));
		}
		
		ExecutorService ex = Executors.newFixedThreadPool(4);
		ex.execute(new ThreadTask(empGrp1));
		ex.execute(new ThreadTask(empGrp2));
		
		ex.shutdown();
	}
}

