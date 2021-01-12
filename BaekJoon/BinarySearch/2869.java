/* 
// 다른풀이
public class Main {
	public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double v = sc.nextDouble();

        if(v == a) System.out.println(1);
        else System.out.println((int)Math.ceil((v - a) / (a - b)) + 1);
        //double은 실수형이기 때문에 int or long(정수) 타입으로 변환해줘야한다.
    }
}
*/