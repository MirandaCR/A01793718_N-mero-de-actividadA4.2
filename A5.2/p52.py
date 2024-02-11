"""Modules for the code"""


import json
import sys
import time


def load_json_file(filename):
    """
    Loads JSON data from a file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: The JSON data loaded from the file.
              If the file is not found or the JSON format is invalid,
              returns an empty dictionary.

    Raises:
        FileNotFoundError: If the file is not found.
        json.JSONDecodeError: If the JSON format is invalid.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{filename}'.")
        return {}
    except ImportError:
        print("Error Loading")
        return {}


def compute_total_cost(price_catalogue, sales_record):
    """
    Computes the total cost of sales based on a price catalogue and
    sales record.

    Args:
        price_catalogue (list): List of dictionaries representing
                                the price catalogue.
        sales_record (list): List of dictionaries representing
                            the sales record.

    Returns:
        float: The total cost of all sales.

    Prints warnings for items not found in the price catalogue.
    """
    total_cost = 0
    for sale in sales_record:
        item = sale['Product']
        quantity = sale['Quantity']
        matching_items = [
            prod for prod in price_catalogue if prod.get('title') == item
        ]
        if matching_items:
            price = matching_items[0]['price']
            total_cost += price * quantity
        else:
            print(f"Warning: Item '{item}' not found in price catalogue.")

    return total_cost


def main():
    """
    Main function to compute total sales cost.

    Reads a price catalogue and a sales record from JSON files,
    computes the total cost of all sales, and writes the result to a
    text file.

    Validates command-line arguments and gracefully handles errors.
    """
    if len(sys.argv) != 3:
        print("Usage: compute_sales.py priceCatalogue.json salesRecord.json")
        return

    start_time = time.time()

    try:
        price_catalogue = load_json_file(sys.argv[1])
        sales_record = load_json_file(sys.argv[2])
    except (FileNotFoundError, json.JSONDecodeError) as exception:
        print(f"An error occurred: {exception}")
        return

    total_cost = compute_total_cost(price_catalogue, sales_record)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Total cost of all sales:", total_cost)
    print("Time elapsed:", elapsed_time, "seconds")

    try:
        with open("SalesResults.txt", "w", encoding='utf-8') as results_file:
            results_file.write(f"Total cost of sales: {total_cost}\n")
            results_file.write(f"Time elapsed: {elapsed_time} seconds\n")
    except ImportError:
        print("Error Loading")


if __name__ == "__main__":
    main()
