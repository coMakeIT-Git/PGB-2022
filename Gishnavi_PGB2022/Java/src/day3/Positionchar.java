package day3;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Positionchar {

	public static String char_Count(String s) {
			Map<Character, List<Integer>> dict = new HashMap<>();
			s = s.replaceAll(" ", "");
			for (int i = 0; i < s.length(); i++) {
				char id =  s.charAt(i);
			    if (dict.containsKey(id)) {
			        dict.get(id).add(i);
			    } else {
			        dict.put(id, new ArrayList<Integer>());
			        dict.get(id).add(i);
			    }
		        // System.out.print(s.charAt(i) + " ");
		    }
			return dict.toString();
		}

    public static void main(String[] args) throws IOException {
    	BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
    	System.out.print("Enter String : ");
        String input = bfr.readLine();
        System.out.print(char_Count(input));

    }

}