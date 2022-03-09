package Task3_genricclass;

public class display <G>{
	private G g;
	public void add(G t)
    {
        this.g = t;
    }
  
    public void get() { System.out.println(g); }
    public static void main(String args[])
    {
    	display<Integer> i=new display<Integer>();
    	display<String> s=new display<String>();
    	i.add(1000);
    	s.add("generic class");
    	i.get();
    	s.get();
    	
    }
  

}
