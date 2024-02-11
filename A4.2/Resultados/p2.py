"""Converts numbers in a file to binary and hexadecimal."""

import sys
import time

def convert_to_binary(number):
    """Converts a decimal number to binary."""
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def convert_to_hexadecimal(number):
    """Converts a decimal number to hexadecimal."""
    hexadecimal = ""
    digits = "0123456789ABCDEF"
    while number > 0:
        hexadecimal = digits[number % 16] + hexadecimal
        number //= 16
    return hexadecimal

def main():
    """Main function to handle file input, conversion, and output."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]

    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid data in file: {line.strip()}")

    start_time = time.time()

    conversions = []
    for number in numbers:
        binary = convert_to_binary(number)
        hexadecimal = convert_to_hexadecimal(number)
        conversions.append((number, binary, hexadecimal))

    elapsed_time = time.time() - start_time

    results = f"""
Conversions:
{'-' * 25}
Number | Binary | Hexadecimal
{'-' * 25}
{''.join(f"{number:10} | {binary:10} | {hexadecimal:10}" for number, binary, hexadecimal in conversions)}
Execution Time: {elapsed_time:.4f} seconds
"""

    print(results)

    with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
        file.write(results)

if __name__ == "__main__":
    main()
