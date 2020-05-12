//read string using stringbuffer and count vowels and consonents

import java.io.Console;

class pr2{
	public static void main(String args[]){
		Console c = System.console();
		String s =c.readLine("Enter a string: ");
		StringBuffer sb = new StringBuffer(s);
		
		int vc=0,cc=0;

		for(int i=0;i<s.length();i++){
			char ch=sb.charAt(i);
			if (Character.isLetter(ch)){
				switch(ch){
					case 'a','e','i','o','u','A','E','I','O','U' -> vc++;
					default -> cc++;
				}
			}
		}
		System.out.println("Vowels: "+vc+"\nConsonents: "+cc);
	}
}