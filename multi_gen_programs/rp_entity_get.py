def rp_entity_get():
	import os, json, re, traceback
	path = "entity"
	paths = []
	for a, b, c in os.walk(path):
		for i in c:
			path2 = os.path.join(a, i)
			if path2.rsplit(".", 1)[1] == "json":
				paths.append(path2)

	def parse_jsonStr_to_json(json_raw):
		try:
			strs = json_raw.read()
			json_str1 = re.sub(re.compile('(//[\\s\\S]*?\n)'), '', strs)
			json_str2 = re.sub(re.compile('(/\*\*\*[\\s\\S]*?/)'), '', json_str1)
			return json.loads(json_str2)
		except Exception as e:
			traceback.print_exc()

	geo_values = []
	for i in paths:
		try:
			with open(i) as f:
				a = parse_jsonStr_to_json(f)
			description = a["minecraft:client_entity"]["description"]
			geo_all = (description["geometry"])
			geo_keys = list(geo_all.keys())
			for d in geo_keys:
				if geo_all[d] != "":
					geo_values.append(geo_all[d])
		except:
			continue
	print("Старые геометрии были получены")
	return geo_values