def pause(end: bool=False) -> None:
    """Wait for user input"""
    act = "end program" if end else "continue"
    input(f"Press <ENTER> to {act}...")
    if end: quit()

def clear_terminal(end: str="") -> None:
    """Clear the terminal"""
    print("\033c", end=end)