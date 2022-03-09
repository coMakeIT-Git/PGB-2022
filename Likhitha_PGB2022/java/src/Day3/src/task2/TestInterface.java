package task2;
interface Gross{
	void gross_sal();
	void display();
}

 class Salary implements Gross{
	public void gross_sal()
	{
		System.out.println("This is gross salary of employee");
	}
	public void display()
	{
		System.out.println("This is employee salary details");
	}
}
 class TestInterface {
 public static void main(String[] args)
 {
	 Salary s= new Salary();
	 s.gross_sal();
	 s.display();
 }
}
