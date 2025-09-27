# 4) Product Data Transformer (lambda, map, filter, zip)
#    - Ask user for a list of product names (comma-separated).
#    - Ask user for a list of product prices (comma-separated).
#    - Process them by:
#         - Pairing product with price.
#         - Filtering out items where price <= 0.
#         - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
#    - Save the final result as JSON into "products.json".
#    - Print a preview of the first 5 results.

import json 
from time_decorator import log_time

@log_time
def product_transformer():
    while True:
        names = input("Enter product names (comma-separated): ").strip().split(",")
        prices_input = input("Enter product prices (comma-separated): ").strip().split(",")
        prices = list(map(float, prices_input))

        try:
            if len(names) != len(prices):
                raise ValueError("Names and prices count mismatch.")
            break
        except ValueError:
            print("Invalid input. Please try again.")

    products = list(zip(names, prices))
    filtered = filter(lambda p: p[1] > 0, products)
    transformed = list(map(lambda p: {"product": p[0].strip(), "price": p[1], "discounted": round(p[1] * 0.9)}, filtered))

    with open("output_files/products.json", "w") as f:
        json.dump(transformed, f, indent=4)

    print("Products saved to output_files/products.json")
    print("Preview:", transformed[:5])

if __name__ == "__main__":
    product_transformer()   

