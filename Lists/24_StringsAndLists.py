__author__ = 'lena'

# Split method creates list from string
song = "The rain in Spain"
wds = song.split()
print(wds)

# Optional delimiter (default is " ")
wds = song.split('ai')
print(wds)

# Join method creates str from lst
wds = ["This", "is", "the", "song", "that", "doesn't", "end"]
song = " "
song = song.join(wds)
print(song)

# Shorthand methods
newsong = " ".join(wds) + " NEW "
print(newsong)

# Any "glue" may be used
print("***".join(wds))
