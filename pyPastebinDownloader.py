try:
	import urllib.request
	import ssl
	import sys
	from bs4 import BeautifulSoup
except ModuleNotFoundError:
	print("Error importing the required dependencies")
	print("Please make sure all dependencies have been installed correctly")
	sys.exit()	

def done(filename):
	print("Saved content as " + filename)

def webpage():
	try:
		webpage = urllib.request.urlopen(url, context=context)
		html_doc = webpage.read()
		soup = BeautifulSoup(html_doc, 'html.parser')
		raw = soup.find(id="paste_code").get_text()
		filename = url[-8:] + ".txt"
		save = open(filename, 'w')
		save.write(raw)
		save.close()
		done(filename)
	except:
		print("Error parsing webpage...")
		print("Please try again")
		sys.exit()

def localfile():
	try:
		content = open(url, 'r') 
		for line in content:
			webpage = urllib.request.urlopen(line, context=context)
			html_doc = webpage.read()
			soup = BeautifulSoup(html_doc, 'html.parser')
			raw = soup.find(id="paste_code").get_text()
			filename = line[-8:] + ".txt"
			save = open(filename, 'w')
			save.write(raw)
			save.close()
			done(filename)
	except IOError:
		print("Error opening or reading file...")
		print("Please try again")
		sys.exit()
	except:
		print("Unexpected error...")
		print("Please try again")
		sys.exit()

try:
	context = ssl._create_unverified_context() # Context to disable the default certificate verification
	url = input("Path to file or single link please:\n")
	if (url[0:4] == "http"): # Check if link or path were given
		webpage()
	else:
		localfile()
	
	print("Done.")
except:
	print("Unexpected error...")
	print("Please try again")
	sys.exit()
