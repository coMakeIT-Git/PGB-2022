public class UncheckedException{
    public static void main(String[] args) {
	    try {
	        int[] dataArray = null;         
	        System.out.println("Array Length:" + dataArray.length);
	    }
	    catch(NullPointerException e) {
	    	System.out.println("Error: Array is empty. Cannot print length!");
	    }
    }
}
