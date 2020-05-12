import java.io.Console;

class pr7{
	public static void main(String args[]){
		Console c=System.console();
		String str=c.readLine("Enter string:\n");
		String nstr="";
		for(int i=str.length()-1;i>=0;i--){
			nstr=nstr+str.charAt(i);
		}
		if(str.equals(nstr)){
			System.out.println("Palindrome");
		}
		else{
			System.out.println("Not palindrome");
		}
	}
}
