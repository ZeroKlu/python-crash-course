"""Module to create and populate a trie"""

from pathlib import Path
from sm_utils import file_path, timer
from trie_node import TrieNode

class Trie:
    """Models a trie (alphabet only)"""

    def __init__(self, size: int=26, base_char: str="a") -> None:
        """Initialize"""
        self.size = size
        self.root = TrieNode(self.size)
        self.offset = ord(base_char)

    def insert(self, key: str) -> None:
        """Insert a string into the trie"""
        current_node = self.root
        for c in key.lower():
            index = ord(c) - self.offset
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(self.size)
            current_node = current_node.children[index]
        current_node.word_end = True

    def prefix_exists(self, key: str) -> bool:
        """Check if prefix exists in the trie"""
        current_node = self.root
        for c in key.lower():
            if current_node.children[ord(c) - self.offset] is None:
                return False
            current_node = current_node.children[ord(c) - self.offset]
        return True

    @timer
    def search(self, key: str) -> bool:
        """Check if word exists in the trie"""
        current_node = self.root
        for c in key.lower():
            if current_node.children[ord(c) - self.offset] is None:
                return False
            current_node = current_node.children[ord(c) - self.offset]
        return current_node.word_end

    def delete(self, key: str) -> bool:
        """Remove word from trie"""
        current_node = self.root
        last_branch_node = None
        last_branch_char = "a"
        for c in key.lower():
            if current_node.children[ord(c) - self.offset] is None:
                return False
            count = 0
            for i in range(26):
                if current_node.children[i] is not None:
                    count += 1
            if count > 1:
                last_branch_node = current_node
                last_branch_char = c
            current_node = current_node.children[ord(c) - self.offset]
        count = 0
        for i in range(26):
            if current_node.children[i] is not None:
                count += 1
        if count > 0:
            current_node.word_end = False
            return True
        if last_branch_node is not None:
            last_branch_node.children[ord(last_branch_char) - self.offset] = None
            return True
        self.root.children[ord(key[0]) - self.offset] = None
        return True

    def load_words(self, file_name: str, folder: str = None) -> None:
        """Load words from a file into the trie"""
        words = Path(file_path(file_name, folder)).read_text(encoding="UTF-8").splitlines()
        for word in words:
            self.insert(word)
