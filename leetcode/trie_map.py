class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_leaf = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        pointer = self.root
        for level in range(len(key)):
            if key[level] not in pointer.children:
                pointer.children[key[level]] = TrieNode()
            pointer = pointer.children[key[level]]

        pointer.is_leaf = True

    def search(self, key):
        pointer = self.root
        for level in range(len(key)):
            if key[level] not in pointer.children:
                return False
            pointer = pointer.children[key[level]]

        return pointer and pointer.is_leaf


def main():

    trie = Trie()
    trie.insert("car")
    trie.insert("curve")
    trie.insert("code")

    print(trie.search("car"))
    print(trie.search("cat"))
    print(trie.search("ca"))
    print(trie.search("code"))
    print(trie.search("codec"))


if __name__ == '__main__':
    main()


