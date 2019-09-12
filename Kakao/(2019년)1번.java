class Solution {
    public int solution(String s) {
        int min = s.length();
		for(int unit = 1; unit < s.length(); unit++) {
			String res = "";
			int i;
		
			for(i = 0; true; i += unit) {
				if(i + unit > s.length()) {
					res += s.substring(i);
					break;
				}
				String str = s.substring(i, i+unit);
				int cnt = 0;	
				int j = i+unit;
				while(str.equals(s.substring(j-unit, j))) {
					cnt++;
					j += unit;
					if(j > s.length()) break;
				}
				
				if(cnt != 1) {
					res += cnt + str;
					i += unit * (cnt-1);
				}else {
					res += str;
				}
			}
			if(res.length() < min) min = res.length();
		}
		
		return min;
    }
}