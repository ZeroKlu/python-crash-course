from sm_utils import clear_terminal
from relative_paths import get_path
from pathlib import Path

def get_bitmap() -> str:
    """Obtain the bitmap ASCII pattern from file"""
    bitmap_path = get_path("bitmap_world.txt", "data")
    file_path = Path(bitmap_path)
    return file_path.read_text().rstrip()

def draw_bitmap(word: str, bitmap: str, boundary: str=".") -> None:
    """Draw the ASCII bitmap on screen"""
    clear_terminal()
    lines = bitmap.splitlines()
    for line in lines:
        for i in range(len(line)):
            tail = "\n" if i == len(line) - 1 else ""
            if line[i] == " ":
                print(" ", end=tail)
            elif line[i] == boundary:
                print(boundary, end=tail)
            else:
                print(word[i % len(word)], end=tail)

def do_bitmap() -> None:
    """Get a string from the user and overlay it on the ASCII bitmap"""
    clear_terminal()
    word = input("Enter a word, and I will use it to draw a world map:\n> ")
    if word is None or word.strip() == "":
        print("Cannot draw map without a word!")
        return
    bitmap = get_bitmap()
    draw_bitmap(word, bitmap)

def main() -> None:
    do_bitmap()

if __name__ == "__main__":
    main()
