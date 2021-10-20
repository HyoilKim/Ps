import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] heights = new int[1001];
        int maxh = 0;
        int maxi = -1;

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken());
            int H = Integer.parseInt(st.nextToken());
            heights[L] = H;
            if (H > maxh) {
                maxi = L;
                maxh = H;
            }
        }
        
        int tmp = 0;
        int total = 0;
        for (int i=1; i<=1000; i++) { 
            tmp = Math.max(tmp, heights[i]);
            total += tmp;
            if (i == maxi) {
                break;
            }
        }
        
        tmp = 0;
        for (int i=1000; i >= 1; i--) {
            if (i == maxi) {
                break;
            }
            tmp = Math.max(tmp, heights[i]);
            total += tmp;
        }

        System.out.println(total);
    }
}