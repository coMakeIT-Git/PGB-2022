package task3;

public interface functional_interface {
	void abstract_function(int x);
    default void fun()
    {
       System.out.println("Hello Employee");
    }
}
