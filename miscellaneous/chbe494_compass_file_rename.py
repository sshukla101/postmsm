import glob
import os

files=glob.glob("*.m")
new_files=[]
for i in range(0,len(files)):
  temp=files[i].split('_')
  new_files.append(temp[4]+'_'+temp[5]+'_'+temp[6]+'_'+temp[7])
  os.rename(files[i],new_files[i])
  
  
  txt_files=glob.glob(".txt")
  
  for f in txt_files:
    os.remove(f)
