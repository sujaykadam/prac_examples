import java.io.*;
class loin1{
	public static void main(String args[])throws IOException{
		String u1="";
		char[] p1;

		Console c = System.console();
		u1= c.readLine("Enter username:\n");
		p1= c.readPassword("Enter password:\n");
		if(u1.equals("kamal") && (new String(p1)).equals("classes")){
			System.out.println("\nSuccess");
		}
		else{
			System.out.println("\nFailed");
		}
	}
}