from stats import get_word_count, get_letter_counts, sort_by_quantity
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_sorted_high_to_low = sort_by_quantity(get_letter_counts(text))
    print_report(book_path, num_words, char_sorted_high_to_low)
    

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_report(book_path, num_words, char_sorted_high_to_low):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_high_to_low:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()