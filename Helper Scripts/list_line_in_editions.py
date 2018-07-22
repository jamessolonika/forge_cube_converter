import re
import os

search_for="Date="
forge_path="/Applications/forge-gui-desktop-1.6.11/res/editions/"


reg = r"" + search_for + ".+\n"
found_list=[]

for file in os.listdir(forge_path):
    with open(forge_path + file) as file_object:
        text=file_object.read()
        found=re.search(reg,text)
        if found:
            found_item=found.group()[len(search_for):-1]
            if found_item not in found_list:
                found_list.append(found_item)
        else:
            print("Error in: ",file)

print("Length: ",len(found_list),"\n\n")
found_list.sort()
print(found_list)