class Employee{
	private static int count=0;
	private int eid;
	private String ename;
	private int esalary;

	public static void showCount(){
		System.out.println(Employee.count);
	}

	public Employee(int eid, String ename, int esalary){
		this.eid=eid;
		this.ename=ename;
		this.esalary=esalary;
		count++;
	}

	public void showData(){
		System.out.println("Employee ID: "+this.eid);
		System.out.println("Employee name: "+this.ename);
		System.out.println("Enployee salary: "+this.esalary);
		System.out.println();
	}
}

class EmployeeTest{
	public static void main(String args[]){	
		System.out.println();
		
		Employee e1=new Employee(1,"abc",15000);
		Employee e2=new Employee(2,"def",20000);
		Employee e3=new Employee(3,"ghi",25000);

		e1.showData();
		e2.showData();
		e3.showData();

		Employee.showCount();
	}
}