class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.flag = True

    def search(self, word: str) -> bool:
        
        def dfs(node,index):
            if index == len(word):
                return node.flag
            
            character = word[index]

            if character == ".":
                for ch in node.children.values():
                    if dfs(ch,index+1):
                        return True
                
                return False
            else:
                if character not in node.children:
                    return False
                return dfs(node.children[character],index+1)
        return dfs(self.root,0)
