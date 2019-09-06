import java.util.Scanner;

public class Main {
    public static void main(String[] args){
		Scanner in = new Scanner(System.in);
        int E = in.nextInt();
        int S = in.nextInt();
        int M = in.nextInt();
        int year = 1;   
        
        int e = 1, s = 1, m = 1;
        while(true){
            if(e == E && s == S && m == M) break;
            year++;
            e++; s++; m++; 
            if(e == 16) e = 1;
            if(s == 29) s = 1;
            if(m == 20) m = 1;      
        }   
        System.out.print(year);
    }   
}