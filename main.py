def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = get_num_words(text)
    print(num_words)
    chars_dict = get_chars_dict(text)
    print(chars_dict)
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()