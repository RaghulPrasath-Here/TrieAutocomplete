from collections import defaultdict

class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.isEnd = False

    def __str__(self):
        return f"value : {self.value}, children : {list(self.children.keys())}"
    
class Trie:
    def __init__(self):
        self.startNode = TrieNode(" ")

    def insert(self, word: str) -> None:
        currentNode = self.startNode
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                node = TrieNode(c)
                currentNode.children[c] = node
                currentNode = node
        
        currentNode.isEnd = True

    def search(self, word: str) -> bool:
        currentNode = self.startNode
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                return False

        return currentNode.isEnd

    def startsWith(self, prefix: str) -> object:
        currentNode = self.startNode
        for c in prefix:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                return None
        
        return currentNode

if __name__ == "__main__":

    def dfs(node, string, result):
        if node.isEnd:
            result.append(string)
                  
        if len(node.children) == 0:
            return

        for child in node.children.values():
            dfs(child, string + child.value, result)

    words = []
    searchedWords = {}

    with open('words.txt', 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()          
            if word:                    
                words.append(word)

    # initializing trie 
    trie = Trie()

    for word in words:
        trie.insert(word)
    
    while True:
        searchString = input("Enter a word to see all the words that starts with it : ")
        
        node = trie.startsWith(searchString)
        result = []
        if node:
            dfs(node, searchString, result)
        
        currentWordsCount = {}

        for word in result:
            if word not in searchedWords:
                currentWordsCount[word] = 0
            else:
                currentWordsCount[word] = searchedWords[word]
        
        currentWordsCount = sorted(currentWordsCount.items(), key=lambda item: item[1], reverse=True)
        currentWordsCount = currentWordsCount[0:10]
        
        print(f"\nWords that start with {searchString}")
        print("\nChoose a word from the below list you want to search (1 for the 1st word)")
        print(currentWordsCount)

        choice = int(input())

        searchedWords[str(currentWordsCount[choice - 1][0])] = currentWordsCount[choice - 1][1] + 1

        print(searchedWords)

        end = input("Stop searching? y or n: ").strip().lower()
        if end == "y":
            break