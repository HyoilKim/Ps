# '#' 속성으로 메모리 공간 절약
class Trie:
    def __init__(self):
        self.children = dict()

    def insert(self, word: str):
        node = self.children
        for ch in word:
            if ch not in node:
                node[ch] = dict()
            node = node[ch]
        node['#'] = True

    def search(self, word: str):
        node = self.children
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return '#' in node

    def startsWith(self, prefix: str):
        node = self.children
        for ch in prefix:
            if not ch in node:
                return False
            node = node[ch]
        return True

# TrieNode 생성하여 root 고정 및 word 속성으로 존재 여부 판단
class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.word=False
            self.children={}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
        node.word=True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                return False
            node=node.children[i]
        return node.word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node=self.root
        for i in prefix:
            if i not in node.children:
                return False
            node=node.children[i]
        return True
        