import json
import webbrowser
import requests

class Media:

	def __init__(self, trackName="No Title", artistName="No Author", releaseDate="No Year", json=None):
		if json != None:
			self.title = json['trackName']
			self.author = json['artistName']
			self.year = json['releaseDate']
			try:
				self.url = json['trackViewURL']
			except:
				self.url = 'None'
		else:
			self.title = trackName
			self.author = artistName
			self.year = releaseDate


## Other classes, functions, etc. should go here
	def __str__(self):
		return "{} by {} ({})".format(self.title, self.author, self.year)  

	def __len__(self):
		return 0

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass


class Song(Media):
	def __init__(self, trackName="No Title", artistName="No Author", releaseDate="No Year", collectionName="No Album", trackTimeMillis="No track length", primaryGenreName="No Genre", json=None):
		super().__init__(trackName, artistName, releaseDate, json)
		if json != None:
			self.album = json['collectionName']
			self.t_len = json['trackTimeMillis']
			self.gen= json['primaryGenreName']
		else:
			self.album = collectionName
			self.t_len = trackTimeMillis
			self.gen= primaryGenreName

	def __str__(self):
		return "{} by {} ({}) [{}]".format(self.title, self.author, self.year, self.gen)  

	def __len__(self):
		return self.t_len/1000 

class Movie(Media):
	def __init__(self, trackName="No Title", artistName="No Author", releaseDate="No Year", contentAdvisoryRating="None", trackTimeMillis="no length", json=None):
		super().__init__(trackName, artistName, releaseDate, json)
		if json != None:
			self.rating = json['contentAdvisoryRating']
			self.movie_len = ['trackTimeMillis']
		else:
			self.rating = contentAdvisoryRating
			self.movie_len = trackTimeMillis 


	def __str__(self):
		return Media.__str__(self) + "[" + self.rating + "]" 

	def __len__(self):
		return self.t_len/60000
jsonfile = "sample_json.json"

try:
    jfname=open(jsonfile, 'r')
    jfread=jfname.read()
    jsondata=json.loads(jfread)
except:
    jsondata={}

#print(jsondata[0])

# ex=Movie(json=jsondata[0])
# print(ex)

# inst=Song(json=jsondata[1])
# print(inst)

def get_itudata(name):
        baseurl = "https://itunes.apple.com/search"
        parameters = {}
        parameters["term"] = name
        #parameters["entity"] = mtype
        parameters["limit"] = 50
        it_data = requests.get(baseurl, parameters)
        it_dict=it_data.text
        itu_data=json.loads(it_dict)
        return itu_data

#List of song instances
#--------------------------
# song_inst=[]
# for song in dataa['results']:
#     inst1=Song(json=song)
#     song_inst.append(inst1)
# print(song_inst)
#---------------------------
search_term=input("Enter a word to search or type exit to quit")

while search_term!="exit":
	Songs=[]
	Movies=[]
	Other_Media=[]
	word=get_itudata(search_term)
	for item in word['results']:
		if item['kind']=='feature-movie':
			Movies.append(Movie(json=item).__str__())
		elif item['kind']=='song':
			Songs.append(Song(json=item).__str__())
		else:
			Other_Media.append(Media(json=item).__str__())

	all_media = Songs+Movies+Other_Media

	print('song')
	for c, value in enumerate(Songs, 1):
		print(c, value)
	if len(Songs)==0:
		print("No results for songs")
	num=len(Songs)

	print("--------------------------")

	print('movie')
	for c, value in enumerate(Movies, num+1):
		print(c, value)
	if len(Movies)==0:
		print("No results for movies")

	print("--------------------------")

	print('others')
	num2=len(Songs+Movies)
	for c, value in enumerate(Other_Media, num2+1):
		print(c, value)
	if len(Other_Media)==0:
		print("No results")

	if len(all_media)==0:
		break

	search_index=input("Enter a number for more info, or exit:")
	if search_index != "exit":
		ex=all_media[int(search_index)-1]
		print(webbrowser.open(ex))
		search_term=input("Enter a word to search or type exit to quit")
	else:
		break
	


 







