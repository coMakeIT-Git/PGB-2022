package day2;
class Generic<A, B>
{
	A obj1; 
	B obj2; 

	// constructor
    Generic(A obj1, B obj2)
	{
		this.obj1 = obj1;
		this.obj2 = obj2;
	}

		public void print()
	{
		System.out.println(obj1);
		System.out.println(obj2);
	}	
		
		public static void main (String[] args)
	{
		Generic <Integer, String> obj = new Generic<Integer, String>(23,"Generic");

		obj.print();
	}
}


