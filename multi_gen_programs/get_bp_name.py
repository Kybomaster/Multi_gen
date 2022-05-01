def get_bp_folder_name(beh_path):
    import os, json
    spe = "/"
    sperator2 = "\\"
    path = f"..{spe}..{spe}{beh_path}"
    paths = []
    dep_uuid_rp = []
    dep_ver_rp = []
    default_path = os.getcwd()

    try:
        with open("manifest.json", "r", encoding="utf8") as f:
            s = json.load(f)
        uuid_rp = s["header"]["uuid"]
        version_rp = s["header"]["version"]
    except:
        print("Ошибка чтения RP манифеста (uuid, version)")
        
    try:
        with open("manifest.json", "r", encoding="utf8") as f:
            s = json.load(f)
        dep_uuid_rp.append(s["dependencies"][0]["uuid"])
        dep_ver_rp.append(s["dependencies"][0]["version"])
    except:
        print("Ошибка чтения зависимостей в RP манифесте")

    for a, b, c in os.walk(path):
        for i in c:
            if i == "manifest.json":
                paths.append(a.split(sperator2)[-1])

    uuidbp = []
    ver_bp = []
    dep_uuid_bp = []
    dep_ver_bp = []
    dep_path = []

    #создаем массивы где параллельно будут храниться uuid и версии манифестов
    paths.append("stop")
    j = 0
    while paths[j] != "stop":
        try:
            with open(f"{path}{spe}{paths[j]}{spe}manifest.json", "r", encoding="utf8") as f:
                s = json.load(f)
            uuidbp.append(s["header"]["uuid"])
            ver_bp.append(s["header"]["version"])
        except:
            print("Ошибка чтения BP манифеста")
            continue

        try:
            with open(f"{path}{spe}{j}{spe}manifest.json", "r", encoding="utf8") as f:
                s = json.load(f)
            dep_uuid_bp.append(s["dependencies"][0]["uuid"])
            dep_ver_bp.append(s["dependencies"][0]["version"])
            dep_path.append(paths[j])
        except:
            print("Ошибка чтения зависимостей в BP манифесте (uuid, version)")
            continue

    paths.remove("stop")
    print(dep_path)
    
    Isk = True
    for e in range(len(uuidbp)):
        for r in range(len(dep_uuid_rp)):
            if dep_uuid_rp[r] == uuidbp[e]:
                if dep_ver_rp[r] == ver_bp[e]:
                    final_folder_name = paths[e]
                    Isk = False

                else:
                    print("Версия в манифесте BP не совпадает с версией в зависимости RP")
    
    if Isk:
        for e in range(len(uuid_rp)):
            for r in range(len(dep_uuid_bp)):
                if dep_uuid_bp[r] == uuid_rp[e]:
                    if dep_ver_bp[r] == version_rp[e]:
                        final_folder_name = paths[e]
                    else:
                        print("Версия в манифесте RP не совпадает с версией в зависимости BP")

    os.chdir(default_path)
    return final_folder_name, uuid_rp, version_rp