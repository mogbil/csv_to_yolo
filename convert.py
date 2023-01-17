import os
import pandas as pd

width = 0 # Image Width
height = 0 # Image Height
csv = pd.read_csv('') # CSV File
folder = "" # Labels Directory

for i in range(len(csv)):
    c_id = csv.iloc[i][""] # Excel name of Class row
    img_name = csv.iloc[i][""] # Excel name of Image  row
    xmin = csv.iloc[i][""] # Excel name of xmin row
    xmax = csv.iloc[i][""] # Excel name of xmax row
    ymin = csv.iloc[i][""] # Excel name of ymin row
    ymax = csv.iloc[i][""] # Excel name of ymax row
    x = ((xmin + xmax)/2) / width
    y = ((ymin+ ymax)/2) / height
    w = (xmax - xmin) / width
    h = (ymax - ymin) / height
    print(str(int(c_id))," ",x," ",y," ",w," ",h)
    c_img_name = img_name.split(".")
    to_folder = os.path.join(folder+"/"+c_img_name[0]+".txt")
    txt_file = open(to_folder, "a")
    txt_file.write(str(int(c_id))+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"\n")
    txt_file.close()
