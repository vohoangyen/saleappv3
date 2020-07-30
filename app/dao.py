import json


def read_products():
    with open("data/products.json", encoding="utf-8") as f:
        json.load(f)


if __name__ == "__main__":
    print(read_products())

