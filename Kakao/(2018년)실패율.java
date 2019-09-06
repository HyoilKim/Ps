import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int[] tryNum = new int[N+2];
		ArrayList<Rate> failRate = new ArrayList<>();
		
		for(int i = 0; i < stages.length; i++) {
			tryNum[stages[i]]++;
		}
		
		int failPlayer = tryNum[0];
		int totalPlayer = stages.length;
		for(int i = 1; i < tryNum.length-1; i++) {
			failPlayer = tryNum[i];
			float rate = (float)failPlayer / (float)totalPlayer;
			failRate.add(new Rate(rate, i));
			totalPlayer -= tryNum[i]; 		
		}
		
		failRate.sort(null);
		
        int[] answer =  new int[failRate.size()];
		for(int i = 0; i < failRate.size(); i++) {
			answer[i] = failRate.get(i).stage;
		}
        return answer;
    }
}

class Rate implements Comparable<Rate>{
	float rate;
	int stage;
	
	Rate(float rate, int stage){
		this.rate = rate;
		this.stage = stage;
	}
	
	public int compareTo(Rate r) {
		if(this.rate > r.rate) return -1;
		else if(this.rate < r.rate) return 1;
		else return 0;
	}
}