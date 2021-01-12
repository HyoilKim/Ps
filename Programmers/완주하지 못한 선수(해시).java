import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> player = new HashMap<>();
        
        //player�� ���� ī��Ʈ�Ͽ� value�� ����
        for(int i = 0; i < participant.length; i++) {
            String key = participant[i];
            if(!player.containsKey(key)) {
                player.put(key, 1);
            }else {
                player.put(key, player.get(key) + 1);
            }
        }

        //�Ϸ��� �������� value - 1
        for(int i = 0; i < completion.length; i++) {
            String key = completion[i];
            if(value > 0) {
                player.put(key, player.get(key) - 1);
            }       
        }

        //���� value���� 1�̸� �������� ���� ����
        String answer = "";
        for(int i = 0; i < participant.length; i++) {
            if(player.get(participant[i]) > 0) {
                answer = participant[i];
                break;
            }
        }
        return answer;
    }
}