import json

class Thing:
    """Models some thing"""

    def __init__(self, size: str, color: str) -> None:
        """Initialize the class attributes"""
        self.size = size
        self.color = color

def main():
    """Testing Function"""
    thing = Thing("Large", "Blue")
    # The __dict__ object is built-in on every class and returns a dictionary of the class attributes
    thing_attributes = thing.__dict__

    # This can be useful when serializing a class to JSON

    # This would return an error: TypeError: Object of type Thing is not JSON serializable
    # print(json.dumps(thing, indent=4))

    # Since json.dumps() expects a dictionary as its argument, this will work
    print(json.dumps(thing.__dict__, indent=4))

if __name__ == "__main__":
    main()
