import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static int[][] sudoku;
	static int blank = 0;
	static boolean oncePrint = false;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sudoku = new int[9][9];
		
		for(int i = 0; i < 9; i++) {
			String[] line = br.readLine().split(" ");
			for(int j = 0; j < 9; j++) {
				sudoku[i][j] = Integer.parseInt(line[j]);
				if(sudoku[i][j] == 0) blank++;
			}
		}	
		
		dfs(0, 0);		
	}	
	
	public static void dfs(int k, int cnt) {
		if(cnt == blank && !oncePrint) {
			printSudoku();
			oncePrint = true;
			return;
		}
		for(int i = k; i < 9*9; i++) {
			int row = i / 9;
			int col = i % 9;
			if(sudoku[row][col] == 0) {
				for(int num = 1; num <= 9; num++) {
					if(!inCol(num, col) && !inRow(num, row) && !inSquare(num, row, col)) {
						sudoku[row][col] = num;
						dfs(i + 1, cnt + 1);
						sudoku[row][col] = 0;
					}
				}
				return;
			}
		}
	}
	
	public static boolean inCol(int val, int col) {
		for(int i = 0; i < 9; i++) {
			if(val == sudoku[i][col])
				return true;
		}
		return false;
	}
	
	public static boolean inRow(int val, int row) {
		for(int i = 0; i < 9; i++) {
			if(val == sudoku[row][i])
				return true;
		}
		return false;
	}
	
	public static boolean inSquare(int num, int x, int y) {
		int xx = x / 3;
		int yy = y / 3;
		
		for(int i = xx * 3; i < xx*3 + 3; i++) {
			for(int j = yy * 3; j < yy * 3 + 3; j++) {
				//System.out.println(x + " " + y);
				if(sudoku[i][j] == num) {
					return true;
				}
			}
		}
		return false;
	}
	
	public static void printSudoku() {
		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				System.out.print(sudoku[i][j] + " ");
			}
			System.out.println("");
		}	
	}
}