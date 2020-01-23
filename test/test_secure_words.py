import unittest
from securewords import get_words_from_file, get_longest_word, validate_word
from securewords import main, transpose_word


class TestPositiveSecureWords(unittest.TestCase):

    def test_example_file(self):
        """
        A basic file with valid words separated by new lines
        """
        word_list = get_words_from_file(file_path='examples\example.txt')
        self.assertEqual(word_list, ['a', 'ab', 'abc', 'abcd', 'abcde'])

    def test_file_with_spaces(self):
        """
        A file with new line and whitespace separating words
        """
        word_list = get_words_from_file(
            file_path='examples\\file_with_spaces.txt')
        self.assertEqual(word_list, ['a', 'b', 'cd', 'cd', 'abcde', 'abc'])

    def test_empty_file_throws_exception(self):
        """
        A file with no words will throw an exception
        """
        self.assertRaises(
            Exception,
            get_words_from_file, 'examples\emptyfile.txt')

    def test_get_longest_word(self):
        """
        The function should return the longest word
        """
        word_list = ['a', 'ab', 'abc', 'abcd', 'abcde']
        longest_word = get_longest_word(word_list)
        self.assertEqual(longest_word, 'abcde')

    def test_get_longest_word_longest_first(self):
        """
        Order should not impact the ability to get the largest word
        """
        word_list = ['a', 'abcde', 'ab', 'abc', 'abcd']
        longest_word = get_longest_word(word_list)
        self.assertEqual(longest_word, 'abcde')

    def test_all_invalid_words(self):
        """
        If there are no valid words an exception is raised
        """
        word_list = ['1', '&^', 'abcd***']
        self.assertRaises(Exception, get_longest_word, word_list)

    def test_two_largest_words(self):
        """
        Two longest words will raise an exception
        """
        word_list = ['a', 'abc', 'abc']
        self.assertRaises(Exception, get_longest_word, word_list)

    def test_valid_validator(self):
        """
        Tests valid input for the word validator
        """
        valid_input = ['test', 'a', 'string']
        for word in valid_input:
            valid = validate_word(word)
            self.assertTrue(valid)

    def test_invalid_validator(self):
        """
        Tests invalid inputs for the word validator
        """
        invalid_input = ['1', '##$', 'a1#']
        for word in invalid_input:
            invalid_input = validate_word(word)
            self.assertFalse(invalid_input)

    def test_tranpose_word(self):
        word = 'test'
        transposed_word = transpose_word(word)
        self.assertEqual(transposed_word, 'tset')

    def test_functional(self):
        """
        Tests the entire script and output.
        """
        main()


if __name__ == '__main__':
    unittest.main()
