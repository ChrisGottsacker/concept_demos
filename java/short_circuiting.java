public class short_circuiting{
	public static void main(String[] args){
		x = a;

		boolean bool;
		// print() not called due to optimization
		bool = false && print(true, "short-circuiting, print() not called");
		// print() called b/c && is left-associative so the function's
		// return value needs to be found first
		bool = print(true, "no short-circuiting, print() called") && false;

		bool = print(false, "no short-circuiting, print() called") && print(true, "short-circuiting, print() not called");
		bool = print(true, "no short-circuiting, print() called") && print(true, "no short-circuiting, print() called");
	}

	public static boolean print(boolean ret, String msg){
		System.out.println(msg);
		return ret;
	}
}
