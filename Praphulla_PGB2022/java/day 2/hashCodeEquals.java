
import java.util.HashSet;
import java.util.Set;
public class hashCodeEquals {
	public static void main(String[] args) {
	Student s1 = new Student("Praphulla");
	Student s2 = new Student("Praphulla");
	s1.setid("CMI-043");
	s2.setid("CMI-043");
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
	System.out.println("Hey This is Main");
}
}

