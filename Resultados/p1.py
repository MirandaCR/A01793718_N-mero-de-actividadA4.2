"""Computes descriptive statistics from a file of numbers."""

import sys
import time

def calculate_mean(numbers):
    """Calculates the mean of a list of numbers."""
    total = sum(numbers)
    return total / len(numbers)

def calculate_median(numbers):
    """Calculates the median of a list of numbers."""
    numbers.sort()
    middle_index = len(numbers) // 2
    return (
        (numbers[middle_index - 1] + numbers[middle_index]) / 2
        if len(numbers) % 2 == 0
        else numbers[middle_index]
    )

def calculate_mode(numbers):
    """Calculates the mode(s) of a list of numbers."""
    mode_counts = {}
    for number in numbers:
        mode_counts[number] = mode_counts.get(number, 0) + 1
    max_count = max(mode_counts.values())
    return [number for number, count in mode_counts.items() if count == max_count]

def calculate_variance(numbers, mean):
    """Calculates the variance of a list of numbers."""
    deviations = [(number - mean) ** 2 for number in numbers]
    return sum(deviations) / len(numbers)

def calculate_standard_deviation(variance):
    """Calculates the standard deviation from the variance."""
    return variance ** 0.5

def main():
    """Main function to handle file input, statistics calculation, and output."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]

    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid data in file: {line.strip()}")

    start_time = time.time()

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    modes = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    standard_deviation = calculate_standard_deviation(variance)

    elapsed_time = time.time() - start_time

    results = f"""
Mean: {mean}
Median: {median}
Modes: {modes}
Variance: {variance}
Standard Deviation: {standard_deviation}
Execution Time: {elapsed_time:.4f} seconds
"""

    print(results)

    with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
        file.write(results)

if __name__ == "__main__":
    main()
