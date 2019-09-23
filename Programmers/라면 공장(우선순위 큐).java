import java.util.*;

class Solution {
    public int solution(int stock, int[] dates, int[] supplies, int k) {
		Queue pq = new PriorityQueue<>(Comparator.reverseOrder());
        int ans = 0; 
        int index = 0;
        for (int i = 0; i < k; i++) {
            //����Ȯ��
            if (index < dates.length && i == dates[index])
                pq.add(supplies[index++]);

            //���� ���� ��
            if (stock == 0) {
                int max = (int)pq.poll();
                stock += max;
                ans++;
            }
            stock--;
        }
        return ans;
    }
}