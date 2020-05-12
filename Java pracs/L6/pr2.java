// 1= appens, 2=view, 3=delete, 4=exit
import java.io.Console;

class pr2{

	public static void main(String args[]){
		Console c = System.console();
		int[] data = new int[0];

		while (true) {
			int op=Integer.parseInt(c.readLine("1.Add\n2.View\n3.Delete\n4.Exit\n"));
			if (op==1){
				int cs = data.length;
				int ndata[]=new int[cs+1];
				System.arraycopy(data,0,ndata,0,cs);
				ndata[ndata.length-1]=Integer.parseInt(c.readLine("Enter element\n"));
				data=ndata;
			}

			else if (op==2){
				for (int i:data)
					System.out.print(i+" ");
				System.out.println();
			}

			else if (op==3){
				int delele=Integer.parseInt(c.readLine("Enter number to delete"));
				boolean flag=false;
				for (int j=0;j<data.length;j++){
					if (delele==data[j]){
						flag=true;
						break;
					}
				if(flag==true){
					int cs=data.length;
					int ndata[]=new int[cs-1];
					System.arraycopy(data,0,ndata,0,j);
					System.arraycopy(data,0,ndata,0,data.length-j-1);
					data=ndata;
				}
				else{
					System.out.println("Not Found");
				}	
			}
		}
			else if (op==4){
			break;
		}

		else{
			System.out.println("Invalid option");
		}
	}
}
}