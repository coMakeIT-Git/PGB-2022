import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Collections;
import java.util.stream.Collectors;
interface Student {
  public void voice();
  public void work();
}
abstract class Training{
public void CMITTraining()
{
System.out.println("CMIT training with Plan");
}
abstract public void CMITFeedback(String a);
public abstract int adde(int n1, int n2);
}
class Shyam implements Student {
  public void voice() {
    System.out.println("Says: Hello");
  }
  public void work() {
    System.out.println("Always Sleeps");
  }
}
class Concrete extends Training{
int id;
String a;
public Concrete(int id){
this.id=id;
}
public void CMITFeedback(String a){
System.out.println("Marked as "+a);
}
public int adde(int num1, int num2){
return num1+num2;
  }
}
class interfaceConcept{
  public static void main(String[] args) {
   Shyam s = new Shyam();
   s.voice();
   s.work();
    System.out.println("Salary CTC and initial feedback:"); 
   Concrete c1 = new Concrete(34);
   System.out.println(c1.adde(3,4));
   c1.CMITFeedback("Good");
   Concrete c2 = new Concrete(24);
   System.out.println(c2.adde(5,6));
   c2.CMITFeedback("Bad");
   Concrete c3 = new Concrete(1034);
   System.out.println(c3.adde(7,5));
   c3.CMITFeedback("Worst");
   Concrete c4 = new Concrete(1);
   System.out.println(c4.adde(1,2));
   c4.CMITFeedback("Better");
   List<Object> a = new ArrayList<Object>();
      a.add(c1);
      a.add(c2);
      a.add(c3);
      a.add(c4);
   List<Integer> al = new ArrayList<Integer>();
      al.add(c1.id);
      al.add(c2.id);
      al.add(c3.id);
      al.add(c4.id);
   HashSet<Object> s1 = new HashSet<Object>();
      s1.add(c1);
      s1.add(c2);
      s1.add(c3);
      s1.add(c4);
   HashMap<Integer,Object> m1 = new HashMap<Integer,Object>();
      m1.put(1,c1);
      m1.put(2,c2);
      m1.put(3,c3);
      m1.put(4,c4);
   System.out.println("List of Objects are:"); 
   for(Object number: a)
   System.out.println(number);
   System.out.println("HashMap of objects are:"); 
   for(Map.Entry m : m1.entrySet())    
   System.out.println(m.getKey()+" "+m.getValue());
   System.out.println("Set of Objects are:"); 
   for(Object b:s1)  
   System.out.println(b);
   System.out.println("Original ID's are:"); 
   for(int id:al)
   System.out.println(id);
   System.out.println("Sorted Id's are:");
   List<Integer> sortedList =al.stream().sorted().collect(Collectors.toList());
   sortedList.forEach(System.out::println);  
}
}
