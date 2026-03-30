class Trie:
    def __init__(self):
        self.reference = [None] * 26
        self.endflag = False
class PrefixTree:

    def __init__(self):
        self.root = Trie() ## At first we need to create the trie
        ## for root node

    def insert(self, word: str) -> None:
        ## Insert function starts from root
        current_node = self.root
        ## THen checks if the character is present or not
        for w in word:
            i = ord(w) - ord('a')
            if current_node.reference[i] == None: ## Char is not present
                current_node.reference[i] = Trie() ## creating a new trie object for the character
            current_node = current_node.reference[i]  ## moving to the new char reference node
        current_node.endflag = True ## Setting the last bool flag to be true

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            i  = ord(w) - ord('a')
            if curr.reference[i] == None:
                return False
            curr = curr.reference[i]
        return curr.endflag
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for p in prefix:
            i = ord(p) - ord('a')
            if curr.reference[i] == None:
                return False
            curr = curr.reference[i]
        return True        
        