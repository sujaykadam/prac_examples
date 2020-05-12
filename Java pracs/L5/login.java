import java.io.*;
class login{
	public static void main(String args[])throws IOException{
		String u1="";
		String p1="";

		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);

		System.out.println("Enter username:");
		u1=br.readLine();
		System.out.println("Enter password: ");
		p1=br.readLine();

		if(u1.equals("kamal") && p1.equals("classes")){
			System.out.println("\nSuccess");
		}
		else{
			System.out.println("\nFailed");
		}
	}
}