def create(name, BP_folder_name, name_space_config, development_or_world):
    import json, os
    spe = "/"
    pack_name = BP_folder_name
    namespace = name_space_config
    if development_or_world == "development":
        beh_path = "development_behavior_packs"
    else:
        beh_path = "behavior_packs"
    path = f"..{spe}..{spe}{beh_path}{spe}{pack_name}{spe}items{spe}{name}"

    try:
        for root, dirs, files in os.walk(f"w_programs{spe}templates"):
            for file in files:
                if file == "item_template.json":
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

    listt["minecraft:item"]["description"]["identifier"] = namespace + name
    listt["minecraft:item"]["components"]["minecraft:icon"]["texture"] = name
    listt["minecraft:item"]["components"]["minecraft:display_name"]["value"] = name.replace("_", " ")
    with open(path+".json", "w") as f:
        json.dump(listt, f, sort_keys=False, indent=4)
    print("BP нового предмета был сгенерирован")