import java.util.Scanner;

public class Main {
    public static void main(String[] args){
		Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[][] triangle = new int[N+1][N+1];
        
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= i; j++){
                triangle[i][j] = in.nextInt();
            }
        }
        
        for(int i = 2; i <= N; i++){
            for(int j = 1; j <= i; j++){
                if(triangle[i-1][j-1] > triangle[i-1][j]){
                    triangle[i][j] += triangle[i-1][j-1];
                }else{
                    triangle[i][j] += triangle[i-1][j]; 
                }
            }
        }
        
        int max = triangle[N][1];
        for(int i = 1; i <= N; i++){
            if(max < triangle[N][i]){
                max = triangle[N][i];
            }
        }
        System.out.print(max);
        
    }
}