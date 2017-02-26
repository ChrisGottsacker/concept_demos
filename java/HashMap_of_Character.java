/*
 * Demonstrates that HashMap hashes intelligently and does not
 * create duplicate entries
 */


import java.util.*;
public class HashMap_of_Character{
	public static void main(String[] args){
		HashMap<Character, String> h = new HashMap<Character, String>();
		Character j = new Character('j');
		Character k1 = new Character('k');
		Character k2 = new Character('k');
		h.put(j, "j");
		h.put(k1, "k1");
		h.put(k2, "k2");
		System.out.println(k1 == k2);		// false
		System.out.println(h.entrySet());	// [j=j, k=k2]
	}
}
