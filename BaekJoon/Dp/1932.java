package project;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
		Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int res = makeOne(num);
        System.out.print(res);
    }
    
    public static int makeOne(int n){
        int[] arr = new int[1000001];
        arr[1] = 0;
        for(int i = 2; i <= 1000000; i++){
            if(i % 6 == 0){
                arr[i] = min(arr[i/3], arr[i/2], arr[i-1]) + 1;
            }else if(i % 3  == 0){
                arr[i] = min(arr[i/3], arr[i-1]) + 1;
            }else if(i % 2 == 0){
                arr[i] = min(arr[i/2], arr[i-1]) + 1;
            }else{
                arr[i] = arr[i-1] + 1;
            }
        }
        return arr[n];
    }
    public static int min(int a, int b){
        if(a > b) return b;
        else return a;
    }
    public static int min(int a, int b, int c){
        if(a > b){
            if(b > c) return c;
            else return b;
        }else{
            if(a < c) return a;
            else return c;
        }
    }
}