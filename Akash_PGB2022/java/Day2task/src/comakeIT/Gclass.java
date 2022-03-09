package comakeIT;

public class Gclass<o> {
	o value;

	public o getValue() {
		return value;
	}

	public void setValue(o value) {
		this.value = value;
	}
	
	public static void main(String[] args) {
		Gclass<Integer> g1= new Gclass<Integer>();
		Gclass<String> g2= new Gclass<String>();
		g1.setValue(21);
		g2.setValue("ganesh");
		System.out.println(g1.getValue());
		System.out.println(g2.getValue());
	}

}
