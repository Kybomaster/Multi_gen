def geometry_create():
	import os, json
	path = "models"
	paths = []
	geo_ids = []
	for a, b, c in os.walk(path):
		for i in c:
			path2 = os.path.join(a, i)
			if path2.rsplit(".", 1)[1] == "json":
				paths.append(path2)
	for i in paths:
		try:
			with open(i) as f:
				a = json.load(f)
			ver = a["format_version"]
			if int(ver.split(".")[1]) >= 12:
				geo_ids.append(a["minecraft:geometry"][0]["description"]["identifier"])
			elif int(ver.split(".")[1]) < 12:
				for i in list(a.keys()):
					if i != "format_version" and i != "debug" and i != "minecraft:geometry":
						geo_ids.append(i)
		except:
			continue
	print("Новые геометрии были получены")
	return geo_ids