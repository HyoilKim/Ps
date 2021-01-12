import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> player = new HashMap<>();
        
        //player의 수를 카운트하여 value로 저장
        for(int i = 0; i < participant.length; i++) {
            String key = participant[i];
            if(!player.containsKey(key)) {
                player.put(key, 1);
            }else {
                player.put(key, player.get(key) + 1);
            }
        }

        //완료한 선수들은 value - 1
        for(int i = 0; i < completion.length; i++) {
            String key = completion[i];
            if(value > 0) {
                player.put(key, player.get(key) - 1);
            }       
        }

        //아직 value값이 1이면 완주하지 못한 선수
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