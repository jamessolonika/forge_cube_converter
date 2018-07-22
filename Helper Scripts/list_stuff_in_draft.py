import re
import os
import glob

forge_path="/Applications/forge-gui-desktop-1.6.11/res/sealed/*.sealed"


reg = r".+:"
found_list=[]
for file in glob.glob(forge_path):
    with open(file) as file_object:
        for line in file_object:
            found=re.search(reg,line)
            if found:
                found_item=found.group()
                if found_item not in found_list:
                    found_list.append(found_item)
            elif line == "\n":
                pass
            else:
                print("Error in: ",file)

print("Length: ",len(found_list),"\n\n")

print(found_list)
