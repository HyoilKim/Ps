package ps;
import java.util.*;

public class Test {
	public static void main(String[] args) {
		int[] answer = {1,2,3,4,5};
		int[] supoja1 = {1, 2, 3, 4, 5};
		int[] supoja2 = {2, 1, 2, 3, 2, 4, 2, 5};
		int[] supoja3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
		int[] score = new int[3];
		
		for(int i = 0; i < answer.length; i++) {
			int i1 = i % 5;
			int i2 = i % 8;
			int i3 = i % 10;
			if(supoja1[i1] == answer[i]) score[0]++;
			if(supoja2[i2] == answer[i]) score[1]++;
			if(supoja3[i3] == answer[i]) score[2]++;
		}

		int max = Math.max(score[0], Math.max(score[1], score[2]));
		int resLen = 0;
		for(int i = 0; i < 3; i++)
			if(max == score[i])
				resLen++;
        
        int[] res = new int[resLen];
		for(int i = 0, j = 0; i < 3; i++) {
			if(max == score[i]) {
                res[j++] = i+1;
			}
		}
	}
}

