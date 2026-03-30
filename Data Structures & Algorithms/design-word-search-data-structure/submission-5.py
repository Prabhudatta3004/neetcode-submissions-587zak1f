class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = TrieNode()
            curr_node = curr_node.children[ch]
        curr_node.flag = True

    def search(self, word: str) -> bool:
        
        # Define the helper inside so it can access 'word' easily
        def dfs(node, index):
            # Base Case: If we run out of characters, check if we marked a word end here
            if index == len(word):
                return node.flag
            
            ch = word[index]

            if ch == ".":
                # === THE PART YOU ASKED ABOUT ===
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
                # ================================
            
            else:
                # Standard check: if char not found, stop. Else, keep going.
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], index + 1)

        # Start the recursion from the root
        return dfs(self.root, 0)
