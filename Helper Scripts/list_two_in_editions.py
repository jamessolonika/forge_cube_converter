import re
import os

search_for_1="Type="
search_for_2="Name="
forge_path="/Applications/forge-gui-desktop-1.6.11/res/editions/"


reg_1 = r"" + search_for_1 + ".+\n"
reg_2 = r"" + search_for_2 + ".+\n"
found_list_1=[]
found_list_2=[]

for file in os.listdir(forge_path):
    with open(forge_path + file) as file_object:
        text=file_object.read()
        found=re.search(reg_1,text)
        if found:
            found_item=found.group()[len(search_for_1):-1]
            if found_item not in found_list_1:
                found_list_1.append(found_item)

                found2=re.search(reg_2,text)
                found_item_2=found2.group()[len(search_for_2):-1]
                found_list_2.append(found_item_2)
        else:
            print("Error in: ",file)

print("Length: ",len(found_list_1),"\n\n")

for value in range(0,len(found_list_1)):
    print(found_list_1[value]," ",found_list_2[value])