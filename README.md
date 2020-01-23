### Secure Words

A simple project that takes a file with words, finds the largest and then transposes that word.

A valid word will contain only alphabetical letters, A–Z or a–z. Any other word will be removed from consideration as the longest word.
If there are multiple longest words the application will exit and let the user know. The application will check for a newline and/or whitespace to determine if there is a new word.

###Getting started
The securewords application, only accepts one input. The path to the file must be provided.
To run the script simply run the script. If no file is provided the default example.txt will be used:

`python securewords.py --filepath <path_to_file>`