//add csv 

import java.io.Console;

class pr5{
	public static void main(String args[]){
		Console c = System.console();
		String s =c.readLine("Enter a string: ");
		String data[]=s.split(",");
		int sum=0;

		for (String d:data)
			sum=sum+Integer.parseInt(d);
		System.out.println("Sum: "+sum);
	}
}