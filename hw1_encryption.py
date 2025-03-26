import random


def encrypt_text(clean_text, encryption_key):
    # the key
    chunks = [ clean_text[i:i+31] for i in range(0, len(clean_text), 31)]

    # check if last chunk has 31 letters, if not then pad it.
    last_chunk_length = len(chunks[-1])
    if last_chunk_length < 31:
        padding = [ "А" for i in range(0, 31-last_chunk_length) ]
        padded_chunk = chunks[-1] + "".join(padding)
        chunks[-1] = padded_chunk

    encrypted_text = []
    for chunk in chunks:
        permutated_dict= [ (letter, encryption_key[ind]) for ind, letter in enumerate(chunk) ]
        permutated_chunk = sorted(permutated_dict, key=lambda k: k[1])
        transform_str_chunk = [ item[0] for item in permutated_chunk]
        transform_str_chunk = "".join(transform_str_chunk)
        encrypted_text.append(transform_str_chunk)

    encrypted_text = "".join(encrypted_text)
    print(encrypted_text)

    encrypted_file = open("encrypted_alice.txt", "w")
    encrypted_file.write(encrypted_text)


if __name__ == "__main__":
    text = "alice.txt"
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Ѓ', 'Е', 'Ж', 'З', 'Ѕ', 'И', 'Ј', 'К', 'Л', 'Љ', 'М', 'Н', 'Њ', 'О', 'П', 'Р', 'С', 'Т', 'Ќ', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Џ', 'Ш']

    clean_text = ""
    alice_file = open(text, "r")
    content = alice_file.read().upper()
    alice_file.close()

    clean_text = clean_text.join([ a for a in content if a in alphabet ])
    encryption_key = random.sample(list(range(0,31)), 31)
    encrypt_text(clean_text, encryption_key)
