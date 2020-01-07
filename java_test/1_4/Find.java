//package lec01;

public class Find {

	/**
	 * Find value in an array
	 * @param a array to search; requires that val occurs exactly once in a.
	 * @param val value to search for
	 * @return index i such that a[i] = val
	 */
	public static int findA (int[] a, int val) {
		for (int i = 0; i < a.length; ++i) {
			if (a[i] == val) {
				return i;
			}
		}
		return a.length;
	}
	
	/**
	 * Find value in an array
	 * @param a a array to search.
	 * @param val value to search for.
	 * @return returns largest result such that a[result] = val or -1 if no such result.
	 */
	public static int findB (int[] a, int val) {
		for (int i = 0; i < a.length; ++i) {
			if (a[i] == val) {
				return i;
			}
		}
		return -1;
	}
	
	/**
	 * 
	 * @param a a array to search.
	 * @param val value to search for.
	 * @return returns largest result such that a[result] = val
	 * @throws ElemNotFoundException if val don't occurs in a.
	 */
	public static int findC (int[] a, int val) throws ElemNotFoundException {
		for (int i = a.length-1; i >= 0; --i) {
			if (a[i] == val) {
				return i;
			}
		}
		throw new ElemNotFoundException();
	}
	
	public static int findD(int[] a, int val){
		
		int i = 0;
//		try{
			while(true){
				if(a[i++] == val) 
					return --i;
			}		
//		}catch (ArrayIndexOutOfBoundsException e){
//			System.out.println("not found");
//			System.exit(-1);
//		}
//		return -1;
	}
	
	public static int findE(int[] a, int val) throws ArrayIndexOutOfBoundsException{
		
		int i = 0;
		while(true){
			if(a[i++] == val) 
				return --i;
		}
	}
	
	public static void main(String[] args) {
		
		int[] a = {1, 2, 3};//{1, 1, 1},{2, 3},{}
		int x = 4;
		
//		System.out.println(findA(a, x));
//		System.out.println(findB(a, x));
/*		
		try{
			System.out.println(findC(a, x));
		}catch(ElemNotFoundException e){
			System.out.println(e.getMessage1());
		}
*/		
		System.out.println(findD(a, x));
		
		System.out.println(findE(a, x));
	}

}
