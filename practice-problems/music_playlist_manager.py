playlist = ["Believer", "Shape of You", "Tum Hi Ho"]

print("===== My Playlist =====")

for song in playlist:
    print(song)

new_song = input("\nEnter a song to add: ")

if new_song in playlist:
    print("Song already exists in playlist 🎵")

else:
    playlist.append(new_song)
    print("Song added successfully ")

print("\nUpdated Playlist:")

for song in playlist:
    print(song)