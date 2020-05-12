import java.io.Console;
 class ArrayTest{
 	public static void main(String args[]){
 		Console c = System.console();
 		int marks [];
 		int n = Integer.parseInt(c.readLine("Enter number of students:"));
 		marks = new int[n];

 		for(int i=0;i<n;i++)
 			marks[i]= Integer.parseInt(c.readLine("Enter marks:"));

 		int top=0, fail=0;
 		double sum=0.0;
 		for(int k:marks)
 			sum=sum+k;
 			
 		for(int i=0;i<n;i++){
 			if (marks[i]>70)
 				top+=1;
 			else if (marks[i]<40)
 				fail+=1;
 		}
 		double avg=0.0;
 		avg=sum/n;
 		System.out.printf("Avg=%.2f, above 70=%d, below 40=%d",avg,top,fail);
 	}
 }