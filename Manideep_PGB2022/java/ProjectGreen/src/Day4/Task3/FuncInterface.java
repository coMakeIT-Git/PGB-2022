package Day4.Task3;

public interface FuncInterface {
	void abstractFun(int x);
    default void normalFun()
    {
       System.out.println("Hello");
    }
}

