import sys


# TODO find the frequency of the most used bigrams and trigrams in the text.
# compare them with the bigrams and trigrams in the macedonian language
# substitute and repeat.

def format_csv_to_tuple(csv_file):
    """ Format the single, bigram and trigram csv files to tuples (A, 13.33)"""

    file = open(csv_file, "r")
    freq_tuple = [ tuple(row.strip().split(",")) for row in file ]
    freq_tuple = [ (chars, float(freq[:-1])) for (chars, freq) in freq_tuple]
    file.close()

    return freq_tuple


def transform_single_to_dictionary(csv_file):
    """The file must be ordered first, by frequency."""

    letter_freq_tuples = format_csv_to_tuple(csv_file)
    dict = {}
    for letter, freq in letter_freq_tuples:
        dict[letter] = freq

    return dict

def find_letter_frequency(text):
    letter_frequencies = {}
    for i, letter in enumerate(text):
        if letter in letter_frequencies.keys():
            letter_frequencies[letter] += 1
        else:
            letter_frequencies[letter] = 1

    sorted_letter_freq = {}
    for key in sorted(letter_frequencies, key=letter_frequencies.get, reverse=True):
        sorted_letter_freq[key] = letter_frequencies[key]

    for letter in sorted_letter_freq.keys():
        sorted_letter_freq[letter] = (sorted_letter_freq[letter] / len(text)) * 100

    return sorted_letter_freq


# take only the first 11 letters
def substitute_single_letters(text, single_letters):
    letter_frequency = find_letter_frequency(text)
    substitution = {}
    #merge only matching freq
    print(letter_frequency)
    print(single_letters)
    for a, b in zip(letter_frequency.keys(), single_letters.keys()):
        substitution[a] = b

    print(substitution)

    transformed_text = [""] * len(text)
    for i, letter in enumerate(text):
        if letter in substitution.keys():
            transformed_text[i] = substitution[letter].lower()

    return "".join(transformed_text)





if __name__ == "__main__":
    file_name =sys.argv[1]
    alice_file = open(file_name, "r")
    text = alice_file.read()
    alice_file.close()

    # already sorted
    bigrams_file = open("bigrams.csv", "r")
    bigrams = bigrams_file.read()
    bigrams_file.close()
    trigrams_file = open("trigrams.csv", "r")
    trigrams = trigrams_file.read()
    trigrams_file.close()

    single_letters = transform_single_to_dictionary("single.csv")
    result = substitute_single_letters(text, single_letters)
    print(result)
