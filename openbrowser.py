import webbrowser
import sys

new = 2 # open in a new tab, if possible

print 'Openbrowser' 
indent=str(sys.argv[1]) 
# open a public URL, in this case, the webbrowser docs
if indent=='INTERESTED':
	url = "https://www.youtube.com/embed/5-e7NFINJas?list=PLHFlHpPjgk72-DBBxHI1H2ZR2X4y0-bQc&autoplay=1"
	webbrowser.open(url,new=new)
elif indent=='SPECIFICATIONS':
	url = "http://www.apple.com/macbook/specs/"
	webbrowser.open(url,new=new)
