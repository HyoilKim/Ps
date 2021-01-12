import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] supoja1 = {1, 2, 3, 4, 5};
        int[] supoja2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] supoja3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] score = new int[3];

        for(int i = 0; i < answers.length; i++) {
            int i1 = i % 5;
            int i2 = i % 8;
            int i3 = i % 10;
            if(supoja1[i1] == answers[i]) score[0]++;
            if(supoja2[i2] == answers[i]) score[1]++;
            if(supoja3[i3] == answers[i]) score[2]++;
        }

        int max = Math.max(score[0], Math.max(score[1], score[2]));
        int tmp = 0;
        for(int i = 0; i < 3; i++)
            if(max == score[i])
                tmp++;

        int[] res = new int[tmp];
        for(int i = 0, j = 0; i < 3; i++)
            if(max == score[i])
                res[j++] = i+1;

        return res;
    }
}