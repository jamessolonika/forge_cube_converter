import re
import os
import glob

forge_path="/Applications/forge-gui-desktop-1.6.11/res/sealed/*.sealed"

search_item="NumPacks:"
reg = r"" + search_item + ".+\n"
found_list=[]
for file in glob.glob(forge_path):
    with open(file) as file_object:
        text=file_object.read()
        found=re.search(reg,text)
        if found:
            found_item=found.group()[len(search_item):-1]
            if found_item not in found_list:
                found_list.append(found_item)
        else:
            print("Error in: ",file)

print("Length: ",len(found_list),"\n\n")

found_list.sort()
for ex in found_list:
    print(ex)
