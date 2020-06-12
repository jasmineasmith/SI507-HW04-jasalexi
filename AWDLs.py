#Help on scraping javascript from: https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f
#Help on xpath from: https://selenium-python.readthedocs.io/locating-elements.html

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import requests
import json
import codecs
import sys
import csv
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
#import urllib2
#import re
CACHE_FNAME="AWDLsearch1.json"
try:
    fopen=open(CACHE_FNAME, "r")
    fread=fopen.read()
    CACHE_DICTION=json.loads(fread)
except:
    CACHE_DICTION={}

driver = webdriver.Firefox()


def getawdldata(url):
	base_url=url
	uniq=base_url+'geturls'
	if uniq in CACHE_DICTION:
		return CACHE_DICTION[uniq]
	else:
		driver.get(url)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
		time.sleep(10)
		data2=[]
		garbage=[]
		continue_link = driver.find_element_by_tag_name('a')
		elems = driver.find_elements_by_xpath("//a[@href]")
		for elem in elems:
			b=elem.get_attribute("href")
			if "books" in b:
				data2.append(b)
			else:
				garbage.append(b)
		data2 = list(dict.fromkeys(data2))
		driver.quit()
		CACHE_DICTION[uniq] = data2
		dumped_json_cache = json.dumps(CACHE_DICTION)
		fw = open(CACHE_FNAME,"w")
		fw.write(dumped_json_cache)
		fw.close()
		return CACHE_DICTION[uniq]

sprd=[]

pages=[1,2,3,4,5,6,7]
for page in pages:
	url='http://dlib.nyu.edu/ancientworld/search/?q=papyrology&page='+str(page)
	links=getawdldata(url)
	for link in links:
		k=link.replace("http://dlib.nyu.edu/ancientworld", "http://sites.dlib.nyu.edu/viewer")
		l=k+"?embed=true"
		driver.get(l)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
		time.sleep(10)
		title = driver.find_element_by_tag_name('h2')
		d=title.text
		handle = driver.find_elements_by_xpath("//div[@class='field field-name-field-handle field-type-link-field field-label-inline clearfix']")
		garbage2=[]
		for h in handle:
			i=h.text
			if "handle.net" in i:
				j=i.strip('Permanent Link:')
			else:
				garbage2.append(i)
		sprd.append({"Title":d, "Handle":j})

'''for link in links:
	driver.get(link)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
	time.sleep(10)
	title = driver.find_elements_by_class_name('field field-name-title field-type-ds field-label-hidden')
	handle = driver.find_elements_by_class_name('field field-name-field-handle field-type-link-field field-label-inline clearfix')
	
'''
test=links[1]

#need the link in iframe src




#title = driver.find_elements_by_class_name('field field-name-title field-type-ds field-label-hidden')


#handle = driver.find_elements_by_class_name('field field-name-field-handle field-type-link-field field-label-inline clearfix')
#handle = driver.find_elements_by_class_name('field-item even') 
#handle = driver.find_element_by_css_selector('div.field.field-name-title.field-type-ds.field-label-hidden')



driver.quit()


#print(sprd)
df = pd.DataFrame(sprd)
df.to_csv('AWDL_papyrology_search.csv')
print(sprd)

#print(len(e))

'''
def getawdldata2(url):
	base_url=url
	uniq=base_url+'geturls'
	if uniq in CACHE_DICTION:
		return CACHE_DICTION[uniq]
	else:
		resp = requests.get(base_url)
		CACHE_DICTION[uniq] = resp.text
		dumped_json_cache = json.dumps(CACHE_DICTION)
		fw = open(CACHE_FNAME,"w")
		fw.write(dumped_json_cache)
		fw.close()
		return CACHE_DICTION[uniq]

aa=getawdldata2(test)

soup = BeautifulSoup(aa, 'html.parser')
e=soup.find('h2')
'''






# specify the url
'''urlpage = 'http://dlib.nyu.edu/ancientworld/search/?q=papyrology&page=1' 

# run firefox webdriver from executable path of your choice
driver = webdriver.Firefox()

# get web page
driver.get(urlpage)

# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)

#results = driver.find_elements_by_partial_link_text('papy')
#results = driver.find_elements_by_class_name('md_title')
#results2 = driver.find_elements_by_xpath("//h1[a/@href='']")
#results2 = driver.find_elements_by_xpath("//a[1]")
#results2 = driver.findElement(By.partialLinkText("books"))			
#.getText()
data2=[]
garbage=[]
continue_link = driver.find_element_by_tag_name('a')
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    b=elem.get_attribute("href")
    if "books" in b:
    	data2.append(b)
    else:
    	garbage.append(b)

#remove duplicate links in list
data2 = list(dict.fromkeys(data2))

# close driver 
driver.quit()
# save to pandas dataframe



print(data2)
#df = pd.DataFrame(data)
#print(df)


'''







#############
# create empty array to store data
#data = []
# loop over results
#for result in results:
	#print('hi')
    #title = result.text
    #link = result.find_element_by_tag_name('a')
    #product_link = link.get_attribute("href")
    # append dict to array
    #data.append({"hi" : 5})#, "link" : product_link})
    #a=result.text
    #data.append(a)
    #print(result)












########################################################################
#base_url='http://dlib.nyu.edu/ancientworld/search/?q=papyrology&page=1'
'''def getawdldata(url):
	base_url=url
	uniq=base_url+'newsearch'
	if uniq in CACHE_DICTION:
		return CACHE_DICTION[uniq]
	else:
		#resp = requests.get(base_url)
		resp = driver.get(base_url)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
		time.sleep(30)
		driver.quit()
		#CACHE_DICTION[uniq] = resp.text
		CACHE_DICTION[uniq] = resp
		dumped_json_cache = json.dumps(CACHE_DICTION)
		fw = open(CACHE_FNAME,"w")
		fw.write(dumped_json_cache)
		fw.close()
		return CACHE_DICTION[uniq]

u=getawdldata(urlpage)

#print(u)


#results = driver.find_elements_by_xpath("//*[@class=' md_title']")






#print('Number of results', len(results))
#driver.command_executor.set_timeout()'''

