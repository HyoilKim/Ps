import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int[] arr = new int[N];
		int[] len = new int[N];
		
 		for(int i = 0; i < N; i++) {
 			arr[i] = Integer.parseInt(in.readLine());
 			len[i] = 1;
 		}
		
        //Lis
 		int maxLen = len[0];
		for(int i = 1; i < N; i++) {
			int max = -1;
			for(int j = 0; j < i; j++) {
				if(arr[j] < arr[i]) {
					if(len[j] > max)
						max = len[j];
				}
			}
			if(max != -1) len[i] += max;
			if(maxLen <= len[i]) {
				maxLen = len[i];
			}	
		}
		
        //Lis의 최대값은 정렬되어 있기 때문에 제외하고 옮기기
		System.out.println(N - maxLen);	
	}
}
