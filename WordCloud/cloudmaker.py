"""
Created by Matias Ijäs
18.08.2018 - 23.08.2018
Word Cloud generator
"""

import os
import numpy as np
import csv
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import wikipedia as wp
import wordcloud
from wordcloud import WordCloud,STOPWORDS

bg_col = "#ff22ff"
max_w = 100
thedir = os.path.dirname(__file__)
csv_file = "csvs/test.csv"

def get_wiki_data(que):

	title = wp.search(que)[0]
	page = wp.page(title)
	print(page)
	print(page.content)
	return page.content
	
def create_wordcloud(text):
	
	# Image should exists
	mask = np.array(Image.open(os.path.join(thedir, "cloud3.png")))
	stopwords = set(STOPWORDS)
	wc = WordCloud(background_color=bg_col, mask=mask, max_words=max_w, stopwords=stopwords)
	wc.generate(text)
	wc.to_file(os.path.join(thedir, "imgs/wc1.png"))
	print("Done")
	plt.figure(figsize=(25,25))
	plt.imshow(wc, interpolation="bilinear")
	plt.axis("off")
	plt.show()
	
def get_text_from_csv(file):
	text = ""
	the_reader = csv.reader(open(file), delimiter = " ", quotechar = '|')
	for x, line in enumerate(the_reader, start=1):
		try:
			print(','.join(line))
			
			hash_word = ""
			hash_word_on = 0
			for char in (','.join(line)):
				if char == '#':
					hash_word_on = 1
				elif hash_word_on:
					if char != " " and char != "," and char != ".":
						hash_word += char
					else:
						text += " " + filter_hashtag_data(hash_word)
						hash_word = ""
						hash_word_on = 0
			if hash_word_on:
				text += " " + filter_hashtag_data(hash_word)

		except UnicodeDecodeError:
			print("Error in line: " + str(x))
	
	print(text)
	return text
	
def filter_hashtag_data(word):
	
	new_hashtag = ""
	allowed_characters = "1234567890qwertyuiopåasdfghjklöäzxcvbnmQWERTYUIOPÅASDFGHJKLÖÄZXCVBNM"
	print(word)
	for char in word:
		if char not in allowed_characters:
			break
		else:
			new_hashtag += char
	return new_hashtag
	
#print(create_wordcloud(get_text_from_csv(csv_file)))
print(create_wordcloud(get_wiki_data("Social Network Analysis")))

"""
Errors:

Naming file wordcloud.py -> WordCloud cannot be imported
Using wrong canvas -> Canvas too small
Using wrong canvas -> Cannot identify it as a picture
Using non-existent image -> OSError: Image cannot be opened
This saves images, but those cannot be accessed?
"""