package saikeerthana;
import java.util.*;
interface drawable{
	void inpdetails(); 
	 void display();
}
 abstract class Geometric implements drawable {
	public abstract void inpdetails();
	public abstract void display();
	Scanner s=new Scanner(System.in);
}
class Circle extends Geometric{
	int radius;
	String color;
	@Override
	public void inpdetails() {
		System.out.println("Enter radius of circle:");
		radius=s.nextInt();
	}
	@Override
	public void display() {
		System.out.println("AREA OF CIRCLE IS:"+radius*radius*Math.PI);
	}
	//Encapsulation
	public String getcolor()
	{
		return color;
	}
	public void setcolor(String color) {
		this.color=color;
	}
	
}
class Square extends Geometric{
	int side;
	String color;
	@Override
	public void inpdetails() {
		System.out.println("Enter side of square");
		side=s.nextInt();
		
	}
	@Override
	public void display() {
		System.out.println("Area of CIRCLE IS:"+side*side);
		
	}

}
//Polygon overriding show method of square class
class Box
{
	public void show()
	{
		System.out.println("THis is box class");
	}
}
class Hexagon extends Box
{
	public void show()
	{
		System.out.println("THis is Hexagon class");
	}
}
class Details {
    private String shape_name;
    private int edges;
    
    List<Examples> ex=new ArrayList<Examples>();
 
    public String getName() {
       return shape_name;
    }
 
    public int getIdNum() {
       return edges;
    }
    public void setexamples(List<Examples> l1)
    {
        this.ex=l1;
    }
    public List<Examples> getexamples()
    {
        return this.ex;
    }
      
    public void setName(String newName) {
       shape_name = newName;
    }
 
    public void setIdNum( int newId) {
       edges = newId;
    }
 }
 class Examples{
     private String application_name;
     public String getapp_name(){
         return application_name;
     }
     public void set_appname(String newName) {
        application_name = newName;
     }
 }
//Association
class Shape
{
	String sname;
	  
    Shape(String sname)
    {
        this.sname = sname;
    }
 
    // Method of Result class
    public String getsname()
    {
        // returning the no.of sides 
        return this.sname;
    }
}
class Result {
    // Attributes of Result
    int  sides;
  
    Result(int sides)
    {
        this.sides = sides;
    }
 
    // Method of Result class
    public int getsides()
    {
        // returning the no.of sides 
        return this.sides;
    }
}
//Composition
class Dimension
{
	public void print()
	{
		System.out.println("Dimensions of a figure must exist");
	}
}
final class Triangle
{
	private  Dimension dim; 
	Triangle(Dimension dim)
	{
		this.dim=dim;
	}
	public void exist()
	{
		dim.print();
		System.out.println("Triangle has 2 dimensions");
	}
	
}


public class Sampleprg{
	public static void main(String[] args)
	{
		Circle c=new Circle();
		c.inpdetails();
		c.display();
		c.setcolor("blue");
		System.out.println("Color of circle is"+c.getcolor());
		Square s=new Square();
		s.inpdetails();
		s.display();
		Box b=new Box();//polymorphic variables
		b.show();
		b=new Hexagon();
		b.show();
		Shape sh=new Shape("Circle");
		Result rs=new Result(10);
		System.out.println(sh.getsname() + "has" + rs.getsides() + "sides");
		Dimension dim=new Dimension();
		Triangle tr=new Triangle(dim);
		tr.exist();
		 Details d=new Details();
	        d.setName("Square");
	        d.setIdNum(4);
	        Examples de1=new Examples();
	        de1.set_appname("chess board");
	        Examples de2=new Examples();
	        de2.set_appname("tiles on floor");
	        List<Examples> l=new ArrayList<Examples>();
	        l.add(de1);
	        l.add(de2);
	        d.setexamples(l);
	        List<Examples> l2=new ArrayList<Examples>();
	        l2=d.getexamples();
	        
	        System.out.println( d.getName() + "has " +   d.getIdNum() +  " edges " + " used as" + de1.getapp_name() + "and" + de2.getapp_name());
	}
}
 
