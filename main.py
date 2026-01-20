class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, name, duration):
        self.songs.append(duration)

    def total_duration(self):
        return sum(self.songs)

playlist = Playlist()
playlist.add_song("Song 1", 210)
playlist.add_song("Song 2", 180)

print("Jami sekund:", playlist.total_duration())
