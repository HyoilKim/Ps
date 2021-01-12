import java.util.*;
import java.io.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		LinkedList<Truck> bridge = new LinkedList<>();
		Queue<Integer> weights = new LinkedList<>();
		int sumWeight = 0;
		int res = 1;
		
		for(int w : truck_weights) weights.add(w);	
		while(!weights.isEmpty() || !bridge.isEmpty()){
			res++;	
			int w = 0;
			if (!weights.isEmpty()) {
				w = weights.peek();
				if(w + sumWeight <= weight) {
					bridge.add(new Truck(w, bridge_length));
					sumWeight += w;
                    weights.poll();
				}
			}			
			//시간 모두 -1
			for (Truck t : bridge) {
				t.moving();
			}
			if (bridge.getFirst().time == 0) {
				Truck t = bridge.removeFirst();
				sumWeight -= t.weight;
			}
        }
        return res;
    }
}

class Truck{
	int weight;
	int time;
	Truck(int weight, int time){
		this.weight = weight;
		this.time = time;
	}
    public void moving() {
		time--;
	}
}