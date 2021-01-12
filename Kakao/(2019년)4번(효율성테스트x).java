package ps;
import java.util.*;

public class Test {
	public static void main(String[] args) {
		String[] words = {"frodo", "front", "frost", "frozen", "frame", "kakao"};
		String[] queries = {"fro??", "????o", "fr???", "fro???", "pro?"};
		int[] res = new int[queries.length];
		
		int k = 0;
		for(int i = 0; i < queries.length; i++) {
			int cnt = 0;
			for(int j = 0; j < words.length; j++) {
				if(isSame(words[j], queries[i]))
					cnt++;
			}
			res[k++] = cnt;
			System.out.print(cnt + " ");
		}
		
	}
	
	public static boolean isSame(String word, String query) {
		if(word.length() != query.length()) return false;
		for(int i = 0; i < word.length(); i++) {
			if(word.charAt(i) != query.charAt(i) && query.charAt(i) != '?') 
				return false;
		}
		return true;
	}

	
}
