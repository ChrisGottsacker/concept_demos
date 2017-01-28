class return_void{
	public static void main(String[] args){
		// raises compiler error even though it is still a void return type
		return func();
	}

	static void func(){}
}
