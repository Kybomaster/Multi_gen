def find_world(uuid, version):
    import os, json
    spe = "/"
    default_path = os.getcwd()
    os.chdir(f"..{spe}..{spe}minecraftWorlds")
    file_list = os.listdir()
    full_list = [os.path.join(i) for i in file_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime, reverse=True)

    for i in time_sorted_list:
        with open(f"{i}{spe}world_resource_packs.json", "r", encoding="utf8") as f:
            s = json.load(f)
        for o in s:
            if o["pack_id"] == uuid or o["version"] == version:
                return i
    
    os.chdir(default_path)