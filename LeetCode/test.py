import json

data, target_value = input().split('/')
data = json.loads(data)
data = sorted(data, key = lambda x : x["pk"], reverse=True)

res = []
parent_pk = 0
for inquiry_type in data:
	if target_value == inquiry_type['value']:
		if  inquiry_type['is_active'] == True:
			res.append(target_value)
			parent_pk = inquiry_type['parent']
		else:
			res.append("INACTIVE")
			break
		
for cur in data:
	if cur['pk'] == parent_pk:
		if cur['is_active'] == True:
		    if cur['parent'] == "null":
				break
            else:
                parent_pk = cur['parent']
                res.append(cur['value'])
		else:
			res.append("INACTIVE")
			break
			
print(res)