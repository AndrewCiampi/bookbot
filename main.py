def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    string_Frank = (len(text.split()))
    print(f"Word count is: {string_Frank}")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()