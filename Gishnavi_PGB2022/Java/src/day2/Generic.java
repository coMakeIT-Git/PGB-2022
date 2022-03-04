package day2;


class GenericClass<I>
{
    

	GenericClass()
    {
        System.out.println("Generic Class is Initialized");
    }

    public void methodgeneric(I obj)
    {
        System.out.println("Object Type "+obj.getClass().getSimpleName()+"\nObject Value : "+obj);
    }
}
public class Generic {
    public static void main(String[] args) {
        
        GenericClass<Integer> test=new GenericClass<>();
        Integer a=5;
        test.methodgeneric(a);
        
        GenericClass<String> teststring = new GenericClass<>();
        String s="Generic object with String";
        teststring.methodgeneric(s);
    }    
}