package util;
import java.util.*;
import java.util.HashSet;
import java.util.Set;
public class Hashcodeequals {
	public static void main(String[] args) {
	Student s1 = new Student("Sowmya");
	Student s2 = new Student("Sowmya");
	s1.setid("CMI-056");
	s2.setid("CMI-056");
	Set<Student> s = new HashSet<>();
	s.add(s1);
	s.add(s2);
	System.out.println(s);
	if(s1.equals(s2)) {
		System.out.println("Yes");
	}
 	else {
		System.out.println("No");
	}
}
public static void main(String args) {
	System.out.println("This is main");
}
}