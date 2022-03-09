package comakeit;

import java.util.*;

class MyExcep extends Exception {
	MyExcep(){ 
		super();
	}
}

interface function 
{
	public int avg(int x,int y);
}

public class Input {
	public static void validateSum(int sum)throws Exception{
		if(sum>2540) {
			throw new MyExcep();
		}
	}
	
	public static void main(String[] args) {
		try {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter space seperated integers: ");
		String str = sc.nextLine();
		String[] arr = str.split(" ");
		int sum = 0;
		for(int i=0;i<arr.length;i++) {
			sum += Integer.parseInt(arr[i]);
		}
		validateSum(sum);
		System.out.println("Sum of given numbers: "+sum);
		
		}catch(Exception e) {
			e.printStackTrace();
		}
		
		System.out.println("\nCustom Functional Interface");
		function a = (int x,int y)->(x+y)/2;
		System.out.println(a.avg(15,5));
		
		System.out.println("\nFunctional Interface RUNNABLE using lambda expression");
		new Thread(()->{System.out.println("Thread running");}).start();
		
		
	}


}
