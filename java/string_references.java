public class string_references{
	public static void main(String[] args){
		String a = new String("");
		String b = new String("");
		String c= "";
		String d= "";
		System.out.println(a==b);	// false
		System.out.println(a==c);	// false
		System.out.println(c==d);	// true
	}
}
