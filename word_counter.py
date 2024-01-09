from collections import Counter
import string #provides a collection of functions and constants to manipulate strings eg.lower, punctuation.upper etc

def process_word(word):
    removed_word = word.strip(string.punctuation + " ").lower()
    #removes all punctutations and spaces, converts to lowercase
    return(removed_word)



def create_frequency_dict(file_path):
    word_frequency = Counter()

    with open(file_path, mode = 'r') as file:
        for line in file:
            word = line.split()
            removed_word = map(process_word, word)
            word_frequency.update(filter(None, list(removed_word)))
    #return (word_frequency)
    sorted_frequency = dict(sorted(word_frequency.items(), key = lambda item:item[1], reverse=True))
    return sorted_frequency
file_path = 'words.txt'
results = create_frequency_dict(file_path)
for word, frequency in results.items():
    print (f'{word}: {frequency}')
