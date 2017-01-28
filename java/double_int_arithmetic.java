class double_int_arithmetic{
	public static void main(String[] args){
		int i = 1;
		double d = 2;
		System.out.println(i/d);	// 0.5

		d = i/2;	// integer arithmetic
		System.out.println(d);	// 0

		d = i/(double)2;		// double arithmetic
		System.out.println(d);	// 0.5
	}
}
