//read string using stringbuffer and print

import java.io.Console;

class pr1{
	public static void main(String args[]){
		Console c = System.console();
		String s =c.readLine("Enter a string: ");
		StringBuffer sb = new StringBuffer(s);
		
		System.out.println(sb);
		for(int i=0;i<s.length();i++)
			System.out.print(sb.charAt(i));
		System.out.println();

	}
}