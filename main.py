# main.py
from engine import LibraryEngine

def print_menu():
    print("\n--- Kütüphane Yönetim Sistemi ---")
    print("1. Kitap Ekle")
    print("2. Başlığa Göre Ara (Prefix)")
    print("3. Son İşlemi Geri Al (Undo)")
    print("4. Tüm Kitapları Listele (Varsa)")
    print("5. Çıkış")
    print("---------------------------------")

def main():
    lib = LibraryEngine()
    
    while True:
        print_menu()
        choice = input("Yapmak istediğiniz işlemi seçin (1-5): ")

        if choice == "1":
            try:
                book_id = int(input("Kitap ID: "))
                kitapAd = input("Kitap Adı: ")
                yazar = input("Yazar: ")
                kategori = input("Kategori: ")
                lib.add_book(book_id, kitapAd, yazar, kategori)
                print(f"\n> '{kitapAd}' başarıyla eklendi.")
            except ValueError:
                print("\n! Hata: ID sayısal bir değer olmalıdır.")

        elif choice == "2":
            prefix = input("Aramak istediğiniz başligin ilk harflerini giriniz: ")
            print(f"\n--- '{prefix}' ile başlayan sonuçlar ---")
            lib.search_by_title(prefix)

        elif choice == "3":
            print("\n> Son işlem geri alınıyor...")
            lib.undo_last_action()

        elif choice == "4":
            print("\n--- Kütüphane İçeriği ---")
            lib.search_by_title("")

        elif choice == "5":
            print("Sistemden çıkılıyor...")
            break

        else:
            print("\n! Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()