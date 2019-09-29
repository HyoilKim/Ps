import java.util.*;

class Solution {
    static HashSet<Integer> sosuSet = new HashSet<>();
    public int solution(String numbers) {
		char[] tmp = numbers.toCharArray();
		int n = tmp.length;
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
        	arr[i] = tmp[i] - '0';
        }
        
        for (int i = 1; i <= n; i++) {
        	perm(arr, 0, n, i);
        }
        return sosuSet.size();
	}
	
	public static void perm(int[] arr, int depth, int n, int k) { 
		if (depth == k) { 
			String tmp = "";
			for (int i = 0; i < k; i++) {
				tmp += arr[i];
			}
			int num = Integer.parseInt(tmp);
			if(isSosu(num)) {
				sosuSet.add(num);
			}
			return; 
		} 
		for (int i = depth; i < n; i++) { 
			swap(arr, i, depth); 
			perm(arr, depth + 1, n, k); 
			swap(arr, i, depth); 
		}
	}

	public static void swap(int[] arr, int i, int j) {
		int temp = arr[i]; 
		arr[i] = arr[j]; 
		arr[j] = temp;
	}
	
	public static boolean isSosu(int num) {
		if(num <= 1) return false;
		
		for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
		return true;
	}
}