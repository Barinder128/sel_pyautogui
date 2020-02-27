import os, shutil

folder_path = input("enter path for images folder")
files = os.listdir(folder_path)

pickle_data = {1: 'Alicia Silverstone',
2: 'Kristen Stewart',
3: 'Amy Adams',
4: 'Isla Fisher',
5: 'Benicio Del Toro',
6: 'Brad Pitt',
7: 'Chace Crawford',
8: 'Ian Somerhalder',
9: 'Chandra Wilson',
10: 'Alex Newell',
11: 'Chord Overstreet',
12: 'Austin Butler',
13: 'Dana Delany',
14: 'Mimi Rogers',
15: 'Dane Cook',
16: 'Skylar Astin',
17: 'Drea de Matteo',
18: 'Portia de Rossi',
19: 'Ellen Barkin',
20: 'Cameron Diaz',
21: 'Emily Kinney',
22: 'Evanna Lynch',
23: 'Emmanuelle Chriqui',
24: 'JWoww',
25: 'Fabio',
26: 'Jon Hamm',
27: 'Henry Cavill',
28: 'Matt Bomer',
29: 'Jada Pinkett Smith',
30: 'Zoe Saldana',
31: 'Jai Courtney',
32: 'Phillip Phillips',
33: 'Jeffrey Dean Morgan',
34: 'Javier Bardem',
35: 'Jessica Chastain',
36: 'Bryce Dallas Howard',
37: 'Jordana Brewster',
38: 'Demi Moore',
39: 'Katy Perry',
40: 'Zooey Deschanel',
41: 'Leighton Meester',
42: 'Minka Kelly',
43: 'Logan Marshall-Green',
44: 'Tom Hardy',
45: 'Margot Robbie',
46: 'Jaime Pressly',
47: 'Rachel Bilson',
48: 'Selena Gomez',
49: 'Sarah Hyland',
50: 'Mila Kunis'}

for i_count, pickle_data_key in enumerate(pickle_data.keys()):
	print(i_count)
	if(i_count<0):
		pass
	else:
		pickle_data_value = pickle_data[pickle_data_key]
		clean_pickle_data_value = pickle_data_value.replace(" ", "_")

		try:
			_path = '%s/%s'  %(folder_path, clean_pickle_data_value)
			os.mkdir(_path)
		except OSError:
			print ("Creation of the directory %s failed" %_path)

		for file in files:
			if(file[0: len(clean_pickle_data_value)]==clean_pickle_data_value):
				if(file[len(clean_pickle_data_value)]==".webp"):
					shutil.move(folder_path[0:-1]+"/"+file[0: len(clean_pickle_data_value)]+"/"+file, folder_path+"/"+file[0: len(clean_pickle_data_value)]+"/"+file)
				else:
					shutil.move(folder_path+"/"+file, folder_path+"/"+file[0: len(clean_pickle_data_value)]+"/"+file)
