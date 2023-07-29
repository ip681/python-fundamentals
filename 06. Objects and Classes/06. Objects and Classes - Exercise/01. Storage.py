class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if self.capacity - 1 >= 0:
            self.storage.append(product)
            self.capacity -= 1

    def get_products(self):
        return self.storage
