import os
import shutil
import xml.etree.ElementTree as ET

tree = ET.parse("/Users/andrew/Downloads/Telegram Desktop/Info.plist")
root = tree.getroot()
plist_dict = root.find("dict")

for array in plist_dict.findall("array"):
    dict = array.find("dict")
    if dict is not None:
        key = dict.find("key")
        if key.text == "CFBundleURLSchemes":
            arr = dict.find("array")
            string = arr.find("string")
            string.text = "govno"
# update_images(RES_PATH, STATIC_PATH)
tree.write("/Users/andrew/Downloads/Telegram Desktop/Info.plist")
# load_files_to_drive(RES_PATH)

# disk = GoogleDisk(with_auth=True)
# print(disk.get_folder_id_by_name("com.gootax.k666"))
# shutil.rmtree(merge(RES_PATH, "com.gootax.fsd"))
