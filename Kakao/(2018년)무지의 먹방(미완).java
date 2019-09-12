package ps;
import java.util.*;

public class Test {
	public static void main(String[] args) {
		int[] food_times = {1, 1, 1};
		long k = 2;
		
		List<Time> timeTable = new LinkedList<>();
		for(int i = 0; i < food_times.length; i++) {
			timeTable.add(new Time(i+1, food_times[i]));
		}
		
		int i = 0;
		while(!timeTable.isEmpty())
		{

			int time = timeTable.get(i).time;
			int idx = timeTable.get(i).idx;
			
			if(time == 1) timeTable.remove(i--);
			else timeTable.set(i, new Time(idx, time-1));
					
			k--;
			if(k == 0) {
				break;
			}

			i++;
			if(i == timeTable.size()) i %= timeTable.size();
		}
		
		if(timeTable.isEmpty()) 
			System.out.println(-1);
		else
			System.out.println(timeTable.get(i).idx);
		
	}
}
class Time{
	int time;
	int idx;
	Time(int idx, int time){
		this.time = time;
		this.idx = idx;
	}
}
