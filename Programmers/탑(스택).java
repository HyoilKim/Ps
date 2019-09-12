class Solution {
    public int[] solution(int[] heights) {
        int len = heights.length;
        int[] res = new int[len];

        for(int i = len-1 ; i >= 0; i--) {
            for(int j = i; j >= 0; j--) {
                if(heights[i] < heights[j]) {
                    res[i] = j + 1;
                    break;
                }
            }
        }
        return res;
    }
}