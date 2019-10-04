import random

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """creates a new product"""
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 10000000)

    def stealability(self):
        """gets the change of it being stolen"""
        ratio = self.price / self.weight
        if ratio < 0.5:
            return('Not so stealable')
        elif ratio >= 0.5 and ratio < 1.0:
            return('Kinda stealable')
        else:
            return('Very stealable!')


    def explode(self):
        """determains if it will explode or not"""
        proba = self.flammability * self.weight
        if proba < 10:
            return('...fizzle')
        elif proba >= 10 and proba < 50:
            return('...boom!')
        else:
            return('...BABOOM!!')

class BoxingGlove(Product):
    """Override the product funtion"""
    def __init__(self, name, weight=10):
        super().__init__(name, weight=10)
        self.weight = weight

    def explode(self):
        """returns globe"""
        return("It's a golve.")

    def punch(self):
        """returns a punch"""
        punchval = self.weight
        if punchval < 5:
            return('That tickles')
        elif punchval >= 5 and punchval < 15:
            return('Hey that hurt!')
        else:
            return('OUCH!')
