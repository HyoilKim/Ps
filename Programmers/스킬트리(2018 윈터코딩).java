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
				//������ �ִ� ��ų�̸� ���ʴ�� ���;��Ѵ�
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