import sys, os, json

"""Default folder for accessing files"""
default_path: str|None=None

def root_path() -> str:
    """Return the root execution path of the script"""
    return os.path.dirname(sys.argv[0])

def set_path(folder: str|None=None) -> str:
    """Set the default folder for accessing files"""
    if folder: return folder
    json_path = os.path.join(root_path(), "sm_utils.json")
    if not os.path.isfile(json_path): return "data"
    with open(json_path) as f:
        data = json.load(f)
    global default_path
    default_path = data["default_path"]
    return data["default_path"]

set_path()

def dir_path(folder_path: str=default_path) -> str:
    """Return the specified path under the root directory"""
    if not folder_path: return root_path()
    return os.path.join(root_path(), folder_path)

def file_path(filename: str, folder_path: str = default_path) -> str:
    """Return the specified complete file path"""
    return os.path.join(dir_path(folder_path), filename)

def pause(line: bool=True, end: bool=False) -> None:
    """Wait for user input"""
    act = "end program" if end else "continue"
    if line: print()
    input(f"Press <ENTER> to {act}...")
    if end: quit()

def clear_terminal(end: str="") -> None:
    """Clear the terminal"""
    print("\033c", end=end)