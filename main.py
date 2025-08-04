import sys
from stats import count_words
from stats import count_symbols
from stats import sort_dic


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = count_words(text)
    symbols = count_symbols(text)
    sorted_list = sort_dic(symbols)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted_list)):
        if sorted_list[i]['char'].isalpha():
            print(f"{sorted_list[i]['char']}: {sorted_list[i]['num']}")

main()
