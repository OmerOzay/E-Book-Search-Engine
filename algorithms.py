# algorithms.py

def merge_sort(book_list):
    #Kitap listesini başlığa göre alfabetik sıralar
    if len(book_list) <= 1:
        return book_list

    mid = len(book_list) // 2
    left_half = merge_sort(book_list[:mid])
    right_half = merge_sort(book_list[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].title.lower() < right[j].title.lower():
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list