import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean contain = false;
		Arrays.sort(phone_book);
		
		for(int i = 0; i < phone_book.length-1; i++) {
			if(phone_book[i+1].contains(phone_book[i])) {
				contain = true;
				break;
			}
		}
		
		if(contain) return false;
		else return true;
    }
}