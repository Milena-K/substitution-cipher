import random


def encrypt_text(text, key):
    print(key)
    print()
    encrypted_text = [''] * len(text)
    for i, letter in enumerate(text):
        encrypted_text[i] = key[letter]

    encrypted_text = "".join(encrypted_text)
    encrypted_file = open("encrypted_alice.txt", "w")
    encrypted_file.write(encrypted_text)
    encrypted_file.close()


if __name__ == "__main__":
    text = "alice.txt"
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Ѓ', 'Е', 'Ж', 'З', 'Ѕ', 'И', 'Ј', 'К', 'Л', 'Љ', 'М', 'Н', 'Њ', 'О', 'П', 'Р', 'С', 'Т', 'Ќ', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Џ', 'Ш']

    alice_file = open(text, "r")
    content = alice_file.read().upper()
    alice_file.close()

    clean_text = "".join([ a for a in content if a in alphabet ])
    substitution = random.sample(list(range(0,31)), 31)
    encryption_key = {}
    for i in range(0,31):
        encryption_key[alphabet[i]] = alphabet[substitution[i]]

    encrypt_text(clean_text, encryption_key)

    ## test
    # encrypt_text("МИЛЕНА", encryption_key)
