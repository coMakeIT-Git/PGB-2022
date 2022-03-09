package Day3.Task1;
import Day3.Task1.Drawable;
public  class Rectangle implements Drawable{
	public void draw()
	{
		System.out.println("Rectangle is Drawing");
	}
	public void play()
	{
		System.out.println("In Rectangle Class Play Method is called");
	}
	public static void main(String args[])
	{
		Rectangle r=new Rectangle();
		r.draw();
		r.play();
	}
}
