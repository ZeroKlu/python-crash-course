from relative_paths import get_path
from pathlib import Path
import json

def get_settings(file: str="settings.json", folder: str="files") -> dict[str, str]:
    """Get settings dictionary from JSON file"""
    return json.loads(Path(get_path(file, folder)).read_text())

def pause(end: bool=False) -> None:
    """Wait for user input"""
    act = "end program" if end else "continue"
    input(f"Press <ENTER> to {act}...")
    if end: quit()

def clear_terminal(end: str="") -> None:
    """Clear the terminal"""
    print("\033c", end=end)