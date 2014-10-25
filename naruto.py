import urllib2
from bs4 import BeautifulSoup as bs


with open('naruto.txt','r') as f:
	last_downloaded_video = f.read()

webpage = urllib2.urlopen('http://www1.narutospot.net/watch/naruto-shippuden-'+last_downloaded_video)

soup = bs(webpage)
a = []
for link in soup.find_all('a'):
	if link.has_attr('data-video-id'):
		a.append(link)

#try just with first data-video-id

id = a[0]['data-video-id']
webpage2 = urllib2.urlopen('http://www1.narutospot.net/video/play/'+id)
soup = bs(webpage2)
string = str(soup.find_all('script')[2])
print string
url = string.split(': ')[1].split(',')[0]
url = url.replace('"','')
with open("temp.txt",'wb') as f:
	f.write(url[1:][:-1])


video = urllib2.urlopen(open("temp.txt").read()).read() #workaround till SO answer
filename = "naruto.mp4"
with open(filename,'wb') as f:
	f.write(video)