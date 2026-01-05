# engine.py
import time
from models import Book
from structures import BookBST, Trie
from algorithms import merge_sort

class LibraryEngine:
    def __init__(self):
        self.book_storage = BookBST()
        self.title_index = Trie()
        self.undo_stack = [] 

    def add_book(self, book_id, title, author, category):
        new_book = Book(book_id, title, author, category)
        self.book_storage.insert(new_book)
        self.title_index.insert(title, book_id)
        self.undo_stack.append(('ADD', book_id, title))
        print(f"✅ Eklendi: {title}")

    def search_by_title(self, prefix):
        print(f"\n🔍 Arama: '{prefix}'")
        start_time = time.time()
        
        found_ids = self.title_index.search_prefix(prefix)
        results = []
        for b_id in found_ids:
            node = self.book_storage.search(b_id)
            if node:
                results.append(node.book)
        
        sorted_results = merge_sort(results)
        
        if not sorted_results:
            print("   (Sonuç bulunamadı)")
        else:
            for book in sorted_results:
                print(f"   -> {book}")
            
        print(f"⏱️  Süre: {(time.time() - start_time):.6f} sn")

    def undo_last_action(self):
        print("\n⏪ Geri Alma İşlemi...")
        if not self.undo_stack:
            print(" !!! Geri alınacak işlem yok.")
            return

        action, book_id, title = self.undo_stack.pop()
        
        if action == 'ADD':
            self.book_storage.delete(book_id)
            print(f"'{title}' (ID: {book_id}) silindi.")