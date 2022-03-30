package task1;
class peninfo{  
	//method overloading
static int info(int no_pen,int price)
{
	return no_pen*price;
	}  
static int info(int no_pen,int price,int tax)
{
	return no_pen*price*tax;
	}  
//method overriding
void info()
{
	System.out.println("pen1");
	}
}  

class polymorphism extends peninfo{  
	void info()
	{
		System.out.println("pen2");
		}  
public static void main(String[] args){ 
	polymorphism p=new polymorphism();
	p.info();
System.out.println(peninfo.info(10,20));  
System.out.println(peninfo.info(10,20,5));  
}} 

