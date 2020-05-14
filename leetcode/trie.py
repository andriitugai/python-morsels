class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.is_leaf = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def _get_char_index(char):
        return ord(char) - ord('a')

    def insert(self, key):
        pointer = self.root
        for level in range(len(key)):
            index = self._get_char_index(key[level])
            if not pointer.children[index]:
                pointer.children[index] = TrieNode()
            pointer = pointer.children[index]

        pointer.is_leaf = True

    def search(self, key):
        pointer = self.root
        for level in range(len(key)):
            index = self._get_char_index(key[level])
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]

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




