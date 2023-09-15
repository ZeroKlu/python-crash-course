from node import Node
from range_char import range_char

class Morse:
    """Implement a Morse code encoder/decoder using a binary tree"""

    def __init__(self):
        """Initialize the Morse code tree"""
        self.tree = Node(None)
        self.tree.left = Node("E")
        self.tree.left.left = Node("I")
        self.tree.left.left.left = Node("S")
        self.tree.left.left.left.left = Node("H")
        self.tree.left.left.left.right = Node("V")
        self.tree.left.left.right = Node("U")
        self.tree.left.left.right.left = Node("F")
        self.tree.left.right = Node("A")
        self.tree.left.right.left = Node("R")
        self.tree.left.right.left.left = Node("L")
        self.tree.left.right.right = Node("W")
        self.tree.left.right.right.left = Node("P")
        self.tree.left.right.right.right = Node("J")
        self.tree.right = Node("T")
        self.tree.right.left = Node("N")
        self.tree.right.left.left = Node("D")
        self.tree.right.left.left.left = Node("B")
        self.tree.right.left.left.right = Node("X")
        self.tree.right.left.right = Node("K")
        self.tree.right.left.right.left = Node("C")
        self.tree.right.left.right.right = Node("Y")
        self.tree.right.right = Node("M")
        self.tree.right.right.left = Node("G")
        self.tree.right.right.left.left = Node("Z")
        self.tree.right.right.left.right = Node("Q")
        self.tree.right.right.right = Node("O")

        # Missing-link nodes for numerals
        self.tree.right.right.right.right = Node(None)
        self.tree.left.left.right.right = Node(None)
        self.tree.right.right.right.left = Node(None)

        # Include numerals
        self.tree.left.right.right.right.right = Node("1")
        self.tree.left.left.right.right.right = Node("2")
        self.tree.left.left.left.right.right = Node("3")
        self.tree.left.left.left.left.right = Node("4")
        self.tree.left.left.left.left.left = Node("5")
        self.tree.right.left.left.left.left = Node("6")
        self.tree.right.right.left.left.left = Node("7")
        self.tree.right.right.right.left.left = Node("8")
        self.tree.right.right.right.right.left = Node("9")
        self.tree.right.right.right.right.right = Node("0")

        # Missing-link nodes for punctuation
        self.tree.left.right.left.right = Node(None)
        self.tree.left.right.left.right.left = Node(None)
        self.tree.right.right.left.left.right = Node(None)
        self.tree.left.left.right.right.left = Node(None)
        self.tree.right.left.right.left.right = Node(None)
        self.tree.left.right.left.left.right = Node(None)

        # Include punctuation
        self.tree.left.right.left.right.left.right = Node(".")
        self.tree.right.right.left.left.right.right = Node(",")
        self.tree.left.left.right.right.left.left = Node("?")
        self.tree.right.left.right.left.right.left = Node(";")
        self.tree.right.right.right.left.left.left = Node(":")
        self.tree.right.left.left.left.left.right = Node("-")
        self.tree.right.left.left.right.left = Node("/")
        self.tree.left.right.right.right.right.left = Node("'")
        self.tree.left.right.left.left.right.left = Node("\"")
        self.tree.right.left.right.left.right.right = Node("!")
        self.tree.right.left.left.left.right = Node("--")
        self.tree.right.left.right.right.left = Node("(")
        self.tree.right.left.right.right.left.right = Node(")")
        self.tree.left.left.right.right.left.right = Node("_")

    def decode(self, encoded, delimiter = " ", separator = "_"):
        """Decode Morse code to letters"""
        encoded_words = encoded.split(separator)
        decoded_words = []
        for word in encoded_words:
            encoded_chars = word.strip().split(delimiter)
            decoded = []
            for e in encoded_chars:
                node = self.tree
                for n in e:
                    assert n in [".", "-"]
                    node = node.left if n == "." else node.right
                decoded.append(node.value)
            decoded_words.append("".join(decoded))
        result = ""
        for word in decoded_words:
            if len(result) > 0: result += " "
            result += word
        return result

    def encode(self, message, delimiter = " ", invalid_char_sub = "□", space_char_sub = "■"):
        """Encode letters to Morse code"""
        morse = ""
        for character in message.upper():
            valid_chars = list(range_char("A", "Z"))
            for i in range(0, 10): valid_chars.append(str(i))
            valid_chars.extend([".", ",", "?", ";", ":", "-", "/", "'", "\"", "!", "--", "(", ")", "_"])
            if character not in valid_chars:
                code = space_char_sub if character == " " else invalid_char_sub
            else:
                encoded = []
                self.get_code(self.tree, character, encoded)
                code = "".join(encoded)
            if len(morse) > 0: morse += delimiter
            morse += code
        return morse.replace(" " + invalid_char_sub + " ", invalid_char_sub).replace(" " + space_char_sub + " ", space_char_sub)

    def get_code(self, node, character, code):
        """Traverse tree to obtain morse for character"""
        if node == None:
            return False
        elif node.value == character:
            return True
        else:
            if self.get_code(node.left, character, code):
                code.insert(0, ".")
                return True
            elif self.get_code(node.right, character, code):
                code.insert(0, "-")
                return True
            return False
