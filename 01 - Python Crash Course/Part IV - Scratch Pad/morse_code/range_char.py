"""Utility function to generate a range of characters"""

def range_char(start, stop):
    """Generate a range of characters"""
    return (chr(n) for n in range(ord(start), ord(stop) + 1))
