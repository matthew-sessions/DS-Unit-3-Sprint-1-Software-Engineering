from acme import Product
import random
from random import randint, sample, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """generates 30 products"""
    products = []
    for i in range(num_products):
        adj = random.choice(ADJECTIVES)
        noun = random.choice(NOUNS)
        name = f"{adj} {noun}"
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        products.append(Product(name,price,weight,flammability))
    return(products)

def inventory_report(products):
    """provites a report for all the features of the products"""
    names = [i.name for i in products]
    price = [i.price for i in products]
    weight = [i.weight for i in products]
    flammability = [i.flammability for i in products]
    nameun = []
    for i in names:
        if i not in nameun:
            nameun.append(i)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(nameun)}')
    print(f'Average price: {sum(price)/len(price)}')
    print(f'Average weight: {sum(weight)/len(weight)}')
    print(f'Average flammability: {sum(flammability)/len(flammability)}')



if __name__ == '__main__':
    inventory_report(generate_products())
