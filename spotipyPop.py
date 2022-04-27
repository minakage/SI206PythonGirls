import os
import sys
import spotipy
import sqlite3
import webbrowser
import numpy as np

import sqlite3
import urllib.request, urllib.parse, urllib.error
import spotipy.util as util
import spotipy.util as util
import matplotlib
import matplotlib.pyplot as plt

username = "miainakage@msn.com"
scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope, client_id='e192483549944492a872412ca0106029', client_secret='35790b625ce542929b76fbfb4bcd5d10', redirect_uri='http://localhost:8888/callback')
spotify = spotipy.Spotify(auth = token)



def total_list_songs_popularity():
    olivia_rodrigo_uri = 'spotify:artist:1McMsnEElThX1knmY4oliG'
    artist_data = spotify.artist_top_tracks(olivia_rodrigo_uri)
    popularity_list = []
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 1
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))
    
    bazzi_uri = 'spotify:artist:4GvEc3ANtPPjt1ZJllr5Zl'
    artist_data = spotify.artist_top_tracks(bazzi_uri)
    for song in artist_data['tracks'][:11]:
        artist_id = 2
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))

    billie_eilish_uri = 'spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH'
    artist_data = spotify.artist_top_tracks(billie_eilish_uri)
    for song in artist_data['tracks'][:11]:
        artist_id = 3
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))

    mac_miller_uri = 'spotify:artist:4LLpKhyESsyAXpc4laK94U'
    artist_data = spotify.artist_top_tracks(mac_miller_uri)
    for song in artist_data['tracks'][:11]:
        artist_id = 4
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))


    lady_gaga_uri = 'spotify:artist:1HY2Jd0NmPuamShAr6KMms'
    artist_data = spotify.artist_top_tracks(lady_gaga_uri)
    for song in artist_data['tracks'][:11]:
        artist_id = 5
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))

    harry_styles_uri = 'spotify:artist:6KImCVD70vtIoJWnq6nGn3'
    artist_data = spotify.artist_top_tracks(harry_styles_uri)
    for song in artist_data['tracks'][:11]:
        artist_id = 6
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))
        
    post_malone_uri = 'spotify:artist:246dkjvS1zLTtiykXe5h60'
    artist_data = spotify.artist_top_tracks(post_malone_uri)
    for song in artist_data['tracks'][:11]:
        artist_id = 7
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))

    rihanna_uri = 'spotify:artist:5pKCCKE2ajJHZ9KAiaK11H'
    artist_data = spotify.artist_top_tracks(rihanna_uri)
    for song in artist_data['tracks'][:11]:
        artist_id = 8
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))

    elton_john_uri = 'spotify:artist:3PhoLpVuITZKcymswpck5b'
    artist_data = spotify.artist_top_tracks(elton_john_uri)
    for song in artist_data['tracks'][:11]:
        artist_id = 9
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))

    madonna_uri = 'spotify:artist:6tbjWDEIzxoDsBA1FuhfPW'
    artist_data = spotify.artist_top_tracks(madonna_uri)
    for song in artist_data['tracks'][:11]:
        artist_id = 10
        song_title = song['name']
        popularity = song['popularity']
        popularity_list.append((artist_id, song_title, popularity))
    
    conn = sqlite3.connect('PythonGirls.db')
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISTS Spotipy (artist_id INTEGER, song VARCHAR NOT NULL PRIMARY KEY UNIQUE, popularity INTEGER)')
    conn.commit()
    cur.execute('SELECT * FROM Spotipy')
    data = cur.fetchall()
    if len(data) < 75:
        for item in popularity_list[len(data):len(data) + 25]:
            cur.execute('INSERT OR IGNORE INTO Spotipy (artist_id, song, popularity) VALUES (?,?,?)''', (item[0], item[1], item[2]))
        conn.commit()
    elif len(data) >= 75:
        for item in popularity_list[len(data):]:
            cur.execute('INSERT OR IGNORE INTO Spotipy (artist_id, song, popularity) VALUES (?,?,?)''', (item[0], item[1], item[2]))
        conn.commit()


   
    
	# This accesses the necessary column in the database
    data = cur.execute(""" SELECT popularity FROM Spotipy WHERE artist_id='1' """)
    olivia_total = 0
	# This iterates through the rows to add popularity values and divide by number of times the singer appears in the database
    for row in data:
        olivia_total += (row[0])
    olivia_total = olivia_total / 10
    print(olivia_total)


    data = cur.execute(""" SELECT popularity FROM Spotipy Popularity WHERE artist_id='2' """)
    bazzi_total = 0
	# This iterates through the rows to add total fame values and divide by number of times the singer appears in the database
    for row in data:
        bazzi_total += (row[0])
    bazzi_total = bazzi_total / 10
    print(bazzi_total)

       
    data = cur.execute(""" SELECT popularity FROM Spotipy WHERE artist_id='3' """)
    billie_total = 0
	# This iterates through the rows to add total fame values and divide by number of times the singer appears in the database
    for row in data:
        billie_total += (row[0])
    billie_total = billie_total / 10
    print(billie_total)

    data = cur.execute(""" SELECT popularity FROM Spotipy WHERE artist_id='4' """)
    mac_total = 0
	# This iterates through the rows to add total fame values and divide by number of times the singer appears in the database
    for row in data:
        mac_total += (row[0])
    mac_total = mac_total / 10
    print(mac_total)

    data = cur.execute(""" SELECT popularity FROM Spotipy WHERE artist_id='5' """)
    gaga_total = 0
	# This iterates through the rows to add total fame values and divide by number of times the singer appears in the database
    for row in data:
        gaga_total += (row[0])
    gaga_total = gaga_total / 10
    print(gaga_total)

    data = cur.execute(""" SELECT popularity FROM Spotipy WHERE artist_id='6' """)
    harry_total = 0
	# This iterates through the rows to add total fame values and divide by number of times the singer appears in the database
    for row in data:
        harry_total += (row[0])
    harry_total = harry_total / 10
    print(harry_total)

    data = cur.execute(""" SELECT popularity FROM Spotipy WHERE artist_id='7' """)
    post_total = 0
	# This iterates through the rows to add total fame values and divide by number of times the singer appears in the database
    for row in data:
        post_total += (row[0])
    post_total = post_total / 10
    print(post_total)

    data = cur.execute(""" SELECT popularity FROM Spotipy WHERE artist_id='8' """)
    rihanna_total = 0
	# This iterates through the rows to add total fame values and divide by number of times the singer appears in the database
    for row in data:
        rihanna_total += (row[0])
    rihanna_total = rihanna_total / 10
    print(rihanna_total)


    data = cur.execute(""" SELECT popularity FROM Spotipy WHERE artist_id='9' """)
    elton_total = 0
	# This iterates through the rows to add total fame values and divide by number of times the singer appears in the database
    for row in data:
        elton_total += (row[0])
    elton_total = elton_total / 10
    print(elton_total)

    data = cur.execute(""" SELECT popularity FROM Spotipy WHERE artist_id='10' """)
    madonna_total = 0
	# This iterates through the rows to add total fame values and divide by number of times the singer appears in the database
    for row in data:
        madonna_total += (row[0])
    madonna_total = madonna_total / 10
    print(madonna_total)


  
    #creating txt file for all of the averages of top 10 popular songs from each artist
    with open("popularityValues.txt", 'w') as f:
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Olivia Rodrigo', olivia_total))
        f.write('\n')
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Bazzi', bazzi_total))
        f.write('\n')
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Billie Eilish', billie_total))
        f.write('\n')
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Mac Miller', mac_total))
        f.write('\n')
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Lady Gaga', gaga_total))
        f.write('\n')
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Harry Styles', harry_total))
        f.write('\n')
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Post Malone', post_total))
        f.write('\n')
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Rihanna', rihanna_total))
        f.write('\n')
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Elton John', elton_total))
        f.write('\n')
        f.write("{} has an average popularity of {} from their top ten songs on Spotify".format('Madonna', madonna_total))
        f.write('\n')

    
    x = (olivia_total, bazzi_total, billie_total, mac_total, gaga_total, harry_total, post_total, rihanna_total, elton_total, madonna_total)
    y = ("Olivia Rodrigo", "Bazzi", "Billie Eilish", "Mac Miller", "Lady Gaga", "Harry Styles", "Post Malone", "Rihanna", "Elton John", "Madonna")

    plt.barh(y, x, align = "center", color = ["maroon",
                                                                "brown",
                                                                "indianred",
                                                                "darksalmon",
                                                                "lightcoral",
                                                                "lightpink",
                                                                "hotpink",
                                                                "palevioletred",
                                                                "mediumvioletred",
                                                                "darkmagenta"])
                                                                
                                                                
    plt.ylabel("Artist Name")
    plt.xlabel("Average Popularity")
    plt.title("Avg Popularity of Top 10 Songs from 10 Artists from Spotify")
    plt.savefig("artist_popularity.png")
    plt.tight_layout()
    plt.show()









