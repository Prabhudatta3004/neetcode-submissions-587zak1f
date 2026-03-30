class TrieNode:
    def __init__(self):
        self.children = {} 
        self.flag = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = TrieNode()
            curr_node = curr_node.children[ch]
        curr_node.flag = True


    def search(self, word: str) -> bool:
        curr_node = self.root
        for ch in word:
            if ch not in curr_node.children:
                return False
            curr_node = curr_node.children[ch]
        return curr_node.flag

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for ch in prefix:
            if ch not in curr_node.children:
                return False
            curr_node = curr_node.children[ch]
        return True
        