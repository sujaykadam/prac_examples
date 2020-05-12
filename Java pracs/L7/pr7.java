//print according to csv

import java.io.Console;

class pr7{
	public static void main(String args[]){
		Console c = System.console();
		String s =c.readLine("Enter a string: ");
		String data[]=s.split(",");
		System.out.println();
		for (int i=0;i<data.length;i+=2){
			int j;
			for(j=0;j<Integer.parseInt(data[i+1]);j++)
				System.out.print(data[i]+"\t");
			System.out.println();
		}
	}
}