#function for duration in ms value
def total_list_songs_duration_ms():
    olivia_rodrigo_uri = 'spotify:artist:1McMsnEElThX1knmY4oliG'
    artist_data = spotify.artist_top_tracks(olivia_rodrigo_uri)
    duration_ms_list = []
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 1
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))
    
    bazzi_uri = 'spotify:artist:4GvEc3ANtPPjt1ZJllr5Zl'
    artist_data = spotify.artist_top_tracks(bazzi_uri)
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 2
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))

    billie_eilish_uri = 'spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH'
    artist_data = spotify.artist_top_tracks(billie_eilish_uri)
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 3
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))

    mac_miller_uri = 'spotify:artist:4LLpKhyESsyAXpc4laK94U'
    artist_data = spotify.artist_top_tracks(mac_miller_uri)
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 4
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))


    lady_gaga_uri = 'spotify:artist:1HY2Jd0NmPuamShAr6KMms'
    artist_data = spotify.artist_top_tracks(lady_gaga_uri)
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 5
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))

    harry_styles_uri = 'spotify:artist:6KImCVD70vtIoJWnq6nGn3'
    artist_data = spotify.artist_top_tracks(harry_styles_uri)
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 6
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))
        
    post_malone_uri = 'spotify:artist:246dkjvS1zLTtiykXe5h60'
    artist_data = spotify.artist_top_tracks(post_malone_uri)
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 7
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))

    rihanna_uri = 'spotify:artist:5pKCCKE2ajJHZ9KAiaK11H'
    artist_data = spotify.artist_top_tracks(rihanna_uri)
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 8
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))

    elton_john_uri = 'spotify:artist:3PhoLpVuITZKcymswpck5b'
    artist_data = spotify.artist_top_tracks(elton_john_uri)
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 9
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))

    madonna_uri = 'spotify:artist:6tbjWDEIzxoDsBA1FuhfPW'
    artist_data = spotify.artist_top_tracks(madonna_uri)
    for song in artist_data['tracks'][:11]:
        artist_name = song['artists'][0]['name']
        artist_id = 10
        song_title = song['name']
        duration_ms = song['duration_ms']
        duration_ms_list.append((artist_id, song_title, duration_ms))
    
    conn = sqlite3.connect('PythonGirls.db')
    cur = conn.cursor()


    cur.execute('CREATE TABLE IF NOT EXISTS Spotipy2 (artist_id INTEGER, song VARCHAR NOT NULL PRIMARY KEY UNIQUE, duration_ms INTEGER)')
    conn.commit()
    cur.execute('SELECT * FROM Spotipy2')
    data = cur.fetchall()
    if len(data) < 75:
        for item in duration_ms_list[len(data):len(data) + 25]:
            cur.execute('INSERT OR IGNORE INTO Spotipy2 (artist_id, song, duration_ms) VALUES (?,?,?)''', (item[0], item[1], item[2]))
        conn.commit()
    elif len(data) >= 75:
        for item in duration_ms_list[len(data):]:
            cur.execute('INSERT OR IGNORE INTO Spotipy (artist_id, song, duration_ms) VALUES (?,?,?)''', (item[0], item[1], item[2]))
        conn.commit()


    song_title_list = []
    duration_list = []
    for i in duration_ms_list:
        song_title_list.append(i[1])
        duration_list.append(i[2])
    
    # fig = plt.figure()
    fig = plt.figure(figsize=(16,8))
    plt.bar(song_title_list, duration_list, align = "center", color = ["hotpink"])
    plt.xticks(rotation=90)                                                                                                
    plt.xlabel("Song Title")
    plt.ylabel("Duration (ms)")
    spacing = 0.400
    fig.subplots_adjust(bottom=spacing)
    plt.title("Duration of 100 Songs in Milliseconds")


    plt.savefig("song_duration.png")
    plt.tight_layout()
    plt.show()






if __name__ == "__main__":
   
    conn = sqlite3.connect('PythonGirls.db')
    cur = conn.cursor()
   
    total_list_songs_popularity()
    total_list_songs_duration_ms()