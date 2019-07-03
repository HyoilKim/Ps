import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int[] alphCnt = new int[26];
		String str = in.next();
		str = str.toUpperCase();
		
		for(int i = 0; i < str.length(); i++) {
			int idx = str.charAt(i) - 'A';
			alphCnt[idx]++;
		}
		
		int max = alphCnt[0];
		int maxIdx = 0;
		boolean same = false;
		for(int i = 1; i < 26; i++) {
			if(alphCnt[i] != 0) {
				if(max < alphCnt[i]) {
					max = alphCnt[i];
					maxIdx = i;
					same = false;
				}else if(max == alphCnt[i]) {
					same = true;
				}
			}
		}
		
		if(same) {
			System.out.print('?');
		}else {
			System.out.print((char)('A' + maxIdx));
		}
	}
}

