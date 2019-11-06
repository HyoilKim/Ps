import java.util.*;
import java.io.*;

public class Test{
	static List<Integer> res = new ArrayList<>();
	public static void main(String[] args) throws Exception{
		//hit가 있으면 ?it h?t hi?를 찾는다
		//dfs로 찾아서 계속 찾다가 
		//count가 words길이보다 커지면 종료
		String begin = "hit";
		String target = "cog";
		String[] words = {"hot","dot","dog","lot","log","cog"};
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		boolean[] visit = new boolean[words.length];
		
		wordChange(words, begin, target, visit, 0);
		Collections.sort(res);
		if(res.size() == 0) {
			System.out.println(0);
		}else {
			System.out.println(res.get(0));
		}
	}
	
	public static void wordChange(String[] words, String word, String target, boolean[] visit, int cnt) {
		if(word.equals(target)) {
			res.add(cnt);
			return;
		}
		
		for (int i = 0; i < word.length(); i++) {
			StringBuilder tmp = new StringBuilder(word);
			tmp.setCharAt(i, '?');
			String anWord = tmp.toString();
			
			for (int j = 0; j < words.length; j++) {
				if (isEqual(anWord, words[j]) && !visit[j]) {
					System.out.println(anWord + " " + words[j] + " " + cnt);
					visit[j] = true;
					wordChange(words, words[j], target, visit, cnt+1);
					visit[j] = false;
				}
			}
		}
	}
	
	public static boolean isEqual(String a, String b) {
		if(a.length() != b.length()) return false;
		for(int i = 0; i < a.length(); i++) {
			if(a.charAt(i) != b.charAt(i)) {
				if(a.charAt(i) != '?' && b.charAt(i) != '?')
					return false;
			}	
		}
		return true;
	}
	
}
