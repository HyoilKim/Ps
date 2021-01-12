import java.util.Scanner;

public class Test {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String str = in.next();
		int[] arr = new int[26];
		
		for(int i = 0; i < 26; i++) arr[i] = -1;
		for(int i = 0; i < str.length(); i++) {
			if(arr[str.charAt(i) - 'a'] == -1) {
				arr[str.charAt(i) - 'a'] = i;
			}
		}
		for(int i = 0; i < 26; i++) System.out.print(arr[i] + " ");
	}
}