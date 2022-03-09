package day2.util;
class factorial_funs{
	int recursive(int n){
		if(n==1){
			return 1;
		}
		return recursive(n-1)*n;
	}
	int nonRecursive(int n){
		int ans=1;
		for(int i=2;i<=n;i++){
			ans*=i;
		}
		return ans;
	}
}
public class Factorial{
	public static void main(String[]args) {
		factorial_funs a=new factorial_funs();
		System.out.println("recursive "+a.recursive(9));
		System.out.println("non-recursive "+a.nonRecursive(10));
	}
}