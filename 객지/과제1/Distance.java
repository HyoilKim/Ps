package first_hw;

public class Distance {

	private String name;
	private Double lat;
	private Double lng;
	
	public Distance(String name, Double lat, Double lng) {
		this.name = name;
		this.lat = lat;
		this.lng = lng;
	}
	
	public String writeDistance() {
		String locateInfo = "Country : " + name + "\nlatitude = " + lat + "\nlongitude = " + lng + "\n--------------------\n";
		return locateInfo;
	}
	public static String getDistance(Distance a, Distance b) {
		String res = a.writeDistance() + b.writeDistance() + "is\n";
		Double x = a.lat - b.lat;
		Double y = a.lng - b.lng;
		x = Math.pow(x, 2);
		y = Math.pow(y, 2);
		Double dis = Math.sqrt(x + y);
		
		return res + dis;
		
	}
	
}
