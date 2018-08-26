import matplotlib.pyplot as plt

# Amount of positive, neutral and negative
items = [140, 200, 500]
title = "SNA data analysis from Twitter"

labels = 'Positive [' + str(items[0]) + ']', 'Neutral [' + str(items[1]) + ']', 'Negative[' + str(items[2]) + ']'

# Light dataset
colors = ['#10e510','#c1c1c1','#e51010']
# Normal dataset
#colors = ['green', 'grey', 'red']
# Dark dataset
#colors = ['#126612', '#565656', '#661212']

# Splitting the positive from the image a bit.
split = (0.1, 0, 0)
shadow = False
angle = 140

fig = plt.figure()

plt.title(title)
plt.pie(items, explode=split, labels=labels, colors=colors, autopct='%1.1f%%', shadow=shadow, startangle=angle)
plt.axis('equal')
plt.show()

fig.savefig("imgs/Figure1.png")