package Task2_factorial;

public class factorialcheck {
	int num;
	static int factrecursion(int num)
	{
		if(num==0)
			return 1;
		else
		    return num*factrecursion(num-1);
	}
	static int factnonrecursion(int num)
	{
		int i,fac=1;
		if(num==0)
			return 1;
		else
		{
			for(i=1;i<=num;i++)
			{
				fac=fac*i;
			}
			return fac;
		}
	}
	public static void main(String args[])
	{
		System.out.println(factorialcheck.factrecursion(8));
		System.out.println(factorialcheck.factnonrecursion(8));
	}

}
