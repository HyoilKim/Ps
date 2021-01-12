import java.util.Scanner;

public class Main {
	static int[] arr;
	static int[] res;
	static int k;
	static int len;
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		
		while(true) {
			k = in.nextInt();	// k>6 or 0
			if( k == 0 ) return;
			len = 0;
			arr = new int[k];
			res = new int[6];
			
			for(int i = 0; i < k; i++) {
				arr[i] = in.nextInt(); // 1~49
			}
			dfs(0, len);
            System.out.println("");
		}
	}
	
	public static void dfs(int i, int len) {
		if( len == 6 ) {
			for(int j = 0; j < 6; j++) {
				System.out.print(res[j] + " ");
			}
			System.out.println("");
			len--;
			return;
		} else {
			for(int idx = i; idx < k; idx++) {
				res[len] = arr[idx];
				dfs(idx + 1, len + 1);			
			}
		}
	}
}
