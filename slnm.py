# -*- coding: utf-8 -*-
import pprint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# for selections
from selenium.webdriver.common.by import By

start = int(input("Enter begining year: "))
end = int(input("Enter ending year: "))

dv = webdriver.Chrome(ChromeDriverManager().install())

game_data = {}

for i in range(start, end + 1):
	try:
		dv.get(f"https://store.steampowered.com/charts/topsellers/global/{i}-11-5")

		time.sleep(4)

		games = dv.find_elements(By.CSS_SELECTOR, "tbody tr")

		data = {}

		for game in games:
			game_name = game.find_elements(By.CSS_SELECTOR, "td")[2].text
			game_price = game.find_elements(By.CSS_SELECTOR, "td")[3].text

			if "\n" in game_price:
				game_price = game_price.split("\n")[-1]
			elif len(game_price) == 0:
				continue
			elif "Free" in game_price:
				game_price = "FTP"
			data[game_name] = game_price
		game_data[i] = data 
	except:
		continue


pprint.pprint(game_data)