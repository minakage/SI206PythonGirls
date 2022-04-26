import requests
from lyricsgenius import Genius
import spotipy.util as util
import matplotlib.pyplot as plt
import os
import sqlite3
import urllib.request, urllib.parse, urllib.error
import unittest

client_access_token = "TdqbB8wmj5911L-VIyyz5eW1xotjd2swpscoJhO1r0GzV-UYbH43nYRiv_8kbGUV"

search_term = "Olivia Rodrigo"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
olivia_json_data = response.json()
for song in olivia_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])
    print(song['result']['full_title'], song['result']['annotation_count'])



search_term = "Bazzi"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
bazzi_json_data = response.json()
for song in bazzi_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])

search_term = "Billie Eilish"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
billie_json_data = response.json()
for song in billie_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])

search_term = "Mac Miller"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
mac_json_data = response.json()
for song in mac_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])

search_term = "Lady Gaga"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
lady_json_data = response.json()
for song in lady_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])

search_term = "Harry Styles"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
harry_json_data = response.json()
for song in harry_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])

search_term = "Post Malone"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
post_json_data = response.json()
for song in post_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])

search_term = "Rihanna"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
rihanna_json_data = response.json()
for song in rihanna_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])

search_term = "Elton John"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
elton_json_data = response.json()
for song in elton_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])

search_term = "Madonna"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
madonna_json_data = response.json()
for song in madonna_json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])



conn = sqlite3.connect('PythonGirls.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS GeniusPageViews')
cur.execute('CREATE TABLE GeniusPageViews (song_title TEXT, pageviews INTEGER)')
for item in olivia_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()

for item in bazzi_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()

for item in billie_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()

for item in mac_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()

for item in lady_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()

for item in harry_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()

for item in post_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()

for item in rihanna_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()

for item in elton_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()

for item in madonna_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusPageViews (song_title, pageviews) VALUES (?,?)''', (item['result']['full_title'], item['result']['stats']['pageviews']))
conn.commit()



song_title_list = []
pageviews_list = []
for i in olivia_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

for i in bazzi_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

for i in billie_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

for i in mac_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

for i in lady_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

for i in harry_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

for i in post_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

for i in rihanna_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

for i in elton_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

for i in madonna_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    pageviews_list.append(i['result']['stats']['pageviews'])

    
# fig = plt.figure()
fig = plt.figure(figsize=(16,8))
plt.bar(song_title_list, pageviews_list, align = "center", color = ["lightskyblue"])
plt.xticks(rotation=90)                                                                                                
plt.xlabel("Song Title and Artist")
plt.ylabel("Pageviews (in hundred thousands)")
spacing = 0.400
fig.subplots_adjust(bottom=spacing)
plt.title("Pageviews of 10 Songs from 10 Artists")
plt.savefig("pageviews.png")
plt.tight_layout()
plt.show()












#second table for annotation count
cur.execute('DROP TABLE IF EXISTS GeniusAnnotationCount')
cur.execute('CREATE TABLE GeniusAnnotationCount (song_title TEXT, annotation_count INTEGER)')
for item in olivia_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()

for item in bazzi_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()

for item in billie_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()

for item in mac_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()

for item in lady_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()

for item in harry_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()

for item in post_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()

for item in rihanna_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()

for item in elton_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()

for item in madonna_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['full_title'], item['result']['annotation_count']))
conn.commit()



song_title_list = []
annotation_list = []
for i in olivia_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])

for i in bazzi_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])

for i in billie_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])

for i in mac_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])

for i in lady_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])

for i in harry_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])

for i in post_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])

for i in rihanna_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])

for i in elton_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])

for i in madonna_json_data['response']['hits']:
    song_title_list.append(i['result']['full_title'])
    annotation_list.append(i['result']['annotation_count'])
    
    
# fig = plt.figure()
fig = plt.figure(figsize=(16,8))
plt.bar(song_title_list, annotation_list, align = "center", color = ["lightgreen"])
plt.xticks(rotation=90)                                                                                                
plt.xlabel("Song Title and Artist")
plt.ylabel("Annotation Count")
spacing = 0.400
fig.subplots_adjust(bottom=spacing)
plt.title("Annotation Count of 10 Songs from 10 Artists")
plt.savefig("pageviews.png")
plt.tight_layout()
plt.show()