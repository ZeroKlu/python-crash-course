def make_album(artist, album, songs = None):
    album = {"Artist": artist.title(), "Title": album.title()}
    if songs:
        album["Tracks"] = songs
    return album
