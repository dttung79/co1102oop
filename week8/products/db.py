from product import Product
from tkinter import messagebox
def load_products():
    products = []
    try:
        f = open("products.csv", "r")
        lines = f.readlines()

        for line in lines:
            name, price, stock = line.strip().split(",")
            p = Product(name, float(price), int(stock))
            products.append(p)
        f.close()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")

    return products

def save_products(products):
    f = open("products.csv", "w")
    for p in products:
        f.write(f"{p.name},{p.price},{p.stock}\n")
    f.close()