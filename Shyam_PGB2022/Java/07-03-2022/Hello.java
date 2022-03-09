 interface test{  
        int force(int mass,int acc);  
    }
public class Hello extends Exception
{
    public Hello(String s)
      {
        super(s);
      }
      
    static void a(int num){
    int data = 50/num;
    }

    static void b(){
    try{
    a(0);
    }
    catch(ArithmeticException ex){
    System.out.println("Runtime Exception Handled: Arithmetic Exception");
    }
    }
    static String extractInt(String str)
    {
        str = str.replaceAll("[^\\d]", " ");
        str = str.trim();
        str = str.replaceAll(" +", " ");
        if (str.equals(""))
            return "-1";
        return str;
    }
    public static void main(String args[])
      {
         if(args.length > 0)
           {
               try
                 {
                      String firstNum = args[0];
                      int x = Integer.parseInt(extractInt(firstNum));
                      String secNum = args[1];
                      int y = Integer.parseInt(extractInt(secNum));
                      int sum = x+y;            
                      System.out.println("First Number = "+x);
                      System.out.println("Second Number = "+y);
                      System.out.println("Addition Of Two Numbers = "+sum);
                      b();
                      throw new Hello("Custom Exception Handled: Don't take inputs more than '2'  "); 
              
                  }
               catch(NumberFormatException e)
                 {
                     System.out.println("Number format Exception Handled: Argument/s must be the integer value");
                 }
               catch (Hello ex)  
        	 {	  
            		System.out.println(ex.getMessage());  
        	 } 
        	 catch(NullPointerException npe)
        	 {
        	  	System.out.println("Null Pointer Exception Handled: Please initialize a value ");
                 }
       
           }
           	test a1=(mass,acc)->(mass*acc);  
            	System.out.println("Lambda without datatypes: " +a1.force(10,20));  
            	test a2=(int mass,int acc)->(mass*acc);  
            	System.out.println("Lambda with datatypes: " +a2.force(100,200)); 
            	new Thread(()->System.out.println("Hey: Here the lambda for Runnable says hi")).start(); 
      }
}
