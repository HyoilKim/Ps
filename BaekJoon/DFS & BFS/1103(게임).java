import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M, max_cnt;
    static int[][] map;
    static int[][] dp;
    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};
    static boolean[][] visited;
    static boolean is_cycle;

    public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        dp = new int[N][M];
        visited = new boolean[N][M];

        for(int i = 0; i < N; i++) {
            String str = br.readLine();
            for(int j = 0; j < M; j++) {
                if (str.charAt(j) == 'H') {
                    map[i][j] = -1;
                } else {
                    map[i][j] = str.charAt(j)-'0';
                }
            }
        }

        dfs(0, 0, 1);
        if (is_cycle) {
            System.out.println(-1);
        } else {
            System.out.println(max_cnt);
        }
    }

    public static void dfs(int x, int y, int cnt) {
        max_cnt = Math.max(max_cnt, cnt);
        dp[x][y] = cnt;

        for(int i = 0; i < 4; i++) {
            int nx = x + (dx[i]*map[x][y]);
            int ny = y + (dy[i]*map[x][y]);
            if (nx < 0 || nx >= N || ny < 0 || ny >= M || map[nx][ny] == -1) continue;
            if (visited[nx][ny]) {
                // System.out.println(nx + " " + ny + "cycle " + (cnt+1));
                is_cycle = true;
                return;
            }
            if (dp[nx][ny] <= cnt) {
                visited[nx][ny] = true;
                dfs(nx, ny, cnt+1);
                visited[nx][ny] = false;
                // System.out.println(nx + " " + ny + " " + (cnt+1));
            }
        }
    }
}