def get_uuids_rp():
    import os, json
    spe = "/"
    sperator2 = "\\"

    try:
        with open("manifest.json", "r", encoding="utf8") as f:
            s = json.load(f)
        uuid_rp = s["header"]["uuid"]
        version_rp = s["header"]["version"]
    except:
        print("Ошибка чтения RP манифеста (uuid, version)")


    return uuid_rp, version_rp