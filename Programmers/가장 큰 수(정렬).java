import java.util.*;
class Solution {
    public String solution(int[] numbers) {
		Number[] number = new Number[numbers.length];
		for (int i = 0; i < number.length; i++) {
			number[i] = new Number(Integer.toString(numbers[i]));
		}
		Arrays.sort(number);
		
		String answer = "";
		for (int i = number.length-1; i >= 0; i--) {
			answer += number[i].num;
		}
	
		//������������ ���� ������ ���� ���ڸ� 0�̶�� ���� 0�̴�.
		if (answer.charAt(0) == '0') return "0";
		
        return answer;
    }
}


class Number implements Comparable<Number>{
	String num;
	Number(String num){
		this.num = num;
	}
	public int compareTo(Number o) {
		// 121 122 vs 122 121 �ٿ��� ��
	    return (this.num + o.num).compareTo(o.num + this.num);		
	}
}