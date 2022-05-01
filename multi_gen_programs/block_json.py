def create(name, rgb, BP_folder_name, name_space_config, development_or_world):
  import json, os
  rotate = "y"
  if development_or_world == "development":
      beh_path = "development_behavior_packs"
  else:
      beh_path = "behavior_packs"
  pack_name = BP_folder_name
  namespace = name_space_config
  spe = "/"
  path = f"..{spe}..{spe}{beh_path}{spe}{pack_name}{spe}blocks{spe}{name}"
  try:
    for root, dirs, files in os.walk(f"w_programs{spe}templates"):
      for file in files:
        if file == "block_template.json":
          path_template = os.path.join(root, file)
  except:
    pass

  try:
      open(path).close()
      return None
  except:
      pass

  try:
    listt_raw = open(path_template)
    listt = json.load(listt_raw)
  except:
    print("не удается найти шаблон")

  
  listt["minecraft:block"]["description"]["identifier"] = namespace + name
  listt["minecraft:block"]["components"]["minecraft:material_instances"]["*"]["texture"] = name
  listt["minecraft:block"]["components"]["minecraft:display_name"] = name.replace("_", " ")
  listt["minecraft:block"]["components"]["minecraft:map_color"] = rgb
  with open(path+".json", "w") as f:
      json.dump(listt, f, sort_keys=False, indent=4)
  print("BP нового блока был сгенерирован")