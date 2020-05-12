import java.io.Console;

class pr4{
	public static void main(String args[]){
		Console c=System.console();
		String str=c.readLine("Enter string:\n");
		System.out.println(str);
		for(int i=0;i<str.length();i++){
			System.out.println(str.charAt(i));
		}
	}
}