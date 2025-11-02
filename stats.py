def get_word_count(file_contents):
    words_in_file = file_contents.split()   #   splits into individual words
    return len(words_in_file)

def get_letter_counts(file_contents):
    char_counts_dict = {}
    file_contents = file_contents.lower()   #   makes all characters lowercase
    split_chars = list(file_contents)       #   split_chars = individual lowercase characters
    for i in split_chars:
        if i in char_counts_dict:           #   adds 1 for each char already in dictionary
            char_counts_dict[i] += 1
        if i not in char_counts_dict:       #   creates new key for new char
            char_counts_dict[i] = 1
    return char_counts_dict
