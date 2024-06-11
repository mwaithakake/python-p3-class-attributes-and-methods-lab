from song import Song


def test_song_initialization():
    song = Song("99 Problems", "Jay-Z", "Rap")
    assert song.name == "99 Problems"
    assert song.artist == "Jay-Z"
    assert song.genre == "Rap"

def test_song_count():
    assert Song.count == 1

def test_song_genres():
    assert Song.genres == ["Rap"]

def test_song_artists():
    assert Song.artists == ["Jay-Z"]

def test_song_genre_count():
    assert Song.genre_count == {"Rap": 1}

def test_song_artist_count():
    assert Song.artist_count == {"Jay-Z": 1}