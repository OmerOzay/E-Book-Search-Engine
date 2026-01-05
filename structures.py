
#trie (prefix arama)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.book_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, title, book_id):
        node = self.root
        for char in title.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.book_ids.append(book_id)

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        self._collect_all_ids(node, results)
        return results

    def _collect_all_ids(self, node, results):
        if node.is_end_of_word:
            results.extend(node.book_ids)
        for child in node.children.values():
            self._collect_all_ids(child, results)

# BST
class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BookBST:
    def __init__(self):
        self.root = None

    def insert(self, book):
        if self.root is None:
            self.root = BSTNode(book)
        else:
            self._insert_recursive(self.root, book)

    def _insert_recursive(self, node, book):
        if book.book_id < node.book.book_id:
            if node.left is None:
                node.left = BSTNode(book)
            else:
                self._insert_recursive(node.left, book)
        elif book.book_id > node.book.book_id:
            if node.right is None:
                node.right = BSTNode(book)
            else:
                self._insert_recursive(node.right, book)

    def search(self, book_id):
        return self._search_recursive(self.root, book_id)

    def _search_recursive(self, node, book_id):
        if node is None or node.book.book_id == book_id:
            return node
        if book_id < node.book.book_id:
            return self._search_recursive(node.left, book_id)
        return self._search_recursive(node.right, book_id)

    def delete(self, book_id):
        self.root = self._delete_recursive(self.root, book_id)

    def _delete_recursive(self, node, book_id):
        if node is None: return node
        
        if book_id < node.book.book_id:
            node.left = self._delete_recursive(node.left, book_id)
        elif book_id > node.book.book_id:
            node.right = self._delete_recursive(node.right, book_id)
        else:
            if node.left is None: return node.right
            elif node.right is None: return node.left
            
            min_larger_node = self._min_value_node(node.right)
            node.book = min_larger_node.book
            node.right = self._delete_recursive(node.right, min_larger_node.book.book_id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current