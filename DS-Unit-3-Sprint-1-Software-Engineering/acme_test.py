import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_different_vales(self):
        """test the product with change"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(),'Kinda stealable') #added for stea.
        self.assertEqual(prod.explode(),'...boom!') #added for explode
        #setting up a test for different values
        prod = Product("test 2", price=15, weight=6)
        self.assertEqual(prod.stealability(),'Very stealable!')
        self.assertEqual(prod.explode(),'...fizzle')

class AcmeReportTests(unittest.TestCase):
    """test the report"""
    def test_default_num_products(self):
        gen = generate_products()
        self.assertEqual(len(gen), 30)

    def test_legal_names(self):
        gen = generate_products()
        for i in gen:
            first = i.name.split(' ')[0]
            sec = i.name.split(' ')[1]
            self.assertIn(first,ADJECTIVES)
            self.assertIn(sec,NOUNS)


if __name__ == '__main__':
    unittest.main()

"""
- Write a new test class `AcmeReportTests` with at least 2 test methods:
  `test_default_num_products` which checks that it really does receive a list of
  length 30, and `test_legal_names` which checks that the generated names for a
  default batch of products are all valid possible names to generate (adjective,
  space, noun, from the lists of possible words)

*Hint* - `test_legal_names` is the trickiest of these, but may not be as bad as
you think. Check out `assertIn` from `unittest`, and remember that Python is
pretty handy at string processing. But if you get stuck, move on and revisit.

Note that `inventory_report()` is pretty tricky to test, because it doesn't
*return* anything - it just prints (a "side-effect"). For the purposes of this
challenge, don't worry about testing it - but as a stretch goal/something to
think about, it's a good ponderer.
"""
