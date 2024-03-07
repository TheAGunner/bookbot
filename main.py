def main():
    book_path = "/home/theagunner/workspace/theagunner/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_dict = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)
    print_dict(sorted_chars_dict, num_words)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_dict(chars_dict, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    for char, count in chars_dict:
        print(f"The '{char}' character was found {count} times")

main()
