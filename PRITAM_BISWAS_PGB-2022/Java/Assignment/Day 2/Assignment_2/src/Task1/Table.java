package Task1;
  
public class Table {
	String tmaterial;
	int tid,tprice;
	
	//Default constructor
	Table()
	{
		
	}
	// parameterized constructor
	Table(String material,int price,int id)
	{
		this.tmaterial =material;
		this.tprice=price;
		this.tid=id;
					
	}
	//getter & setter method
	public int getTid() {
		return tid;
	}

	public void setTid(int tid) {
		this.tid = tid;
	}
	
    public String getTmaterial() {
		return tmaterial;
	}

	public void setTmaterial(String tmaterial) {
		this.tmaterial = tmaterial;
	}

	public int getTprice() {
		return tprice;
	}

	public void setTprice(int tprice) {
		this.tprice = tprice;
	}
    // hash code
	@Override
	public int hashCode() {
		return tid+tmaterial.hashCode();
	}
	// equals override
	@Override
	public boolean equals(Object o)
	{
		Table t=(Table)o;
		if(this.tid==t.tid && this.tmaterial==t.tmaterial)
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	//Method Overloading
	void data(int id)
	{
		System.out.println("Table id :"+id);
	}
	void data(int id,String material)
	{
		System.out.println("Table id :"+id +"\t"+"Material:"+material);
	}
public static void main(String args[])
{
	Table t1=new Table("ABC",101,1000);
	Table t2=new Table("EFG",102,1200);
	Table t3=new Table("ABC",103,1500);
	Table t=new Table();
	
	//equals check
	System.out.println(t1.equals(t2));
	System.out.println(t1.equals(t3));
	
	//Method overloading
	t.data(101);
	t.data(103,"Wood");
	
}
}