import glob

files=glob.glob("*.m")
new_files=[]
for i in range(0,len(files)):
  temp=files[i].split('_')
  new_files.append(temp[4]+'_'+temp[5]+'_'+temp[6]+'_'+temp[7])
  os.rename(files[i],new_files[i])
