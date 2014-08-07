### this assumes the presence of downloaded CogSci HTMLs with 0001/index.html as source
from BeautifulSoup import BeautifulSoup 
import re,os
file("abstracts.txt","w").write("")
for i in range(1,788): 
	## first we need to get the folder name by putting 0's in front them trimmin'!
	folder_name = "000" + str(i)
	folder_name = folder_name[len(folder_name)-3:len(folder_name)]	
	## folders are in a subfolder, then index.html
	folder_name = "../papers/" + folder_name + "/index.html" # sourced from CogSci proceedings HTMLs
	print folder_name
	file_contents = file(folder_name,'r').read() ## read the index.html file
	soup = BeautifulSoup(file_contents) ## parse the HTML
	if (len(soup.findAll('blockquote')[1])>0):
		abstract = soup.findAll('blockquote')[1].contents[0].encode('utf-8').lower()
		abstract = re.sub("\n","",abstract)
		abstract = re.sub("\r","",abstract)
		abstract = re.sub("\f","",abstract)
		file("abstracts.txt","a").write(abstract+"\n")

