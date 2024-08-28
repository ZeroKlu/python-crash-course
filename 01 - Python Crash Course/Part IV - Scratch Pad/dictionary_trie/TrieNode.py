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

#region Source Code Information
#######################################################################
#                  Copyright (C) 2024, DataBank IMX                   #
#                                                                     #
# Source code provided for reference only! Reuse not permitted!       #
#######################################################################
#endregion
