"""Models a node in a trie"""

# pylint: disable=too-few-public-methods
class TrieNode:
    """Models a node in a trie"""

    #region Constructors
    def __init__(self, size: int=26) -> None:
        """Initialize"""
        # Size determines the number of characters able to be tracked per node
        self.children = [None] * size
        # Number of strings stored from the root to this node
        self.word_count = 0
    #endregion
