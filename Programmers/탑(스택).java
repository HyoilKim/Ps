package ps;
import java.util.*;

public class Test {
	public static void main(String[] args) {
		int[] heights =  {3,9,9,3,5,7,2};
		int len = heights.length;
		int[] res = new int[len];
		
		for(int i = len-1 ; i >= 0; i--) {
			for(int j = i; j >= 0; j--) {
				if(heights[i] < heights[j]) {
					res[i] = j + 1;
					break;
				}
			}
		}
		
		for(int i = 0; i < len; i++)
			System.out.print(res[i] + " ");
	}
}

