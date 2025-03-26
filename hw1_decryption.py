# steps to attack a text encrypted with permutation:
# 1. find out the key length (31)
# 2. split the text in key length chunks (check)
# 3. find out the most frequently used digraphs and triplets
# 4. reorder the letters in the chunk so that they match them
# 5. manually find out the right position to place the chunk (hard) (best guess)
#
# reordered letters are small
#
# 6. read more about tabu search attack on permutation cipher
# 7. do the first part of frequency attack so that i have some possible keys.
# 8. read this and code it up https://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html

#####
##### The way to break a permutation cipher
##### is to try out different permutations
##### until you find a first block that makes sense.
#####
import sys

def format_csv_to_tuple(csv_file):

    file = open(csv_file, "r")
    # trigrams_file = open("trigrams.csv", "r")

    freq_tuple = [ tuple(row.strip().split(",")) for row in file ]

    freq_tuple = [ (chars, float(freq[:-1])) for (chars, freq) in freq_tuple]

    return freq_tuple


def transform_bigrams_to_dictionary(bigram_list):
    '''the bigram list must be ordered first, by frequency.'''
    bigram_dict = {}
    for bigram, freq in bigram_list:
        first_letter = bigram[0]
        second_letter = bigram[1]
        if first_letter in bigram_dict.keys():
            bigram_dict[first_letter].append(second_letter)
        else:
            bigram_dict[first_letter] = [second_letter]

    print(bigram_dict)


# TODO transform_trigrams_to_dictionary(trigrams_list)


bigrams = format_csv_to_tuple("bigrams.csv")
bigram_dict = transform_bigrams_to_dictionary(bigrams)

trigrams = format_csv_to_tuple("trigrams.csv")


def build_bigrams(chunk, bigram_ first_chunk):
    bigrams_found = []
    print(chunk)
    print()
    print(first_chunk)

    for letter in chunk:



if __name__ == "__main__":
    text=sys.argv[1]
    alice_file = open(text, "r")
    content = alice_file.read()

    chunks = []
    first_chunk = content[:31]
    for i in range(0, len(content), 31):
        chunk = content[i:i+31]
        chunk_tuple = [(c, j) for j, c in enumerate(chunk)]
        chunks.append(chunk_tuple)

    # they are sorted already
    # transform them to dictionary
    print(bigrams)
    print()
    # print(trigrams)
    build_bigrams(chunks[0], bigram_dict, first_chunk)
    #
