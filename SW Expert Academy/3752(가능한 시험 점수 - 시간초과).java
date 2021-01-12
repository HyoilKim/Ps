package ps;
import java.util.*;
import java.io.*;

public class Test{
	static ArrayList<Integer> allScores;
	public static void main(String[] args) throws Exception{
		
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for(int j = 1; j <= TC; j++) {
        	allScores = new ArrayList<>();
        	int n = Integer.parseInt(br.readLine());
        	boolean[] visited = new boolean[n];
        	String[] line = br.readLine().split(" ");
        	int[] eachScore = new int[n];
        	for(int i = 0; i < n; i++) eachScore[i] = Integer.parseInt(line[i]);
        	
        	for(int i = 1; i <= n; i++) 
        		combination(eachScore, visited, 0, n, i);        
        	System.out.println("#" + j + " " + (allScores.size()+1));
        }
        
	}
	
	static void combination(int[] eachScore, boolean[] visited, int start, int n, int r) {
	    if(r == 0) {
	    	int sum = 0;
	        for(int i = 0; i < n; i++) {
	        	if(visited[i] == true) {
	        		sum += eachScore[i];
	        	}
	        }
	        if(!allScores.contains(sum)) allScores.add(sum);
	        return;
	    } else {
	        for(int i=start; i<n; i++) {
	            visited[i] = true;
	            combination(eachScore, visited, i + 1, n, r - 1);
	            visited[i] = false;
	        }
	    }
	}
}
