def getCenterColor(path):
    from PIL import Image

    MAX_SIZE = 70000
    texture = Image.open(path)

    w, h = texture.size
        
    if w*h > MAX_SIZE:
        return [255, 255, 255]
        
    pixel = []
            
    for x in range(w):
        for y in range(h):
            rgb = texture.getpixel((x, y))
            if rgb[-1] > 0:
                pixel.append(rgb)
        
    gener = [sum(i)//len(i) for i in zip(*pixel)]
    return [gener[0], gener[1], gener[2]]

def terrain_texture(bp_gen, BP_folder_name, RP_name_config, name_space_config, beh_path):
    import os, json
    from w_programs.block_json import create
    path = "textures"
    sep = "/"
    listt = []
    list2 = []
    for a, b, c in os.walk(path):
        for name in c:
            path_file = os.path.join(a, name)
            tmpp = path_file.rsplit("\\", 3)
            if len(tmpp) < 3:
                continue
            try:
                tmp_p = tmpp[2].rsplit(".", 1)[1]
            except:
                #print(2)
                continue
            if tmp_p != "png" and tmp_p != "tga":
                ##print(3)
                continue
            if tmpp[1] == "blocks":
                list2.append([tmpp[1], tmpp[2]])

    try:
        with open(f"{path}/terrain_texture.json") as f:
            listt = json.load(f)
    except:
        listt = {
        "resource_pack_name": RP_name_config,
        "texture_name": "atlas.items",
        "padding": 8,
        "num_mip_levels": 4,
        "texture_data": {}}

    for i in list2:
        cont = 0
        path3 = "textures"+sep+i[0]+sep+i[1]
        path3 = path3.replace(".png", "").replace(".tga", "")
        for ssa in list(listt["texture_data"].keys()):
            if listt["texture_data"][ssa]["textures"] == path3:
                cont = 1
                break
        if cont == 1:
            continue

        tmpp = i[1].replace(".png", "").replace(".tga", "").replace(" ", "_")
        if bp_gen == "y":
            try:
                rgb = getCenterColor(f"{path3}.png")
            except:
                rgb = [255, 255, 255]
            create(tmpp, rgb, BP_folder_name, name_space_config, beh_path)
        listt["texture_data"][tmpp] = {"textures": path3}


    path2 = f"{path}/terrain_texture.json"

    with open(path2, "w") as f:
        json.dump(listt, f, sort_keys=False, indent=4)
    print("Текстуры новых блоков были добавлены в terrain_texture.json")