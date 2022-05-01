def item_texture(bp_gen, BP_folder_name, RP_name_config, name_space_config, development_or_world):
    excep_json = ["egg", "bow_pulling", "bow_standby"]
    import os, json
    from w_programs.item_json import create
    path = "textures"
    spe = "/"
    spisok = []
    spisok_not_raw = []
    for a, b, c in os.walk(path):
        for name in c:
            path_file = os.path.join(a, name)
            tmpp = path_file.rsplit("\\", 3)
            if len(tmpp) < 3:
                continue
            try:
                tmp_p = tmpp[2].rsplit(".", 1)[1]
            except:
                continue
            if tmp_p != "png" and tmp_p != "tga":
                continue
            if tmpp[1] == "items":
                spisok_not_raw.append([tmpp[1], tmpp[2]])


    try:
        with open(f"{path}/item_texture.json") as f:
            spisok = json.load(f)
    except:
        spisok = {
        "resource_pack_name": RP_name_config,
        "texture_name": "atlas.items",
        "texture_data": {}}

    for i in spisok_not_raw:
        path3 = "textures"+spe+i[0]+spe+i[1]
        path3 = path3.replace(".png", "").replace(".tga", "") 

        
    for i in spisok_not_raw:
        conti = 0
        cont = 0
        path3 = "textures"+spe+i[0]+spe+i[1]
        path3 = path3.replace(".png", "").replace(".tga", "")
        for ssa in list(spisok["texture_data"].keys()):
            if spisok["texture_data"][ssa]["textures"] == path3:
                cont = 1
                break
        if cont == 1:
            continue
        
        tmpp = i[1].replace(".png", "").replace(".tga", "").replace(" ", "")
        spisok["texture_data"][tmpp] = {"textures": path3}
        for exc in excep_json:
            if tmpp.find(exc) >= 0:
                conti = 1
                break
        if conti == 1:
            continue
        if bp_gen == "y":
            create(tmpp, BP_folder_name, name_space_config, development_or_world)

    path2 = f"{path}{spe}item_texture.json"

    with open(path2, "w") as f:
        json.dump(spisok, f, indent=4)
    print("Текстуры новых предметов были вписаны в item_texture.json")