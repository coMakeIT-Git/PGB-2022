package comakeit;

public class Genclass<T> {
	T value;

	public T getValue() {
		return value;
	}

	public void setValue(T value) {
		this.value = value;
	}
	
	public static void main(String[] args) {
		Genclass<Integer> g1= new Genclass<Integer>();
		Genclass<String> g2= new Genclass<String>();
		g1.setValue(22);
		g2.setValue("sai");
		System.out.println(g1.getValue());
		System.out.println(g2.getValue());
	}

}
