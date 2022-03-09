public class GenericDemo<X> {
	private X y;
	public void add(X y)
	{
		this.y = y;
	}
	public X get() { 
		return y; }

	public void getArea() {}

	public static void main(String[] args)
	{
		GenericDemo<Integer> factorial = new GenericDemo<Integer>();
		GenericDemo<Double> area = new GenericDemo<Double>();
		factorial.add(7);
		area.add(3.4);
		System.out.println(factorial.get());
		System.out.println(area.get());
	}
}
