import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(input.readLine());
		
		while(TC-->0) {
			StringTokenizer st = new StringTokenizer(input.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			Queue<Pair> q = new LinkedList<>();
			st = new StringTokenizer(input.readLine());
			
			//입력 값과 index를 Pair로 저장
			for(int i = 0; i < N; i++) {
				q.offer(new Pair(Integer.parseInt(st.nextToken()), i));
			}
			
			//최대 값이 찾고자 하는 값에 해당 될 때 까지 poll한다
			for(int i = 1; !q.isEmpty();) {
				if(q.peek().val == qMax(q)) { 
					if(q.poll().idx == M) {
						System.out.println(i);
						break;
					}
					i++;
				}else {
					q.offer(q.poll());
				}
			}
		}
	}
	
	public static int qMax(Queue<Pair> q) {
		int max = Integer.MIN_VALUE;
		Iterator<Pair> iter = q.iterator();
		
		while(iter.hasNext()) {
			Pair next = iter.next();
			if(next.val > max)
				max = next.val;
		}
		
		return max;
	}
}

class Pair{
	int val;
	int idx;
	
	Pair(int val, int idx){
		this.val = val;
		this.idx = idx;
	}
}