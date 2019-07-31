import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;

public class Main {
	public static void main(String[] args) throws Exception {
		LinkedList<Integer> gearA = new LinkedList<>();
		LinkedList<Integer> gearB = new LinkedList<>();
		LinkedList<Integer> gearC = new LinkedList<>();
		LinkedList<Integer> gearD = new LinkedList<>(); 
		
		//gear설정
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		for(int i = 0; i < 4; i++) {
			String line = input.readLine();
			for(int j = 0; j < 8; j++) {
				switch(i) {
				case 0: gearA.add(line.charAt(j) - '0');
						break;
				case 1: gearB.add(line.charAt(j) - '0');
						break;
				case 2: gearC.add(line.charAt(j) - '0');
						break;
				case 3: gearD.add(line.charAt(j) - '0');
						break;
				}
			}
		}
		
		int TC = Integer.parseInt(input.readLine());
		while(TC-->0) {
			StringTokenizer st = new StringTokenizer(input.readLine());
			int gearNum = Integer.parseInt(st.nextToken());
			int dir = Integer.parseInt(st.nextToken());
			int aDir = 0; int bDir = 0;
			int cDir = 0; int dDir = 0;
			
			//a, b, c, d가 돌아갈 방향 설정
			switch(gearNum) {
			case 1:
				aDir = dir;
				if(!isSame(gearA, gearB)) { 
					bDir = -aDir;
					if(!isSame(gearB, gearC)) {
						cDir = -bDir;
						if(!isSame(gearC, gearD)) {
							dDir = -cDir;	
						}
					}
				}break;
			case 2:
				bDir = dir;
				if(!isSame(gearA, gearB))  
					aDir = -bDir;				
				if(!isSame(gearB, gearC)) {
					cDir = -bDir;
					if(!isSame(gearC, gearD)) 
						dDir = -cDir;
				}break;
			case 3:
				cDir = dir;
				if(!isSame(gearC, gearD)) 
					dDir = -cDir;
				if(!isSame(gearB, gearC)) { 
					bDir = -cDir;
					if(!isSame(gearA, gearB)) 
						aDir = -bDir;	
				}break;
			case 4:
				dDir = dir;
				if(!isSame(gearC, gearD)) { 
					cDir = -dDir;
					if(!isSame(gearB, gearC)) {
						bDir = -cDir;
						if(!isSame(gearA, gearB)) 
							aDir = -bDir;	
					}
				}break;	
			}
			
			rotateGear(gearA, aDir);
			rotateGear(gearB, bDir);
			rotateGear(gearC, cDir);
			rotateGear(gearD, dDir);
		}
		//결과출력
		int sum = 0;
		if(gearA.get(0) == 1) sum += 1;
		if(gearB.get(0) == 1) sum += 2;
		if(gearC.get(0) == 1) sum += 4;
		if(gearD.get(0) == 1) sum += 8;
		System.out.println(sum);
	}
	
	public static boolean isSame(LinkedList<Integer> a, LinkedList<Integer> b) {
		return a.get(2) == b.get(6);
	}
	
	public static void rotateGear(LinkedList<Integer> gear, int dir) {
		switch(dir) {
		case 0:
			break;
		case 1:
			gear.add(0, gear.get(7));
			gear.remove(8);
			break;
		case -1:
			gear.add(8, gear.get(0));
			gear.remove(0);
			break;
		}
	}
}
