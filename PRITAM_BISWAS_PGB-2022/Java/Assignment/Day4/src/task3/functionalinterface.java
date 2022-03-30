package task3;

public interface functionalinterface {
	void abstractfunction(int x);
    default void fun()
    {
       System.out.println("Hello Employee");
    }
}