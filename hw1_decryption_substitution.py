import sys
import csv
import pandas as pd

# TODO: visualize the frequencies in the text and compare with mk lang
# substitute and pray to find similarities

# PLAN: find the frequency of the most used bigrams and trigrams in the text.
# compare them with the bigrams and trigrams in the macedonian language
# substitute and repeat.

def format_csv_to_tuple(csv_file):
    """ Format the single, bigram and trigram csv files to tuples (A, 13.33)"""
    csv_file = open(csv_file, "r")
    freq_tuple = [ tuple(row.strip().split(",")) for row in csv_file ]
    freq_tuple = [ (chars, float(freq[:-1])) for (chars, freq) in freq_tuple]
    csv_file.close()
    return freq_tuple


def write_dict_to_csv(dictionary, csv_file_name):
    with open(csv_file_name, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(zip(dictionary.keys(), dictionary.values()))
    print(f"Data successfully written to {csv_file_name}")


def transform_to_dictionary(csv_file):
    """The file must be ordered first, by frequency."""
    letters_freq_tuples = format_csv_to_tuple(csv_file)
    dict = {}
    for letters, freq in letters_freq_tuples:
        dict[letters] = freq
    return dict


def find_frequency(dictionary):
    for letter in dictionary.keys():
        dictionary[letter] = (dictionary[letter] / len(text)) * 100
    return dictionary


def sort_dictionary(dictionary):
    sorted_freq = {}
    for key in sorted(dictionary, key=dictionary.get, reverse=True):
        sorted_freq[key] = dictionary[key]
    return sorted_freq


def find_letter_frequency(text):
    letter_count = {}
    for i, letter in enumerate(text):
        if letter in letter_count.keys():
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return find_frequency(sort_dictionary(letter_count))


def find_bigram_frequency(text):
    bigrams = {}
    previous_letter = ""
    for next_letter in text:
        bigram = f"{previous_letter}{next_letter}"
        previous_letter = next_letter
        if bigram in bigrams.keys():
            bigrams[bigram] += 1
        else:
            bigrams[bigram] = 1
    return sort_dictionary(find_frequency(bigrams))


def find_trigram_frequency(text):
    trigrams = {}
    i = 2
    while i < len(text):
        first_letter = text[i-2]
        middle_letter = text[i-1]
        last_letter = text[i]
        trigram = f"{first_letter}{middle_letter}{last_letter}"
        if trigram in trigrams.keys():
            trigrams[trigram] += 1
        else:
            trigrams[trigram] = 1
        i += 1
    return sort_dictionary(find_frequency(trigrams))


def transform_text(text, mappings):
    transformed_text = [""] * len(text)
    for i, letter in enumerate(text):
        if letter in mappings.keys():
            transformed_text[i] = mappings[letter][0]
        else:
            transformed_text[i] = letter

    return "".join(transformed_text)


def substitute_single_letters(text):
    # TODO: ovie mappings treba da se narrownat down uste so pomosh na bigrams.
    # za da mozam da vidam koi bukvi se edni do drugi najchesto i da izoliram sto e mozhno povekje bukvi.
    mappings = {
        "Х": ["a"],

        "Ќ": ["о", "и", "а"],
        "П": ["о", "и", "а"],
        "Д": ["о", "и", "а"],

        "Љ": ["т", "н"],
        "Ѓ": ["т", "н"],

        "Ч": ["р", "с"],
        "У": ["р", "с"],

        "И": ["в", "д", "к"],
        "Ж": ["в", "д", "к"],
        "С": ["в", "д", "к"],
        "Ц": ["в", "д", "к"],

        "Т": ["л", "п"],
        "Е": ["л", "п", "м", "у", "з"],

        "Л": ["м", "у", "з"],
        "Ј": ["м", "у", "з"],
        "Н": ["м", "у", "з"],
    }

    transformed_text = transform_text(text, mappings)
    print(transformed_text)


def substitute_bigrams(text):
    mappings = {
        "Х": ["a"],

        "Ќ": ["о"],
        "П": ["и"],
        "Д": ["e"],

        # mozhe da se zamenat Lj i Gj
        "Љ": ["т"],
        "Ѓ": ["н"],

        "Ч": ["р"],
        "У": ["с"],

        "И": ["в"],
        # mozhe da se zamenat
        "Ж": ["д"],
        "С": ["к"],
        #"Ц": ["д", "к"],

        "Т": ["п"],

        "Е": ["л", "м", "у", "з"],

        "Л": ["м", "у", "з"],
        "Ј": ["м", "у", "з"],
        "Н": ["м", "у", "з"],
    }
    transformed_text = transform_text(text, mappings)
    print(transformed_text)



# TODO
def substitute_trigrams(text):
    mappings = {
        "Х": ["a"],

        "Ќ": ["о"],
        "П": ["и"],
        "Д": ["e"],

        # mozhe da se zamenat Lj i Gj
        "Љ": ["т"],
        "Ѓ": ["н"],
        ###########

        "Ч": ["р"],
        "У": ["с"],

        "И": ["в"],
        # mozhe da se zamenat
        "Ж": ["д"],
        "С": ["к"],
        ###########

        "Т": ["п"],
        # ne se sigurni
        # "Е": ["л"], # m, u, z

        # "Л": ["м"], # m, u, z
        # "Ј": ["у"], # m, u, z
        # "Н": ["з"], # m, u, z
    }
    transformed_text = transform_text(text, mappings)
    with open("final_transformation_sigurni.txt", "w") as f:
        f.write(transformed_text)

    print(transformed_text)

def substitute_known_letters_csv(file_csv):
    mappings = {
        "Х": ["a"],

        "Ќ": ["о"],
        "П": ["и"],
        "Д": ["e"],

        # mozhe da se zamenat Lj i Gj
        "Љ": ["т"],
        "Ѓ": ["н"],

        "Ч": ["р"],
        "У": ["с"],

        "И": ["в"],
        # mozhe da se zamenat
        "Ж": ["д"],
        "С": ["к"],
        #"Ц": ["д", "к"],

        "Т": ["п"],
    }

    df = pd.read_csv(file_csv)

    for i, trigrams in enumerate(df["letter"]):
        decrypted_trigram = ""
        for letter in trigrams:
            if letter in mappings.keys():
                decrypted_trigram += mappings[letter][0]
            else:
                decrypted_trigram += letter
        df.loc[i, "letter"] = decrypted_trigram

    df.to_csv("trigrams_decrypted.csv", index=False)
    print("Data successfully written to trigrams_decrypted.csv")

def frequency_distribution_text(text):

    result_letter = find_letter_frequency(text)
    result_bigram = find_bigram_frequency(text)
    result_trigram = find_trigram_frequency(text)

    write_dict_to_csv(result_letter, "letter_text.csv")
    write_dict_to_csv(result_bigram, "bigram_text.csv")
    write_dict_to_csv(result_trigram, "trigram_text.csv")
    substitute_known_letters_csv("trigrams_text.csv")


if __name__ == "__main__":
    file_name =sys.argv[1]
    bob_file = open(file_name, "r")
    text = bob_file.read()
    text = text[:-1]
    bob_file.close()

    letter_file = open("letter.csv", "r")
    letter_csv = letter_file.read()
    letter_file.close()

    bigrams_file = open("bigrams.csv", "r")
    bigrams_csv = bigrams_file.read()
    bigrams_file.close()

    trigrams_file = open("trigrams.csv", "r")
    trigrams_csv = trigrams_file.read()
    trigrams_file.close()

    # frequency_distribution_text(text)

    # substitute_single_letters(text)
    substitute_trigrams(text)
