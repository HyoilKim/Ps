import java.util.Stack;
class Solution {
    public String solution(String p) {
        if(isCorrect(p)) return p;
		else return toCorrect(p);	
    }
    
    public static String toCorrect(String s) {
		if(s.equals("")) return "";
		else {
			//u와 v나누기
			int left = 0;
			int right = 0;
			int i;
			for(i = 0; i < s.length(); i++) {
				
				if(s.charAt(i) == '(') left++;
				else right++;		
				if(left == right) break;
			}
			String u = s.substring(0, i+1);
			String v = s.substring(i+1);
			
			//() ))((() -> ))(( () -> ()
			String res = "";
			if(isCorrect(u)) {
				res += u + toCorrect(v);
			}else {
				String tmp = "(";
				tmp += toCorrect(v);
				tmp += ")";
				u = u.substring(1, u.length()-1);	//앞뒤 자르고
				for(int j = 0; j < u.length(); j++) { // '(' -><- ')'
					if(u.charAt(j) == '(') tmp += ")";
					else tmp += "(";
				}
				res += tmp;
			}
			
			return res;
		}
	}
	
	public static boolean isCorrect(String s) {
		Stack<String> stack = new Stack<String>();
		for(int i = 0; i < s.length(); i++) {
			if(s.charAt(i) == '(') {
				stack.add("(");
			}else {
				if(stack.isEmpty()) return false;
				stack.pop();
			}
			
		}
		return true;
	}
}