import io
import urllib.request
from PIL import Image
url = 'https://cdn.journaldev.com/wp-content/uploads/2018/02/python-io-string-example.png'
with urllib.request.urlopen(url) as f:
	b = io.BytesIO(f.read())
	im = Image.open(b)
	im.save('out.png')
	print("Done")