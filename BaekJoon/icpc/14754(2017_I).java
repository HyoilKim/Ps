import java.util.Scanner;
import java.util.*;

public class Java {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n1 = scanner.nextInt();
		int n2 = scanner.nextInt();
		
		int[][] arr = new int[n1][n2];
		int[][] res = new int[n1][n2];
		for(int i = 0; i < n1; i++) {
			for(int j = 0; j < n2; j++) {
				arr[i][j] = scanner.nextInt();
				res[i][j] = arr[i][j];
			}
		}
		
		
		for(int i = 0; i < n1; i++) {
			int side_max = -1;
			int side_idx = -1;
			for(int j = 0 ; j < n2; j++) {
				// side 에서 봤을 때 max
				if(side_max < arr[i][j]) {
					side_max = arr[i][j];
					side_idx = j;
				}
				
			}
			res[i][side_idx] = 0;
		}
		
		for(int i = 0; i < n2; i++) {
			int front_max = -1;
			int front_idx = -1;
			for(int j = 0 ; j < n1; j++) {
				
				if(front_max < arr[j][i]) {
					front_max = arr[j][i];
					front_idx = j;
				}
			}
			res[front_idx][i] = 0;
		}
		
		long sum = 0;
		for(int i = 0; i < n1; i++) {
			for(int j = 0; j < n2; j++) {
				sum += res[i][j];
			}
		}
		System.out.println(sum);
		
	}
	
}
