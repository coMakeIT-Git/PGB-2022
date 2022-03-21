package task1;

class peninfoclass{
	String penmodel;
	String pentype;
	int penprice;

	public peninfoclass(String penmodel,String pentype,int penprice)
	{
		this.penmodel=penmodel;
		this.pentype=pentype;
		this.penprice=penprice;


	}
}


public class aggregation {

	int store_no;
	String store_name;

	peninfoclass info;

	public aggregation(String store_name, int store_no, peninfoclass info) {
		// TODO Auto-generated constructor stub

		this.store_name = store_name;
		this.store_no = store_no;
		this.info=info;
	}

	public int getstore_no() {
		return store_no;
	}


	public String getstore_name() {
		return store_name;
	}



	void display()
	{
		System.out.println("store Name: "+getstore_name()+"store Number: "+store_no);
		System.out.println("model: "+info.penmodel+" type: "+info.pentype+" price :"+info.penprice);
	}




	public static void main (String[] args)
	{
	    peninfoclass Addressobj=new peninfoclass("cello","ballpoint",100);
		aggregation obj = new aggregation("Abc ",1234,Addressobj);
		obj.display();
	}

}