package first_hw;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Countries {
	private String country;
	private Double lat;
	private Double lng;

	public ArrayList<String> countryArr = new ArrayList<>();	

	public Countries(String country) throws IOException{
		FileReader frC = new FileReader("Countries.txt");
		BufferedReader brC = new BufferedReader(frC);
		
		String str = brC.readLine();
		while(str != null) {
			countryArr.add(str);
			str = brC.readLine();
		}
		
		for(String e : countryArr) {
			StringTokenizer st = new StringTokenizer(e, ",");
			String tmp = st.nextToken();
			if(tmp.contentEquals(country)) {
				this.country = country;
				this.lat = Double.parseDouble(st.nextToken());
				this.lng = Double.parseDouble(st.nextToken());
			}
		}
		brC.close();
	}
	
	public String getCountry() {
		return country;
	}
	public Double getlat() {
		return lat;
	}	
	public Double getlng() {
		return lng;
	}
	
}

