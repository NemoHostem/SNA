"""
Created by Matias Ijäs
18.08.2018 - 23.08.2018
Word Cloud generator
"""

import os
import numpy as np
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import wikipedia as wp
import wordcloud
from wordcloud import WordCloud,STOPWORDS

bg_col = "white"
max_w = 100
thedir = os.path.dirname(__file__)

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
	wc.to_file(os.path.join(thedir, "img\\wc.png"))
	print("Done")
	plt.figure(figsize=(25,25))
	plt.imshow(wc, interpolation="bilinear")
	plt.axis("off")
	plt.show()
	
print(create_wordcloud(get_wiki_data("Monty Python")))