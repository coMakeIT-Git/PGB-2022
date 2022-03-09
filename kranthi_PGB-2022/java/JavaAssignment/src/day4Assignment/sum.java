package day4Assignment;

import java.util.ArrayList;
import java.util.Scanner;

public class sum {
	public static int Add(ArrayList<Integer>l) {
		int sum=0;
		for(int i=0;i<l.size();i++) {
			sum+=l.get(i);
		}
		return sum;
	}
	public static void main(String ars[]) {
		ArrayList<Integer> al=new ArrayList<Integer>();
		System.out.println("Enter numbers:");
		
		//Try Block
		Scanner sc =new Scanner(System.in);
		String str=sc.nextLine();
		
		
		try {
			if(str.equals(""))
				System.out.println("Please Enter Numbers");
			else {
				String [] arrstr=str.split(" ");
				for(String a :arrstr) {
					try {
					al.add(Integer.parseInt(a));}
					catch (NumberFormatException e) {
						e.printStackTrace();
					
				}
			}
		}
		}
			catch (NullPointerException e) {
				e.printStackTrace();}
		/* try(Scanner sc =new Scanner(System.in)){String str=sc.nextLine();
		 * System.out.println(str);}
		 * catch(NullPointerException ex){System.out.println(ex);}
		 * ;
		String str=sc.nextLine();*/
		
		
		
		
		
	
		
		
		System.out.println(sum.Add(al));
	}

}
