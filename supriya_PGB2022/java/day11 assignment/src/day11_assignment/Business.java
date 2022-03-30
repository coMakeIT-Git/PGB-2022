package day11_assignment;
import java.util.*;
abstract class TestBusiness {
//abstract methods
	abstract  void  builditem();
	abstract  void  deployitem();
	// concrete method
	void  transactions()  {
	System.out.println("Business transactions");
	}
	}
class  Sales  extends TestBusiness {
void  builditem()  {
System.out.println("Product building stage.");
}
void  deployitem()  {
System.out.println("Product deploying stage.");
}
}

//Interface
interface Owner{
	public void dealings();
		
}
class Assistant  implements Owner {
public  void  dealings()  {
System.out.println("Business owner does the dealings");
}
}
//Inheritance
class Marketing{
	 public	int numofitemssold=5;	

	public void pname() {
		System.out.println("Product name");
	}
	public  void  price() {
		System.out.println("Products sold");
	}
}
class  Customers  extends Marketing {
	String productName =  "Mobile";
}
//Encapsulation
class Finance{
	private String pname;
	private int purchases;
	// Getter methods
	public String getName()  {
	return pname;
	}
	public  int  getPurchases()  {
		return purchases;
		}
	// Setter methods
	public  void  setName(String pname)  {
	this.pname  = pname;
	}
	public  void  setPurchases(int purchases)  {
	this.purchases  = purchases;
	}
	}
//Polymorphism
class Management {
	public void manage() {
		System.out.println("Product management");
	}
	public void manage(String name,int budget) {
		System.out.println("Product "+ name + "budget is:"+ budget);
	}
   
}
public class  Business  {
public  static  void  main(String[] args)  {
TestBusiness b =  new Sales();
Customers c=new Customers();
Finance f=new Finance();
b.transactions();
b.builditem();
b.deployitem();
c.pname();
c.price();
System.out.println("Product"+c.productName+"is of Rs 20000 cost");
f.setName("Smartphone");
f.setPurchases(500);
System.out.println("Product Name: "  + f.getName());
System.out.println("Number of purchases: "  + f.getPurchases());
Management m=new Management();
m.manage("ABC",30000);
Assistant a=new Assistant();
a.dealings();
//User u=new User();
//u.setProductName("JGJ");
//Client c1=new Client();
//c1.setProductdetails("Requirements");
//Client c2=new Client();
//c2.setProductdetails("Tools");
//List<Client> productList = new ArrayList<Client>();
//productList.add(c1);
//productList.add(c2);
//u.setClient(productList);
//System.out.println(u.getClients()+" are the product details for the product "+
 //       u.getproductName());
Client clnt = new Client("Software", 3);
User u1 = new User("Product1", 20000, clnt);
System.out.println("Product Name: "+u1.productName);
System.out.println("Product Price: "+u1.price);
System.out.println("------------Client Details----------");
System.out.println("Product Details: "+u1.clnt.productdetails);
System.out.println("Project Deadline: "+u1.clnt.deadline+"months");

}
}


class Client{
	 String productdetails;
	int deadline;
	Client(String productdetails, int deadline)
	  {
	    this.productdetails = productdetails;
	    this.deadline = deadline;
	    
	  }
	public String getProductdetails() {
		return productdetails;
	}
	public String setProductdetails(String productdetails ) {
		return this.productdetails=productdetails;
	}
	@Override
    public String toString() {
        return productdetails;
    }
}
class User{
 String productName;
	int price;
	 Client  clnt;
	  User(String n, int p, Client  clnt)
	  {
	    this.productName = n;
	    this.price = p;
	    this.clnt = clnt;
	  }
    List<Client> client;
  
    public String getproductName() {
        return productName;
    }
  
    public void setProductName(String productName) {
        this.productName = productName;
    }
    public List<Client> getClients() {
        return client;
    }
    public void setClient(List<Client> clients) {
        this.client = clients;
    }
     
}
 	





