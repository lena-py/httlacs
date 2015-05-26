__author__ = 'lena'

song = "The rain in Spain"
wds = song.split("ai")
print(wds)

wds = ["This", "is", "the", "song", "that", "doesn't", "end"]
song = ";"
song = song.join(wds)
print(song)
print(wds)
print("***".join(wds))
print(" ".join(wds))