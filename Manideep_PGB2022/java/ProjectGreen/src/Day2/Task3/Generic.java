package Day2.Task3;

public class Generic <G>{
	private G g;
	public void add(G t)
    {
        this.g = t;
    }
  
    public void get() { System.out.println(g); }
    public static void main(String args[])
    {
    	Generic<Integer> i=new Generic<Integer>();
    	Generic<String> s=new Generic<String>();
    	i.add(1);
    	s.add("String");
    	i.get();
    	s.get();
    	
    }
  

}
