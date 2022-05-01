def create_new_mob(development_or_world, BP_folder_name):
    from w_programs.geometry import geometry_create
    from w_programs.rp_entity_get import rp_entity_get
    import os, json, re, traceback

    def parse_jsonStr_to_json(json_raw):
        try:
            strs = json_raw.read()
            json_str1 = re.sub(re.compile('(//[\\s\\S]*?\n)'), '', strs)
            json_str2 = re.sub(re.compile('(/\*\*\*[\\s\\S]*?/)'), '', json_str1)
            return json.loads(json_str2)
        except Exception as e:
            traceback.print_exc()


    spe = "/"
    sperator2 = "\\"
    default_path = os.getcwd()
    folder_name = default_path.split(sperator2)[-1]

    if development_or_world == "development":
        beh_path = "development_behavior_packs"
    else:
        beh_path = "behavior_packs"


    path_to_behavior = f"{beh_path}{spe}{BP_folder_name}"
    back_pach = f"..{spe}"

    geos = geometry_create()
    entity_geos = rp_entity_get()
    permutations_mass = []
    texture_names = []
    texture_paths = []


    path_to_bp_from_rp = f"{back_pach}{back_pach}{path_to_behavior}"

    os.chdir(path_to_bp_from_rp)
    
    for a, b, c in os.walk("blocks"):
        for i in c:
            per_find = False
            block_path = os.path.join(a, i)
            with open(block_path) as f:
                block = parse_jsonStr_to_json(f)

            try:
                properties = block["minecraft:block"]["description"]["properties"]
                experimental = True
            except:
                continue

            if experimental:
                try:
                    block_geo = block["minecraft:block"]["components"]["minecraft:geometry"]
                    entity_geos.append(block_geo)
                except:
                    per_find = True
                    

                if per_find:
                    try:
                        permutationss = block["minecraft:block"]["permutations"]
                        for g in range(len(permutationss)):
                            permutations_mass.append(permutationss[g])
                    except:
                        s = 1

    
    for h in permutations_mass:
        try:
            entity_geos.append(h["components"]["minecraft:geometry"])
        except:
            s = 1

    k = 0
    k2 = 0
    OK = True
    OK2 = True
    while OK2:
        while OK:
            ch = True
            if geos[k] == geos[-1]:
                OK = False
            if entity_geos[k2] == geos[k]:
                del geos[k]
                ch = False
                OK = False
            if ch:
                k += 1
            else:
                k += 0
        k = 0
        OK = True
        if entity_geos[k2] == entity_geos[-1]:
            OK2 = False
        k2 += 1

    def get_textures():
        os.chdir(default_path)
        textures_list = []
        os.chdir("..")
        for a, b, c in os.walk(folder_name):
            for name in c:
                path_file = os.path.join(a, name)
                tmpp = path_file.rsplit("\\")
                tmp_p = tmpp[-1].rsplit(".", 1)[-1]
                if tmp_p != "png" and tmp_p != "tga":
                    continue
                else:
                    path_list_s_obrabotkoy = spe.join((path_file.replace(f"{folder_name}{sperator2}", "").split(sperator2)))
                    textures_list.append(path_list_s_obrabotkoy)
                    texture_names.append(tmpp[-1].rsplit(".", 1)[0])
        list_texturess = list(zip(texture_names, textures_list))
        
        return list_texturess
    def build_textures_paths(raw_geometries, list_textures):
        k = 0
        k2 = 0
        OK = True
        OK2 = True
        while OK2:
            while OK:
                mob_identificator = (raw_geometries[k2]).replace("geometry.", "")
                if list_textures[-1][0] == list_textures[k][0]:
                    OK = False
                if list_textures[k][0] == mob_identificator:
                    runtime_mass = []
                    runtime_mass.append(list_textures[k][1])
                    runtime_mass.append(raw_geometries[k2])
                    texture_paths.append(runtime_mass)
                    del raw_geometries[k2]
                    OK = False
                else:
                    k += 1
            k = 0
            OK = True
            if raw_geometries == raw_geometries:
                OK2 = False
            k2 += 1

            return texture_paths

    #Добавить новую функция для поиска анимаций
    return build_textures_paths(geos, get_textures())