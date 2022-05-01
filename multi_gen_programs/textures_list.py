def texture_list():
    import os, json
    spe = "/"
    spe2 = "\\"
    spisok = []
    for root, dirs, files in os.walk("textures"):
        for file in files:
            path_file = os.path.join(root, file)
            spit_path = path_file.rsplit(spe2)
            try:
                posle_tochki = spit_path[-1].rsplit(".", 1)[-1]
            except:
                continue
            if posle_tochki != "png" and posle_tochki != "tga":
                continue
            spisok.append(path_file.replace(".png", "").replace(".tga", "").replace(spe2, spe))



    path2 = "textures_list.json"

    with open(path2, "w") as f:
        json.dump(spisok, f, indent=4)
    print("Файл texture_list.json был сгенерирован")