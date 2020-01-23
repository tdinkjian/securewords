import argparse
import re
import os

def get_words_from_file(file_path):
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
            print(f'{word} Is an invalid word, it will not be considered')

    if len(longest_word) > 1:
        raise Exception("This file contains multiple longest words")
    if len(longest_word[0]) == 0:
        raise Exception("The file contains no valid words")

    return longest_word[0]


def validate_word(word):
    """
    This function contains the validation of words. Any word containing a
    character that is not a-z or capital A-Z will be considered invalid.
    This function has been separated if future validation is needed

    :param word: a string to validate
    :return: boolean
    """
    validated = bool(re.match('^[a-zA-Z]+$', word))
    return validated


def transpose_word(word):
    """
    Takes a word and transposes it.

    :param word: string to transpose
    :return: transposed word as a string
    """
    return  word[::-1]


def main():
    """
    Main function, argparse is used to get the file path.
    The application will assume the file is in the securewords directory.
    This is mostly done to prevent having to put full paths to files.
    """
    default_path = os.path.join('examples', 'example.txt')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--filepath',
        default=default_path,
        help='The path to the file to to check, must be placed in'
             'securewords dir')
    args = parser.parse_args()

    wordlist = get_words_from_file(args.filepath)
    longestword = get_longest_word(wordlist)
    transposedword = transpose_word(longestword)
    print(f'The longest word is: {longestword}')
    print(f'The longest word transposed is: {transposedword}')


if __name__ == "__main__":
    main()
