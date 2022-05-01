from w_programs.textures_list import texture_list
from w_programs.backup_save import backup
from w_programs.item_textures import item_texture
from w_programs.terrain_texture import terrain_texture
from w_programs.geometry import geometry_create     #Для моба
from w_programs.get_bp_name import get_bp_folder_name
from w_programs.get_uuids import get_uuids_rp
from w_programs.find_world import find_world
from w_programs.getmaincolor_egg_hex import getMainColor_egg_hex   #Это для моба

#from w_programs.create_new_mobs import create_new_mob

import json, os, re

#ИНФОРМАЦИОННЫЙ ПОИСК
def open_json_with_comments(json_raw):
    try:
        strs = json_raw.read()
        json_str1 = re.sub(re.compile('(//[\\s\\S]*?\n)'), '', strs)
        json_str2 = re.sub(re.compile('(/\*\*\*[\\s\\S]*?/)'), '', json_str1)
        return json.loads(json_str2)
    except:
        s = 1

spe = "/"
sperator2 = "\\"
path = f"s{spe}.."
path2 = []
default_path = os.getcwd()
save_stop = ""
for a, b, c in os.walk(path):
    for i in c:
        if i == "a_config.json":
            path2 = os.path.join(a, i)

try:
    with open(path2, "r", encoding='utf8') as f:
        a = open_json_with_comments(f)
except:
    print("Ошибка открытия или чтения конфига (в целом)")

try:
    profile = a["profile"]
    print(f"Был выбран профиль {profile}")
except:
    print("Не удается прочитать какой профиль выбран в конфиге")

try:
    parameters = a["profiles"][profile]["parameters"]
except:
    print("Ошибка чтения параметров из конфига")


try:
    beh_path = os.getcwd().split(sperator2)[-2]
    if beh_path == "development_resource_packs":
        development_or_world = "development"
    else:
        development_or_world = "world"
except:
    print("Ошибка чтения пути")
    save_stop = "y"

try:
    if parameters["name_spaces"]["BP_folder_name"] == "":
        BP_folder_name, rp_uuid, rp_ver = get_bp_folder_name(beh_path)
    else:
        BP_folder_name = parameters["name_spaces"]["BP_folder_name"]
        param_bp = BP_folder_name
except:
    BP_folder_name, rp_uuid, rp_ver = get_bp_folder_name(beh_path)

try:
    uuid_rp = get_uuids_rp()[0]
    ver_rp = get_uuids_rp()[1]
except:
    print("Не удалось получить uuid и версию RP")

try:
    world_name_dep = find_world(uuid_rp, ver_rp)
except:
    print("Ошибка получения имени мира с примененным RP")

try:
    if parameters["name_spaces"]["name_space"] == "":
        name_space = "multigen:"
    else:
        name_space = parameters["name_spaces"]["name_space"]
except:
    name_space = "multigen:"
    
try:
    if parameters["name_spaces"]["RP_name"] == "":
        RP_name = "MultiGen"
    else:
        RP_name = parameters["name_spaces"]["RP_name"]
except:
    RP_name = "MultiGen"
os.chdir(default_path)

try:
    if save_stop != "y":
        if parameters["backup_save"]["save"] == "y":
            is_backup_save = parameters["backup_save"]["save"] == "y"
            backup_parameters = parameters["backup_save"]
            backup_path = backup_parameters["save_path"]
            backup_zip_or_mcworld = backup_parameters["zip_or_mcworld"]
    else:
        print("RP не находится в development или в мире, Поэтому бэкап не будет создан, так же другие функции будут некорректно работать")
except:
    is_backup_save = False

try:
    is_backup_open_file = backup_parameters["open_file"] == "y"
except:
    is_backup_open_file = False

os.chdir(default_path)

try:
    is_texture_list = parameters["textures_list"] == "y"
except:
    is_texture_list = False

try:
    is_item_bp = parameters["item_bp"]
except:
    is_item_bp = False

try:
    is_item_textures = parameters["item_textures"] == "y"
except:
    is_item_textures = False

try:
    is_block_bp = parameters["blocks_bp"]
except:
    is_block_bp = False

try:
    is_terrain_textures = parameters["terrain_textures"] == "y"
except:
    is_terrain_textures = False
os.chdir(default_path)



#ИСПОЛНИТЕЛЬСКАЯ ЧАСТЬ

#БЭКАП
try:
    if save_stop != "y":
        if is_backup_save:
            backup(backup_path, backup_zip_or_mcworld, is_backup_open_file, development_or_world, BP_folder_name, world_name_dep)
    else:
        print("RP не находится в development или в мире, Поэтому бэкап не будет создан, так же другие функции будут некорректно работать")
except:
    print("Ошибка создания бэкапа")
os.chdir(default_path)

#TEXTURES LIST

try:
    if is_texture_list:
        texture_list()
except:
    print("Ошибка создания textures_list.json")

#ITEMS

try:
    if is_item_textures:
        item_texture(is_item_bp, BP_folder_name, RP_name, name_space, development_or_world)
except:
    print("Ошибка создания item_textures.json или bp файлов новых предметов")

#BLOCKS

try:
    if is_terrain_textures:
        terrain_texture(is_block_bp, BP_folder_name, RP_name, name_space, development_or_world)
except:
    print("Ошибка создания terrain_textures.json или bp файлов новых блоков")
os.chdir(default_path)

#СОЗДАТЬ МОБА
#create_new_mob(development_or_world, BP_folder_name)


print("ГЕНЕРАЦИЯ ЗАВЕРШЕНА")