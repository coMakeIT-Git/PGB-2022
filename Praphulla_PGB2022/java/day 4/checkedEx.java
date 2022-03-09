public class checkedEx{
 
    public static void main(String args[])
    {
        try {
 
            Class.forName("Praphulla");
        }
        catch (ClassNotFoundException ex)
         {
            ex.printStackTrace();
            System.out.println(ex.getMessage());  
        }
    }
}
