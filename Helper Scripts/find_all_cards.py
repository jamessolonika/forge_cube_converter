import re
import os

forge_path="/Applications/forge-gui-desktop-1.6.11/res/editions/"

reg = r"[C,U,R,M,L,S]+\s.+"
code=r"^Code=.+"
found_list=[]


for file in os.listdir(forge_path):
    with open(forge_path + file) as file_object:
        set_code=""
        flag=False

        for line in file_object:

            if not flag:
                found=re.search(code,line.strip())
                if found:
                    set_code=line.strip()[5:]
                elif line.strip() == "[cards]":
                    flag=True
            else:
                found=re.search(reg,line.strip())
                if found:
                    found_item=found.group()[2:]
                    if found_item not in found_list:
                        output = "1 " + found_item + "|" + set_code
                        #print(output)
                        found_list.append(output)
                elif line.strip() == "Shield of Kaldra":
                    found_list.append("1 Shield of Kaldra|MBP")
                else:
                    print(file,line)
                    print(found,found_item)

print("[metadata]\nName=__all_cards_test___\n[main]")

found_list.sort()
for ex in found_list:
    print(ex)
