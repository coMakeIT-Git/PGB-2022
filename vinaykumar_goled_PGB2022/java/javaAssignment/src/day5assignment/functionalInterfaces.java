package day5assignment;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.Collectors;

class Employee{
	private String name;
	public Employee(String name) {
		this.name = name;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
}

public class functionalInterfaces {
	public static void main(String[] args) {
		Predicate<String> predicatefunc = t -> t.length() > 5;
		System.out.println(predicatefunc.test("Vinay"));
		System.out.println(predicatefunc.test("Ram"));
		List<String> l = new ArrayList<>();
		l.add("harish");
		l.add("Krishna");
		l.add("John");
		List<String> filtered = l.stream().filter(s -> s.length() > 5).collect(Collectors.<String>toList());
		System.out.println(filtered);
		
		Function<Integer, Integer> functionFunc = t->t*2;
		System.out.println(functionFunc.apply(5));
		Function<Integer, String> functionFunc1 = t->t.toString();
		System.out.println(functionFunc1.apply(5));
		
		Supplier<Integer> supplierFunc = () -> 20;
		System.out.println(supplierFunc.get());
		
		Employee emp = new Employee("harish");
		Consumer<Employee> updateName = p -> p.setName("Praveen");
		updateName.accept(emp);
		System.out.println(emp.getName());
	}
}
