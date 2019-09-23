import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] res = new int[commands.length];
		
		for(int i = 0, k = 0; i < commands.length; i++) {
			ArrayList<Integer> tmp = new ArrayList<>();
			int start = commands[i][0] - 1;
			int end = commands[i][1] - 1;
			int idx = commands[i][2] - 1;
			for(int j = start; j <= end; j++) {
				tmp.add(array[j]);
			}
			
			Collections.sort(tmp);
			res[k++] = tmp.get(idx);
		}
        return res;
    }
}