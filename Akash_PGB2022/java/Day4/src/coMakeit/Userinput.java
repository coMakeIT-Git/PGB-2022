package coMakeit;

import java.util.*;

class Input extends Exception {
	Input(){ 
		super();
	}
}

interface func 
{
	public int avg(int x,int y);
}

public class Userinput {
	public static void validateSum(int sum)throws Exception{
		if(sum>3120) {
			throw new Input();
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
		func  a = (int x,int y)->(x+y)/2;
		System.out.println(a.avg(15,5));
		
		System.out.println("\nFunctional Interface RUNNABLE using lambda expression");
		new Thread(()->{System.out.println("Thread running");}).start();
		
		
	}


}
