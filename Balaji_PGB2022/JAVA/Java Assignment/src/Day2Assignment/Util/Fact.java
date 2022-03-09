package Day2Assignment.Util;

public class Fact {
	
		public static int non_recursive(int num)
		{
			int fact=1;
			for(int i=1;i<=num;i++)
			{
				fact*=i;
			}
			return fact;
		}
		public static int recursive(int n)
		{
			if(n==1) return 1;
			else
				return(n*recursive(n-1));
		}
	}

