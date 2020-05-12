//string buffer palindrome

import java.io.Console;

class pr4{
	public static void main(String args[]){
		Console c = System.console();
		String s =c.readLine("Enter a string: ");
		StringBuffer sb = new StringBuffer(s);
		StringBuffer nsb= new StringBuffer(sb.reverse());

		if (s.equals(nsb.toString()))
			System.out.println("Palindrome");
		else
			System.out.println("Not palindrome");
	}
}