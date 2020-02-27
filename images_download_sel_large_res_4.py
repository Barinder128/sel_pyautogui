import os, shutil

folder_path = input("enter path for images folder")
folder = os.listdir(folder_path)
# similar_looking_1=[""]
# similar_looking_2=[""]

for file_count, file in enumerate(folder):
	clean_file = file.replace(" ", "_")
	and_index = clean_file.find("_and_")
	dot_index = clean_file.find(".")

	# if(file_count>0):
	# 	similar_looking_1.append("")
	# 	similar_looking_2.append("")
	# similar_looking_1[file_count] = clean_file[0: and_index]
	try:
		shutil.copytree("images_high_res/"+clean_file[0: and_index], folder_path+"../"+"images_high_res_1/"+clean_file[0: and_index])
		print("images_high_res/"+clean_file[0: and_index])
	except Exception as e:
		print(e)
		print("error while moving folder: %s" %clean_file[0: and_index])
	# similar_looking_2[file_count] = clean_file[and_index+5:dot_index]
	try:
		shutil.copytree("images_high_res/"+clean_file[and_index+5:dot_index], folder_path+"../"+"images_high_res_2/"+clean_file[and_index+5:dot_index])
		print("images_high_res/"+clean_file[and_index+5:dot_index])
	except Exception as e:
		print(e)
		print("error while moving folder: %s" %clean_file[and_index+5:dot_index])

	














	# for file in files:
	# 	dot_index = file.find(".")
	# 	print(dot_index)
	# 	if(file[dot_index:]==".webp"):
	# 		print(file)
	# 		os.remove(folder_path+"/"+folder+"/"+file) 
	# 		try:
	# 			shutil.copy(folder_path[0:-1]+"/"+folder+"/"+file[0:-5], folder_path+"/"+folder+"/"+file[0:-5])
	# 			print("copy"+folder_path[0:-1]+"/"+folder+"/"+file)
	# 		except:
	# 			try:
	# 				shutil.copy(folder_path[0:-1]+"/"+folder+"/"+file[0:-5], folder_path+"/"+folder+"/"+file[0:-5])
	# 				print("copy"+folder_path[0:-1]+"/"+folder+"/"+file)		
	# 			except:
	# 				# try:
	# 					shutil.copy(folder_path[0:-1]+"/"+folder+"/"+file[0:-5], folder_path+"/"+folder+"/"+file[0:-5])
	# 					print("copy"+folder_path[0:-1]+"/"+folder+"/"+file)	
	# 				# except:
	# 				# 	print(folder_path[0:-1]+"/"+folder+"/"+file+"file not copied")
		
