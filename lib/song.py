class Song:
    genre_count = {}
    artist_count = {}  # Added artist_count dictionary
    count = 0

    def __init__(self, name, genre, artist):
        self.name = name
        self.genre = genre
        self.artist = artist
        self.add_song_to_count()
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Example usage:
song1 = Song("Song A", "Rap", "Artist X")
song2 = Song("Song B", "Rock", "Artist Y")
song3 = Song("Song C", "Country", "Artist X")
song4 = Song("Song D", "Rap", "Artist Z")

print("Genre Count:", Song.genre_count)
print("Artist Count:", Song.artist_count)
print("Total Count:", Song.count)
  