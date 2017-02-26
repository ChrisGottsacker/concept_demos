import java.io.File;
import java.util.Scanner;

/**
 * Opens a file and scans
 */
public class open_and_scan_file{
	/**
	 * @param String[] args Path to text file
	 */
	public static void main(String[] args){
		if(args.length != 1){
			System.err.println("Usage: ...");
			System.exit(1);
		}

		Scanner sc = null;
		try{
			sc = new Scanner(new File(args[0]));
		}
		catch(Exception e){
			e.printStackTrace();
			System.exit(1);
		}


		System.out.println(args[0]);
	}
}
