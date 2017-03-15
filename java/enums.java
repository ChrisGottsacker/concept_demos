import java.util.*;

class enums{
	enum Flavor {
		CHOCOLATE, CHAI, COFFEE
	}
	public static void main(String[] args){
		Flavor milkshake = Flavor.CHOCOLATE;
		if(milkshake == Flavor.CHOCOLATE){
			System.out.println("Enum comparison successful");
		}
	}

}
