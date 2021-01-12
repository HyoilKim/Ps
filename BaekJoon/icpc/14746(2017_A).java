import java.util.Scanner;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		ArrayList<Pair> arr = new ArrayList<>();
		int n1 = scanner.nextInt();
		int n2 = scanner.nextInt();
		int c1 = scanner.nextInt();
		int c2 = scanner.nextInt();
		
		for(int i = 0; i < n1; i++) {
			Pair p = new Pair(scanner.nextInt(), 1);
			arr.add(p);
		}
		
		for(int i = 0; i < n2; i++) {
			Pair p = new Pair(scanner.nextInt(), 2);
			arr.add(p);
		}
		Collections.sort(arr);
		
		int min = 2147483647;
		int cnt = 0;
		for(int i = 0; i < arr.size()-1; i++) {
			Pair p1 = arr.get(i);
			Pair p2 = arr.get(i+1);
			if(p1.k != p2.k) {
				int sub = p1.pos - p2.pos;
				if(sub < min) {
					min = sub;
					cnt = 1;
				} else if(sub == min) {
					cnt++;
				} else {
					continue;
				}
			}
		}
		min += Math.abs(c1-c2);
		System.out.println(min + " " + cnt);
	}
}
class Pair implements Comparable<Pair>{
	int pos;
	int k;
	
	Pair(int pos, int k){
		this.pos = pos;
		this.k = k;
	}
	
	public int compareTo(Pair p) {
		return p.pos - this.pos;
	}

}