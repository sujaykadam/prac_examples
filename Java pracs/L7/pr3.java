//read string using stringbuffer and remove vowels

import java.io.Console;

class pr3{
	public static void main(String args[]){
		Console c = System.console();
		String s =c.readLine("Enter a string: ");
		StringBuffer sb = new StringBuffer(s);

		for(int i=0;i<s.length();i++){
			char ch=sb.charAt(i);
			if (Character.isLetter(ch)){
				switch(ch){
					case 'a','e','i','o','u','A','E','I','O','U' -> sb.replace(i,i+1,"");
				}
			}
		}
		System.out.println(sb);
	}
}