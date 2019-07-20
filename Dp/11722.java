import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int[] arr = new int[N];
		int[] len = new int[N];
		
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			len[i] = 1;
		}
		
		//�ڿ��� ���� �����ϴ� �� = �տ��� ���ʹ� �����ϴ� ��
		int maxLen = len[0];
		for(int i = N - 2; i >= 0; i--) {
			int max = -1;
			for(int j = i + 1; j <= N - 1; j++) {
				if(arr[j] < arr[i]) {
					if(len[j] > max)
						max = len[j];
				}
			}
			if(max != -1) len[i] += max;
			// maxLen ����
			if(maxLen < len[i]) {
				maxLen = len[i];
			}
		}
		System.out.println(maxLen);	
	}
}
