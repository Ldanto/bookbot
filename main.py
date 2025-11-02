from stats import get_word_count, get_letter_counts

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    print(get_letter_counts(text))



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#def get_word_count(file_contents):
 #   words_in_file = file_contents.split()
 #   return len(words_in_file)


   
main()