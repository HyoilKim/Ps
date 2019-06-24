package first_hw;

import java.util.StringTokenizer;

public class KeyValue {	
	private String key;
	private String value;

	public KeyValue(String str) {
		StringTokenizer st = new StringTokenizer(str, "=");
		key = st.nextToken().toString();
		value = st.nextToken().toString();
	}
	public KeyValue(String key, String value) {
		this.key = key;
		this.value = value;
	}
	public String getKey() {
		return key;
	}	
	public String getValue() {
		return value;
	}
}
	