import os, shutil

folder_path = input("enter path for images folder")
folders = os.listdir(folder_path)


for folder in folders:
	files = os.listdir(folder_path+"/"+folder)
	for file in files:
		dot_index = file.find(".")
		print(dot_index)
		if(file[dot_index:]==".webp"):
			print(file)
			os.remove(folder_path+"/"+folder+"/"+file) 
			try:
				shutil.copy(folder_path[0:-1]+"/"+folder+"/"+file[0:-5], folder_path+"/"+folder+"/"+file[0:-5])
				print("copy"+folder_path[0:-1]+"/"+folder+"/"+file)
			except:
				try:
					shutil.copy(folder_path[0:-1]+"/"+folder+"/"+file[0:-5], folder_path+"/"+folder+"/"+file[0:-5])
					print("copy"+folder_path[0:-1]+"/"+folder+"/"+file)		
				except:
					# try:
						shutil.copy(folder_path[0:-1]+"/"+folder+"/"+file[0:-5], folder_path+"/"+folder+"/"+file[0:-5])
						print("copy"+folder_path[0:-1]+"/"+folder+"/"+file)	
					# except:
					# 	print(folder_path[0:-1]+"/"+folder+"/"+file+"file not copied")
		
