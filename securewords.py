import argparse
import re
import os


def get_all_words_from_file(file_path):
    """
    Gets all words from the specified file. The delimiter between words will be
     a new line, and whitespace between each new line. File paths of example
     files should be placed in the examples dir

    :param file_path: path of the file to use when getting words from the file
    :return: a list of words from the file
    """
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file_path)
    all_words = []
    with open(file_path, 'r') as file:
        for line in file:
            all_words.extend(line.split())
    file.close()

    if not all_words:
        raise Exception("File is empty")

    return all_words


def get_longest_word(word_list):
    """
    Gets the longest word from a list of words. This function uses a validator
    function to determine if a word is valid. If there is more then one longest
    word, or the only words in the list are invalid an exception will be thrown.

    :param word_list: list of words
    :return:the longest valid word in the file.
    """
    longest_word = ['']
    for word in word_list:
        valid_word = validate_word(word)
        if valid_word:
            if len(word) > len(longest_word[0]):
                longest_word = [word]
            elif len(word) == len(longest_word[0]):
                longest_word.append(word)
        else:
            word_list.remove(word)
            print(f'{word} was removed for containing invalid characters')
            if not word_list:
                raise Exception("The file only contains invalid words")


    if len(longest_word) > 1:
        raise Exception("This file contains multiple longest words")
    return longest_word[0]


def validate_word(word):
    """
    This function contains the validation of words. Any word containing a
    character that is not a-z or capital A-Z will be considered invalid.
    This function has been separated in case future validation is needed

    :param word: a string to validate
    :return: boolean
    """
    validated = bool(re.match('^[a-zA-Z]+$', word))
    return validated


wordlist = get_all_words_from_file('examples\\emptyfile.txt')
longestword = get_longest_word(wordlist)
print(longestword[::-1])
