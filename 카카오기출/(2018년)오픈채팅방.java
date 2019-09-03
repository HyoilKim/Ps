import java.util.*;
class Solution {
    public String[] solution(String[] record) {
    	//중복허용 -> Map
    	//for each문 사용 생활화하기
        Map<String, String> idMap = new HashMap<>();
        List<String[]> tmp = new ArrayList<>();

        for(String records : record){
            String[] str = records.split(" ");
            String cmd = str[0];
            String id = str[1];

            if(cmd.equals("Enter")){
                String nickname = str[2];
                idMap.put(id, nickname);
                tmp.add(str);
            }else if(cmd.equals("Change")){
                String nickname = str[2];
                idMap.put(id, nickname);
            }else{
                tmp.add(str);
            }
        }

        String[] answer = new String[tmp.size()];
        int idx = 0;
        for(String[] str : tmp){
            String cmd = str[0];
            String id = str[1];
            String nickName = idMap.get(id);

            if(cmd.equals("Enter"))
                answer[idx++] = nickName + "님이 들어왔습니다.";
            else
                answer[idx++] = nickName + "님이 나갔습니다.";
        }
        return answer;
    }    
}