import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        HashMap<Character, Integer> map = new HashMap<>();
		
		for (int i = 0; i < skill.length(); i++) {
			map.put(skill.charAt(i), i);
		}
		
		int cnt = 0;
		for (int i = 0; i < skill_trees.length; i++) {
			String skil = skill_trees[i];
			int order = 0;
			boolean error = false;
			
			for (int j = 0; j < skil.length(); j++) {
				char c = skil.charAt(j);
//				System.out.print(c);
				//순서가 있는 스킬이면 차례대로 나와야한다
				if(map.containsKey(c)){
					if(map.get(c) == order) {
						order++;
					}else {
						error = true;
						break;
					}				
				}
			}
            
			if(!error) {
				cnt++;
			}
		}
        return cnt;
    }
}