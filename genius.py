import requests
from lyricsgenius import Genius
import spotipy.util as util
import matplotlib.pyplot as plt
import os
import sqlite3
import urllib.request, urllib.parse, urllib.error
import unittest

client_access_token = "TdqbB8wmj5911L-VIyyz5eW1xotjd2swpscoJhO1r0GzV-UYbH43nYRiv_8kbGUV"

pageviews_list = []

#first chart for pageviews
search_term = "Olivia Rodrigo"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
olivia_json_data = response.json()
for song in olivia_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))


search_term = "Bazzi"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
bazzi_json_data = response.json()
for song in bazzi_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))

search_term = "Billie Eilish"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
billie_json_data = response.json()
for song in billie_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))

search_term = "Mac Miller"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
mac_json_data = response.json()
for song in mac_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))

search_term = "Lady Gaga"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
lady_json_data = response.json()
for song in lady_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))

search_term = "Harry Styles"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
harry_json_data = response.json()
for song in harry_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))

search_term = "Post Malone"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
post_json_data = response.json()
for song in post_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))

search_term = "Rihanna"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
rihanna_json_data = response.json()
for song in rihanna_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))

search_term = "Elton John"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
elton_json_data = response.json()
for song in elton_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))

search_term = "Madonna"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
response = requests.get(genius_search_url)
madonna_json_data = response.json()
for song in madonna_json_data['response']['hits']:
    pageviews_list.append((song['result']['title'], song['result']['stats']['pageviews']))

print(pageviews_list)



conn = sqlite3.connect('PythonGirls.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS GeniusPageViews (song_title TEXT, pageviews INTEGER)')
conn.commit()
cur.execute('SELECT * FROM GeniusPageViews')
data = cur.fetchall()
if len(data) < 75:
    for item in pageviews_list[len(data):len(data) + 25]:
        cur.execute('INSERT OR IGNORE INTO GeniusPageViews (song_title TEXT, pageviews INTEGER) VALUES (?,?,?)''', (item[0], item[1]))
        conn.commit()
elif len(data) >= 75:
    for item in pageviews_list[len(data):]:
        cur.execute('INSERT OR IGNORE INTO GeniusPageViews (song_title TEXT, pageviews INTEGER) VALUES (?,?,?)''', (item[0], item[1]))
        conn.commit()



song_title_list = []
pageviewsVal_list = []
for i in pageviews_list:
    song_title_list.append(i[0])
    pageviewsVal_list.append(i[1])


fig = plt.figure(figsize=(16,8))
plt.bar(song_title_list, pageviewsVal_list, align = "center", color = ["lightskyblue"])
plt.xticks(rotation=90)                                                                                                
plt.xlabel("Song Title")
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
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()

for item in bazzi_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()

for item in billie_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()

for item in mac_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()

for item in lady_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()

for item in harry_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()

for item in post_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()

for item in rihanna_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()

for item in elton_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()

for item in madonna_json_data['response']['hits']:
    cur.execute('INSERT INTO GeniusAnnotationCount (song_title, annotation_count) VALUES (?,?)''', (item['result']['title'], item['result']['annotation_count']))
conn.commit()



song_title_list = []
annotation_list = []
for i in olivia_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])

for i in bazzi_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])

for i in billie_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])

for i in mac_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])

for i in lady_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])

for i in harry_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])

for i in post_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])

for i in rihanna_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])

for i in elton_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])

for i in madonna_json_data['response']['hits']:
    song_title_list.append(i['result']['title'])
    annotation_list.append(i['result']['annotation_count'])
    
    
# fig = plt.figure()
fig = plt.figure(figsize=(16,8))
plt.bar(song_title_list, annotation_list, align = "center", color = ["lightgreen"])
plt.xticks(rotation=90)                                                                                                
plt.xlabel("Song Title")
plt.ylabel("Annotation Count")
spacing = 0.400
fig.subplots_adjust(bottom=spacing)
plt.title("Annotation Count of 10 Songs from 10 Artists")
plt.savefig("pageviews.png")
plt.tight_layout()
plt.show()