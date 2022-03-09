package saikeerthana;
import java.util.*;
public class Program {
	 
	 public static void main(String[] args) {
		 System.out.println("Enter name");
	        Scanner input = new Scanner(System.in);
	        String str = input.nextLine();

	        char []data=str.toCharArray();
	        Set s = new HashSet();
	        for(int i=0; i<data.length; i++){
	            s.add(data[i]);
	        }
	        Object[] s1 = s.toArray();

	        System.out.print("{ ");
	        for(int i=0; i<s.size(); i++){
	            System.out.print(s.toArray()[i]+"=");
	            Collection t = new ArrayList();
	            char c=(Character) s1[i];
	            for(int j=0;j<data.length; j++){
	                if(c==data[j]){
	                    t.add(j);
	                }
	            }
	            System.out.print(t+ ", ");

	        }
	        System.out.print("}");

	    }
	
}
