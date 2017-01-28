/*
 * Demonstrates that HashMap hashes intelligently and does not
 * create duplicate entries
 */


import java.util.*;
public class HashMap_of_Character{
	public static void main(String[] args){
		HashMap<Character, String> h = new HashMap<Character, String>();
		h.put(new Character('k'), "first value");
		h.put(new Character('k'), "second value");
		System.out.println(h.entrySet());	// [k=second value]
	}
}
