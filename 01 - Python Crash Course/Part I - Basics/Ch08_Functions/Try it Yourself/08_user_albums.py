# Assignment 8.8
# User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album's
#              artist and title. Once you have that information, call make_album() with the user's input and print
#              the dictionary that's created. Be sure to include a quit value in the while loop.

print("Try-it-Yourself:")
print("Assignment 8.8")


def make_album(artist, album, songs=None):
    """Return a dictionary describing a music album"""
    album = {"Artist": artist.title(), "Title": album.title()}
    if songs:
        album["Tracks"] = songs
    return album


while True:
    print("\nPlease tell me about your album:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == "q":
        break

    title = input("Album Title: ")
    if title == "q":
        break

    album = make_album(artist, title)
    print(f"\n{album}!")
