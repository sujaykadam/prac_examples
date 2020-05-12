import java.io.Console;
import java.util.Arrays;

class pr1{
	public static void main(String args[]){
		Console c=System.console();

		int n = Integer.parseInt(c.readLine("Enter number of sutdents: "));
		int marks [];
		marks = new int[n];

		for(int i=0;i<n;i++)
 			marks[i]= Integer.parseInt(c.readLine("Enter marks:"));

 		Arrays.sort(marks);
 		int low=marks[0];
 		int high=marks[n-1];

 		System.out.println("Lowest: "+low+" Highest: "+high);
	}
}