from os import chdir


def backup(backups_path, zip_or_mcworld, Load_to_minecraft, development_or_world, beh_path, world_name_dep):
    import os, zipfile, time, shutil
    from os import startfile
    from w_programs.get_bp_name import get_bp_folder_name
    spe = "/"
    sperator2 = "\\"
    path = f"..{spe}..{spe}.." #Путь назад
    path_mcworld = f"..{spe}.." #Путь назад если mcworld
    path_dev_mcworld = f""
    path_to_world = os.getcwd()
    folder_name = path_to_world.split(sperator2)[-3]
    folder_name_dev = path_to_world.split(sperator2)[-1]
    bp_path_dev = f"..{spe}development_behavior_packs"

    def get_folder_name(): #Получения имени родительской папки, нужно для development
        path_to_def_folder = os.getcwd()
        folder_name_def = path_to_def_folder.split(sperator2)[-1]
        return folder_name_def

    name = get_folder_name()

    tek = time.strftime("%y.%m.%d %H-%M-%S")
    archive_name = f"{tek.replace(':', '-')} {folder_name}.{zip_or_mcworld}"

    if development_or_world == "world":
    
        if zip_or_mcworld == "mcworld":
            os.chdir(path_mcworld)
            zip_file = zipfile.ZipFile(archive_name, "w", compression=zipfile.ZIP_DEFLATED)
            for root, dirs, files in os.walk(f"s{sperator2}.."):
                for file in files:
                    if file == archive_name:
                        continue
                    else:
                        zip_file.write(os.path.join(root, file))

        else:
            os.chdir(path)
            zip_file = zipfile.ZipFile(archive_name, "w", compression=zipfile.ZIP_DEFLATED)
            for root, dirs, files in os.walk(f"{folder_name}"):
                for file in files:
                    if file == archive_name:
                        continue
                    else:
                        zip_file.write(os.path.join(root, file))


    elif development_or_world == "development":

        def fix_pre_za():
            try:
                os.chdir(f"..{spe}__runtime_multigen__")
                os.chdir("..")
                shutil.rmtree("__runtime_multigen__")
                os.chdir(path_to_world)
            except:
                os.chdir(path_to_world)

        os.chdir(path_to_world)
        fix_pre_za()
        os.chdir(path_to_world)

        archive_name = f"{tek.replace(':', '-')} {folder_name_dev}.{zip_or_mcworld}"
        if zip_or_mcworld == "mcworld":
            archive_name = f"{tek.replace(':', '-')} {folder_name_dev}.zip"
        name_bez_n = name
        for n in range(10000):
            numb = "(" + str(n) + ")"
            name_bez_n = name_bez_n.replace(numb, "")

                  
        os.chdir("..")
        shutil.copytree(name, f"__runtime_multigen__{spe}RP_{name_bez_n}")
        os.chdir("__runtime_multigen__")
        zip_file = zipfile.ZipFile(archive_name, "w", compression=zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(f"RP_{name_bez_n}"):
            for file in files:
                if file == archive_name:
                    continue
                else:
                    zip_file.write(os.path.join(root, file))
        os.chdir("..")
                    
        name_bez_n = beh_path
        for n in range(10000):
            numb = "(" + str(n) + ")"
            name_bez_n = name_bez_n.replace(numb, "")
        os.chdir(f"..{spe}development_behavior_packs")
        shutil.copytree(beh_path, f"..{spe}development_resource_packs{spe}__runtime_multigen__{spe}BP_{name_bez_n}")
        os.chdir(f"..{spe}development_resource_packs{spe}__runtime_multigen__")
        for root, dirs, files in os.walk(f"BP_{name_bez_n}"):
            for file in files:
                if file == archive_name:
                    continue
                else:
                    zip_file.write(os.path.join(root, file))

        os.chdir(f"..{spe}..{spe}minecraftWorlds")


        if zip_or_mcworld == "mcworld":
            os.chdir(world_name_dep)
            archive_name_world = f"{tek.replace(':', '-')} {folder_name_dev}.{zip_or_mcworld}"
            zip_file_world = zipfile.ZipFile(archive_name_world, "w", compression=zipfile.ZIP_DEFLATED)
            for root, dirs, files in os.walk(f"s{sperator2}.."):
                for file in files:
                    if file == archive_name_world:
                        continue
                    else:
                        zip_file_world.write(os.path.join(root, file))
            zip_file_world.close()
            zip_file.write(archive_name_world)
            os.remove(archive_name_world)

        else:
            shutil.copytree(world_name_dep, f"..{spe}development_resource_packs{spe}__runtime_multigen__{spe}World")

            os.chdir(f"..{spe}development_resource_packs{spe}__runtime_multigen__")
            for root, dirs, files in os.walk("World"):
                for file in files:
                    if file == archive_name:
                        continue
                    else:
                        zip_file.write(os.path.join(root, file))



    os.chdir(f"{path_to_world}{spe}..")

    zip_file.close()
    if Load_to_minecraft:
        startfile(archive_name)
    else:
        shutil.move(f"__runtime_multigen__{spe}{archive_name}", backups_path)

    shutil.rmtree("__runtime_multigen__")
    
    print("Создан бэкап")