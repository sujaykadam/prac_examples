//read double numbe from commandline and find root
class p5{
	public static void main (String args[]){
		System.out.println("Welcome");
		try{
			double num= Double.parseDouble(args[0]);
			if (num<0)
				throw new Exception("No negetive number");
			double res = Math.sqrt(num);
			System.out.println("Res = "+res);
		}
		catch(ArrayIndexOutOfBoundsException e){
			System.out.println("Atleast one argument");
		}
		catch(NumberFormatException e){
			System.out.println("Only number");
		}
		catch(Exception e){
			System.out.println(e);
		}
		System.out.println("Bye");
	}
}