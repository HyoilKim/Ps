import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
		Map<String, Integer> map = new HashMap<>();
		for(int i = 0; i < clothes.length; i++) {
			String key = clothes[i][1];
			if(!map.containsKey(key)) {
				map.put(key, 1);
			}else {
				map.put(key, map.get(key) + 1);
			}
		}
		
        //각 가지수에 + 1 : 선택 or 미선택
		int mul = 1;
		Iterator<String> keys = map.keySet().iterator();
	    while(keys.hasNext()){
	    	String key = keys.next();
	    	if(map.keySet().size() != 1) {
	    		mul *= map.get(key) + 1;
	    	}else {
	    		mul = map.get(key) + 1;
	    	}
	    }
	    //모두 선택하지 않는 경우의 수는 제외
        return(mul - 1);
    }
}