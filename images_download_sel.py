#!/usr/bin/env python3
import getpass, urllib.request
import pickle
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = getpass.getuser()

driver = webdriver.Firefox(executable_path=r'geckodriver-v0.26.0-linux64/geckodriver')
driver.get('https://www.google.com')
elem_search = driver.find_element_by_css_selector(".gLFyf")
elem_search.send_keys(Keys.CONTROL, 'a') #highlight all in box
elem_search.send_keys('images')
elem_search_btn =  driver.find_element_by_css_selector(".FPdoLc > center:nth-child(1) > input:nth-child(1)")
elem_search_btn.click()
elem_menu_images = driver.find_element_by_css_selector("div.hdtb-mitem:nth-child(2) > a:nth-child(1)")
elem_menu_images.click()
#load pickle file here---------------------
# with open(r"images", "r") as input_file:
# 	pickle_data = pickle.load(input_file)
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
		elem_search_bar = driver.find_element_by_css_selector("#REsRA")
		elem_search_bar.send_keys(Keys.CONTROL, 'a') #highlight all in box
		elem_search_bar.send_keys(clean_pickle_data_value)
		elem_search_btn = driver.find_element_by_css_selector(".CzSCNb > svg:nth-child(1)")
		elem_search_btn.click()
		timeout = 60
		try:
			element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]/img'))
			WebDriverWait(driver, timeout).until(element_present)

			try:
				_path = 'images/%s'  %(clean_pickle_data_value)
				os.mkdir(_path)
			except OSError:
				print ("Creation of the directory %s failed" %_path)

			elem_image1 = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]/img")
			img_src = elem_image1.get_attribute('src')
			# download the image
			urllib.request.urlretrieve(img_src, 'images/%s/%s_01' %(clean_pickle_data_value, clean_pickle_data_value))

			elem_image2 = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[2]/a[1]/div[1]/img")
			img_src = elem_image2.get_attribute('src')
			# download the image
			urllib.request.urlretrieve(img_src, 'images/%s/%s_02' %(clean_pickle_data_value, clean_pickle_data_value))

			elem_image3 = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[3]/a[1]/div[1]/img")
			img_src = elem_image3.get_attribute('src')
			# download the image
			urllib.request.urlretrieve(img_src, 'images/%s/%s_03' %(clean_pickle_data_value, clean_pickle_data_value))

			elem_image4 = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[4]/a[1]/div[1]/img")
			img_src = elem_image4.get_attribute('src')
			# download the image
			urllib.request.urlretrieve(img_src, 'images/%s/%s_04' %(clean_pickle_data_value, clean_pickle_data_value))

			elem_image5 = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[5]/a[1]/div[1]/img")
			img_src = elem_image5.get_attribute('src')
			# download the image
			urllib.request.urlretrieve(img_src, 'images/%s/%s_05' %(clean_pickle_data_value, clean_pickle_data_value))

		except TimeoutException:
		    print("Timed out waiting for page to load")
		

driver.close()