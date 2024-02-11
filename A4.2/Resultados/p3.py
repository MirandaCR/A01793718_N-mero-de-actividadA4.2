"""Counts word frequencies in a file."""

import sys
import time

def count_word_frequencies(words):
    """Counts the frequency of each word in a list of words."""
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def main():
    """Main function to handle file input, word counting, and output."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]

    words = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                try:
                    words.append(word.strip())
                except ValueError:
                    print(f"Invalid data in file: {word}")

    start_time = time.time()

    word_counts = count_word_frequencies(words)

    elapsed_time = time.time() - start_time

    results = f"""
Word Counts:
{'-' * 25}
Word | Frequency
{'-' * 25}
{''.join(f"{word:10} | {count:10}" for word, count in word_counts.items())}
Execution Time: {elapsed_time:.4f} seconds
"""

    print(results)

    with open("WordCountResults.txt", "w", encoding="utf-8") as file:
        file.write(results)

if __name__ == "__main__":
    main()
