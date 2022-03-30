package Day5Assignment;
import java.util.*;
class Sample
{
	static int mul=1,sum=0;
	static float div=1;
	Sample(int i)
	{
		
		sum+=i;
	
	}
	public int Multiplication(int i)
	{
		mul*=i;
		return mul;
	}
	static float Division(float i)
	{
		div/=i;
		return div;
	}
	

}
public class MethodReference {
	public static void main(String args[])
	{
		List<Integer> l=new ArrayList<>();
		l.add(30);
		l.add(20);
		l.add(10);
		Sample obj=new Sample(1);
		l.forEach(Sample::new);  
		//Reference to a constructor
		System.out.println("Sum Of the list is using Constructor:");
		System.out.println(obj.sum);
		l.forEach(Sample::Division);
		
		//Reference To a static Method
		System.out.println("Using Static Method Reference:");
		System.out.println(obj.div);
		
		//Reference to a Instance Method,
		System.out.println("USing Instance Method Reference:");
		l.forEach(obj::Multiplication);
		System.out.println(obj.mul);
		
		
		
	}
}
