package day4assignment;
import java.io.*;

public class checkedUncheckedExceptions {

	public static void main(String[] args) {
		System.out.println("Checked Exception");
		FileInputStream fis = null;
		try {
			fis = new FileInputStream("/Home/eclipse-workspace/file.txt");
		}
		catch(FileNotFoundException fnfe) {
			System.out.println("The specified file is not present at the given path.");
		}
		
		System.out.println();
		System.out.println("Unchecked Exception");
		int array[] = {1, 2, 3, 4, 5};
		System.out.println(array[7]);
	}
}
