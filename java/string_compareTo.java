public class string_compareTo {
	public static void main(String[] args) {
		System.out.println("".compareTo("a"));	// outputs -1, so "" precedes "a"
		System.out.println("~".compareTo("a"));	// outputs 29, so "~" follows "a"
	}
}
