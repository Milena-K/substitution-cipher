import sys
import csv
import pandas as pd


def write_dict_to_csv(dictionary, csv_file_name):
    with open(csv_file_name, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["letter", "frequency"])
        writer.writerows(zip(dictionary.keys(), dictionary.values()))
    print(f"Data successfully written to {csv_file_name}")


def find_frequency(count):
    for letter in count.keys():
        count[letter] = (count[letter] / len(text)) * 100
    return count


def sort_dictionary(dictionary):
    sorted_freq = {}
    for key in sorted(dictionary, key=dictionary.get, reverse=True):
        sorted_freq[key] = dictionary[key]
    return sorted_freq


def find_letter_frequency(text):
    letter_count = {}
    for _, letter in enumerate(text):
        if letter in letter_count.keys():
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return find_frequency(sort_dictionary(letter_count)) # there is one extra letter


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
        "П": ["и", "а", "о"],
        "Д": ["а", "о", "и"],

        "Љ": ["т", "н"],
        "Ѓ": ["н", "т"],

        "Ч": ["р", "с"],
        "У": ["с", "р"],

        "И": ["в", "д", "к"],
        "Ж": ["д", "к", "в"],
        "С": ["к", "в", "д"],
        #"Ц": ["в", "д", "к"],

        "Т": ["л", "п"],
        "Е": ["п", "л", "м", "у", "з"],

        "Л": ["м", "у", "з"],
        "Ј": ["у", "з", "м"],
        "Н": ["з", "м", "у"],
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

        #"Л": ["м", "у", "з"],
        #"Ј": ["м", "у", "з"],
        #"Н": ["м", "у", "з"],
    }

    transformed_text = transform_text(text, mappings)
    print(transformed_text)


def decrypt(text):
    mappings = {
        "Х": ["a"],
        "Ќ": ["о"],
        "Д": ["e"],
        "Љ": ["т"],
        "У": ["с"],
        "Ч": ["р"],
        "Ж": ["д"],
        "П": ["и"],
        "Ѓ": ["н"],
        "И": ["к"], # original i > v
        "С": ["в"], # original s > k
        "Ц": ["л"],
        "Т": ["м"], # original t > p

        "Ј": ["у"],

        # pronajdoci novi
        "Ѕ": ["ќ"],
        "З": ["б"],
        "Л": ["п"],
        "Џ": ["ч"], # M
        "К": ["ж"], # Ц Ж Ш Њ

        # Faza 3
        "Ш": ["њ"],
        "В": ["ш"],
        "Њ": ["ф"],
        "Р": ["ј"],
        "Н": ["з"],
        "Г": ["х"],
        "Е": ["г"],
        # "Ѓ": ["у"],
        "О": ["ц"],
        # faza 4
        "А": ["л"],
        "Ф": ["ѓ"],
    }
    transformed_text = transform_text(text, mappings)
    with open("final_transformation_super_sigurni.txt", "w") as f:
        f.write(transformed_text)
    print("Successfully decrypted text.")


def substitute_known_letters_csv(file_csv):
    mappings = {
        # 100% known letters
        "Х": ["a"],
        "Ќ": ["о"],
        "Д": ["e"],
        "Љ": ["т"],
        "У": ["с"],
        "Ч": ["р"],
        "Ж": ["д"],
        "П": ["и"],
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

    result_letter.pop("Ѝ") # extra letter with low freq
    write_dict_to_csv(result_letter, "letter_text.csv")
    write_dict_to_csv(result_bigram, "bigram_text.csv")
    write_dict_to_csv(result_trigram, "trigram_text.csv")


if __name__ == "__main__":
    file_name =sys.argv[1]
    bob_file = open(file_name, "r")
    text = bob_file.read()
    text = text[:-1]
    bob_file.close()

    # generate csv files, then visualize the data
    frequency_distribution_text(text)

    # decrypt trigrams found in text
    substitute_known_letters_csv("trigrams_text.csv")

    # build the mapping incrementally
    substitute_single_letters(text)
    decrypt(text)
