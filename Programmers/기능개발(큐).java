import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> q = new LinkedList<>();
        LinkedList<Integer> ans = new LinkedList<>();

        for( int i = 0; i < progresses.length; i++ ) {
            int dayToDeploy = (int)Math.ceil((100 - progresses[i]) / speeds[i]);
            if (dayToDeploy == 0) dayToDeploy = 1;
            q.offer(dayToDeploy);
        }

        while( !q.isEmpty() ) {
            int numOfDeploy = 1;
            int dayToDeploy = q.poll();
            if( q.isEmpty() ) {
                ans.add(numOfDeploy);
                break;
            }
            int next = q.peek();

            while( dayToDeploy >= next ) {
                numOfDeploy++;
                q.poll();
                if( q.size() == 0 ) {
                    break;
                }
                next = q.peek();
            }

            ans.add(numOfDeploy);
        }

        int[] answer = new int[ans.size()];
        for( int i = 0; i < ans.size(); i++ ) {
            answer[i] = ans.get(i);
        }

        return answer;
    }
}