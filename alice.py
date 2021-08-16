filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, but file '{filename}' doesn't exist.")
else:
    # Counting of approximated number  of words.
    words = contents.split()
    num_words = len(words)
    print(f"File {filename} consists of {num_words} words.")