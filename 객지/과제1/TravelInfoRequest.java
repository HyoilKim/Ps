package first_hw;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Calendar;
import java.io.FileOutputStream;

public class TravelInfoRequest {
	public static void main(String[] args) {
		try {
			FileReader frP = new FileReader("properties.txt");
			BufferedReader brP = new BufferedReader(frP);
			FileReader frT = new FileReader("template_file.txt");
			BufferedReader brT = new BufferedReader(frT);
			FileOutputStream fos = new FileOutputStream("output_file.txt");
			
			//properties.txt ���� �޾ƿͼ�  KeyValueŸ���� arraylist�� properties�� ����
			ArrayList<KeyValue> properties = new ArrayList<>();			
			String str1 = brP.readLine();
			while(str1 != null) {
				KeyValue k = new KeyValue(str1);
				properties.add(k);
				str1 = brP.readLine();
			}
			
			//date �߰�
			Calendar cal = Calendar.getInstance();		
			String year = cal.get(Calendar.YEAR) + "";
	        String mon = cal.get(Calendar.MONTH) + 1 + "";
	        String day = cal.get(Calendar.DAY_OF_MONTH) + "";	  
			KeyValue date = new KeyValue("date", year + "-" + mon + "-" + day);
			properties.add(date);
			
			//template ���� buf�� ������ �� key���� value�� ����
			//buf�� ���� ����� �����̸�, ���߿� �Ÿ� ���� �߰��� �� ����Ѵ�
			StringBuffer buf = new StringBuffer();
			String str2 = brT.readLine();
		    while(str2 != null) {
		    	buf.append(str2 + "\n"); 
		    	str2 = brT.readLine();
		    }

			String outputString = buf.toString();
			for(KeyValue e : properties){
				outputString = outputString.replace("{" + e.getKey() + "}", e.getValue());	
			}
	        
			//properties���� ���� �������κ��� ��߳���� �������� ���ϴ� �ڵ�
	        String startCountry = "";
	        String departCountry = "";
			for(KeyValue e : properties) {
			    if(e.getKey().contentEquals("startcountry")) {
			    	startCountry = e.getValue();
			    }if(e.getKey().contentEquals("departcountry")) {
			    	departCountry = e.getValue();
			    }
			}

			Countries startingCountry = new Countries(startCountry);
			Countries departingCountry = new Countries(departCountry);	
			
			Distance start = new Distance(startingCountry.getCountry(), startingCountry.getlat(), startingCountry.getlng());
			Distance end = new Distance(departingCountry.getCountry(), departingCountry.getlat(), departingCountry.getlng());
					
			String distanceResult = Distance.getDistance(start, end);        
			outputString = outputString.replace("<add info>", distanceResult);	
			
			//output_file�� ���� ����
	        fos.write(outputString.getBytes("UTF-8"));	        
			frP.close();
			frT.close();
			fos.close();
			brP.close();
			brT.close();
			
			
		}catch(FileNotFoundException e) {
			e.getStackTrace();
		}catch(IOException e2) {
			e2.getStackTrace();
		}
	}

}