import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int[] len = new int[N];
		Pair[] elec = new Pair[N];
		
		for(int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(in.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			elec[i] = new Pair(a, b);
			len[i] = 1;
		}
        
		Arrays.sort(elec);
		
		int maxLen = len[0];
		for(int i = 1; i < N; i++) {
			int max = -1;
			for(int j = 0; j < i; j++) {
				if(elec[j].y < elec[i].y) 
					if(len[j] > max)
						max = len[j];			
			}
			if(max != -1) len[i] += max;
			if(len[i] > maxLen) maxLen = len[i];
		}
		
		System.out.println(N - maxLen);
	}
}

class Pair implements Comparable<Pair>{
	int x;
	int y;
	
	public Pair(int x, int y) {
		this.x = x;
		this.y = y;
	}

	@Override
	public int compareTo(Pair o) {
		if(this.x > o.x) return 1;
		else if(this.x < o.x) return -1;
		else return 0;
	}	
}