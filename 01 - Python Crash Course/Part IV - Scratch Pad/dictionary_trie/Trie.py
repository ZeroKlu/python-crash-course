#region Copyright
#######################################################################
#                  Copyright (C) 2024, DataBank IMX                   #
#                                                                     #
# All rights reserved                                                 #
#                                                                     #
# For further information consult:                                    #
#  - The DataBank IMX End User License Agreement (EULA)               #
#    or                                                               #
#  - DataBank IMX Intellectual Property Statement                     #
#                                                                     #
# Above referenced documents available upon request from:             #
#     development@databankimx.com                                     #
#                                                                     #
#######################################################################
#endregion

#region Imports
from pathlib import Path
from sm_utils import file_path, timer
from TrieNode import TrieNode
#endregion

class Trie:
    """Models a trie (alphabet only)"""

    #region Constructors
    def __init__(self, size: int=26) -> None:
        """Initialize"""
        self.size = size
        self.root = TrieNode(self.size)
    #endregion
    
    #region Methods
    def insert_key(self, key: str) -> None:
        """Insert a string into the trie"""
        current_node = self.root
        for c in key.lower():
            if current_node.children[ord(c) - ord("a")] is None:
                current_node.children[ord(c) - ord("a")] = TrieNode(self.size)
            current_node = current_node.children[ord(c) - ord("a")]
        current_node.word_count += 1

    def prefix_exists(self, key: str) -> bool:
        """Check if prefix exists in the trie"""
        current_node = self.root
        for c in key.lower():
            if current_node.children[ord(c) - ord("a")] is None:
                return False
            current_node = current_node.children[ord(c) - ord("a")]
        return True

    @timer
    def search(self, key: str) -> bool:
        """Check if word exists in the trie"""
        current_node = self.root
        for c in key.lower():
            if ord(c) - ord("a") < 0:
                return False
            if current_node.children[ord(c) - ord("a")] is None:
                return False
            current_node = current_node.children[ord(c) - ord("a")]
        return current_node.word_count > 0

    def delete(self, key: str) -> bool:
        """Remove word from trie"""
        current_node = self.root
        last_branch_node = None
        last_branch_char = "a"
        for c in key.lower():
            if current_node.children[ord(c) - ord("a")] is None:
                return False
            count = 0
            for i in range(26):
                if current_node.children[i] is not None:
                    count += 1
            if count > 1:
                last_branch_node = current_node
                last_branch_char = c
            current_node = current_node.children[ord(c) - ord("a")]
        count = 0
        for i in range(26):
            if current_node.children[i] is not None:
                count += 1
        if count > 0:
            current_node.word_count -= 1
            return True
        if last_branch_node is not None:
            last_branch_node.children[ord(last_branch_char) - ord("a")] = None
            return True
        self.root.children[ord(key[0]) - ord("a")] = None
        return True
    
    def load_words(self, file_name: str, folder: str = None) -> None:
        words = Path(file_path(file_name, folder)).read_text().split("\n")
        for word in words:
            self.insert_key(word)
    #endregion

#region Source Code Information
#######################################################################
#                  Copyright (C) 2024, DataBank IMX                   #
#                                                                     #
# Source code provided for reference only! Reuse not permitted!       #
#######################################################################
#endregion
