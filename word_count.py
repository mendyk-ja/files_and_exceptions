def count_words(filename):
    """Counting approximated number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, but file '{filename}' doesn't exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"File {filename} consists of {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
