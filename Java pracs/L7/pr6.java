//add csv 
import java.util.*;
import java.io.Console;

class pr6{
	public static void main(String args[]){
		Console c = System.console();
		String s =c.readLine("Enter a string: ");
		Scanner scan=new Scanner(s);
		scan.useDelimiter(",");
		int sum=0;

		while(scan.hasNext())
			sum=sum+scan.nextInt();
		System.out.println("Sum: "+sum);
	}
}