package day3_assignment;
import java.util.*;
import java.util.stream.Collectors;
public class CharPosition {
	
	    public static void main(String[] args) {
	    	Scanner sc = new Scanner(System.in);
	    	 System.out.println("Enter the string");
	    	 String str = sc.nextLine();
	    	 
	        indexOfChar(str);
	    }

	    @SuppressWarnings("empty-statement")
	    public static void indexOfChar(String string) {
	        int counter;
	        counter = 0;
	        String letter;
	        int[] letterCounter = new int[26];
	        letter = "abcdefghijklmnopqrstuvwxyz";

	        for (int i = 0; i < string.length(); i++) {
	            counter = 0;
	            letterCounter[letter.indexOf(string.charAt(i))]++;
	        }

	        counter = 0;
	        for (int i = 0; i < letterCounter.length; i++) {
	            if (letterCounter[i] != 0) {
	                counter++;
	            }
	        }
	        String s = null;

	        for (int i = 0; i < string.length(); i++) {
	            // char ch=name.charAt(i);
	            if (letterCounter[letter.indexOf(string.charAt(i))] != 0) {
	                System.out.print(string.charAt(i) + "=[");
	            }
	            for (int j = i; j < string.length(); j++) {
	                if (string.charAt(i) == string.charAt(j)) {
	                    System.out.print(j + ",");
	                }
	            }
	            System.out.println("]");
	        }
	       
	    }
	}


