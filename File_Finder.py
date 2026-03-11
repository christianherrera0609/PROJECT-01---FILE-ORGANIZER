import os
import re
import time
import shutil

def image_finder():
    
    x=input("Wich is the folder that you want to analize: ")
    y=input("I am goint to save it in a new folder, give me the location: ")
    w=input("Whic kind of file do you want to find (txt,jpg)?: ")
        
    start=time.time()
    files= os.listdir(x)
    counter=0
    z=w.replace(".","").strip()
    pathern=fr"\.{z}$"

    if not os.path.exists(y):
            os.mkdir(y)
    
    
    for i in files:
        if re.search(pathern,i,re.IGNORECASE):
            full_origin= os.path.join(x,i)
            full_destiny=os.path.join(y,i)
            shutil.move(full_origin,full_destiny)
            counter += 1

    final=time.time()
    time_final1=final-start
    time_final=round(time_final1,4)
    return f"the time to find and move {counter} files was {time_final}"


imgs=image_finder()
print(imgs)    








