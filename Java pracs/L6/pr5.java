import java.io.Console;

class pr5{
	public static void main(String args[]){
		Console c=System.console();
		String str=c.readLine("Enter string:\n");
		int lc=0,uc=0,dc=0,oc=0;
		for(int i=0;i<str.length();i++){
			char a=str.charAt(i);
			if(Character.isUpperCase(a))
				uc++;
			else if(Character.isLowerCase(a))
				lc++;
			else if(Character.isDigit(a))
				dc++;
			else
				oc++;
		}
		System.out.println("upper "+uc+" lower "+lc+" digit "+dc+" others "+oc);
	}
}
