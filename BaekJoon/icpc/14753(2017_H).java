import java.util.Scanner;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		ArrayList<Integer> arr = new ArrayList<>();
		
		int n = scanner.nextInt();
		long res = 1;
		for(int i = 0; i < n; i++ ) {
			arr.add(scanner.nextInt());
		}
		Collections.sort(arr);
		
		// n1 < n2 ... < n6
		int n1 = arr.get(0);
		int n2 = arr.get(1);
		int n3 = arr.get(2);
		int n4 = arr.get(arr.size()-3);
		int n5 = arr.get(arr.size()-2);
		int n6 = arr.get(arr.size()-1);
		
		System.out.println(Math.max(n4*n5*n6, Math.max(n5*n6, Math.max(n1*n2*n3, Math.max(n6*n1*n2, n1*n2)))));
		// 경우의 수
		// n1,n2,n3 - n1,n2 - n4,n5,n6 - n1,n5,n6 - n5,n6
	}
	
}
