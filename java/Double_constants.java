class Double_constants{
	public static void main(String[] args){
		double inf = Double.NEGATIVE_INFINITY;
		double nan = Double.NaN;

		System.out.println(0>inf);
		System.out.println(Double.isNaN(nan));
		System.out.println(-2.1 + inf);
	}
}
