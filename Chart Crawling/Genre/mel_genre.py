import requests
from bs4 import BeautifulSoup

while True:
    genre = input("Enter music genre (Ballad, Dance, Hip-Hop, R&B, Indie, Rock, Trot, Folk): ")
    count = 0

    if genre == "Ballad":
        gnrCode = "GN0100"
        break
    elif genre == "Dance":
        gnrCode = "GN0200"
        break
    elif genre == "Hiphop":
        gnrCode = "GN0300"
        break
    elif genre == "R&B":
        gnrCode = "GN0400"
        break
    elif genre == "Indie":
        gnrCode = "GN0500"
        break
    elif genre == "Rock":
        gnrCode = "GN0600"
        break
    elif genre == "Trot":
        gnrCode = "GN0700"
        break
    elif genre == "Folk":
        gnrCode = "GN0800"
        break
    else:
        print("Please re-enter the genre.")

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
melon_url = "https://www.melon.com/genre/song_list.htm?gnrCode=" + gnrCode
raw = requests.get(melon_url, headers=header)
soup = BeautifulSoup(raw.text, "html.parser")

box = soup.find("tbody")

all_singer = box.find_all("div", {"class": "ellipsis rank02"})
all_title = box.find_all("div", {"class": "ellipsis rank01"})

print("Top 50 of " + genre)

file = open("mel_genre_folk_top50.txt", "w", -1, "UTF-8")

for singer, title in zip(all_singer, all_title):
    count += 1
    data = (str(count) + ". " + title.find("a").text + " - " + singer.find("a").text)
    file.write(data + "\n")
file.close()
